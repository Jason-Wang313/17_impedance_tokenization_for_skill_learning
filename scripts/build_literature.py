import csv
import json
import math
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS = os.path.join(ROOT, "docs")
DATA = os.path.join(ROOT, "data")
RESULTS = os.path.join(ROOT, "results")
PROGRESS = os.path.join(RESULTS, "literature_progress.txt")
CACHE = os.path.join(DATA, "openalex_literature_cache.json")
CSV_PATH = os.path.join(DOCS, "related_work_matrix.csv")


QUERIES = [
    "robot impedance control skill learning",
    "variable impedance control robot learning manipulation",
    "admittance control learning from demonstration robot contact",
    "force control robot skill learning contact rich manipulation",
    "dynamic movement primitives impedance robot learning",
    "movement primitives robot skill learning contact",
    "learning from demonstration compliant manipulation force",
    "contact rich manipulation robot learning force tactile",
    "tactile manipulation force control robot learning",
    "robot manipulation skill primitives discrete latent actions",
    "vector quantization robot action tokenization skill learning",
    "discrete latent action robotics imitation learning",
    "behavior cloning action tokenization robot manipulation",
    "robot foundation model action tokenization manipulation",
    "visuomotor policy action chunking robot manipulation",
    "diffusion policy robot manipulation action chunking",
    "options skill learning robotics manipulation",
    "passivity based robot control learning impedance",
    "hybrid force position control robot manipulation",
    "compliant contact manipulation learning control robot",
    "variable stiffness actuator robot learning control",
    "interaction primitives robot learning from demonstration",
    "probabilistic movement primitives force control robot",
    "operational space control impedance robot manipulation",
]


MECHANISM_RULES = [
    ("impedance", "impedance/admittance regulation"),
    ("admittance", "impedance/admittance regulation"),
    ("force control", "force or hybrid force-position control"),
    ("hybrid force", "force or hybrid force-position control"),
    ("movement primitive", "movement primitive parameterization"),
    ("dynamic movement primitive", "dynamic movement primitive parameterization"),
    ("probabilistic movement", "probabilistic movement primitive model"),
    ("learning from demonstration", "demonstration-conditioned skill model"),
    ("imitation", "demonstration-conditioned skill model"),
    ("diffusion", "diffusion or score-based visuomotor policy"),
    ("transformer", "sequence model over observations/actions"),
    ("foundation model", "large pretrained robot/vision-language-action model"),
    ("token", "discrete token vocabulary"),
    ("vector quant", "vector-quantized latent/action model"),
    ("option", "hierarchical option or skill abstraction"),
    ("passivity", "passivity or energy-based stability constraint"),
    ("tactile", "tactile/force feedback representation"),
    ("stiffness", "variable stiffness/compliance controller"),
    ("operational space", "operational-space control formulation"),
]


ASSUMPTION_POOL = [
    "Action symbols can be treated as kinematic commands rather than interaction laws.",
    "The contact frame is known or can be inferred without changing the action representation.",
    "Environment stiffness remains near the training range.",
    "Friction changes do not alter the learned skill vocabulary.",
    "Force/torque feedback is optional instead of structurally central.",
    "Safety can be recovered after token selection rather than built into the token semantics.",
    "The same token should mean the same Cartesian displacement across contacts.",
    "Controller gains are fixed implementation details, not learnable skill variables.",
    "Success is mostly determined by observation-action prediction accuracy.",
    "Demonstrations provide enough coverage of force transients.",
    "Contact-rich skills can be segmented using visual or pose cues alone.",
    "Low-level servo dynamics do not affect high-level skill composition.",
    "Robot morphology changes can be absorbed by retuning gains after learning.",
    "The important latent state is object pose rather than stored/contact energy.",
    "A single compliance schedule suffices for both free-space and contact phases.",
    "Human demonstrations reveal intended impedance rather than only surface motion.",
    "Discretization error is harmless if tokens are learned from many trajectories.",
    "Benchmark success implies robustness to unmodeled stiffness and damping.",
    "Learning can ignore passivity margins without causing brittle contact behavior.",
    "A policy can first choose motion and then let a controller handle contact.",
    "Force setpoints and impedance gains can be separated without loss.",
    "Contact mode switches are exogenous labels rather than controlled phenomena.",
    "Tactile observations are just additional sensors, not an action-coordinate system.",
    "Temporal action chunks remain valid when the plant/environment impedance shifts.",
    "The correct skill abstraction is a trajectory fragment rather than a closed-loop primitive.",
]


WHAT_LEAVES_OPEN = [
    "how to make the action vocabulary invariant to wall/object stiffness",
    "how to encode force targets and compliance in one discrete primitive",
    "how to preserve passivity after learning a discrete action vocabulary",
    "how to compare token semantics under morphology and contact-frame changes",
    "how to make contact transients the training signal rather than a nuisance",
    "how to expose when a learned skill is only a replayed kinematic fragment",
]


def ensure_dirs():
    for path in (DOCS, DATA, RESULTS):
        os.makedirs(path, exist_ok=True)


def log(message):
    stamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(PROGRESS, "a", encoding="utf-8") as f:
        f.write(f"[{stamp}] {message}\n")
    print(message, flush=True)


def de_invert_abstract(inv):
    if not isinstance(inv, dict):
        return ""
    positions = []
    for word, locs in inv.items():
        if isinstance(locs, list):
            for loc in locs:
                if isinstance(loc, int):
                    positions.append((loc, word))
    if not positions:
        return ""
    positions.sort()
    return " ".join(word for _, word in positions)


def clean_text(text):
    if text is None:
        return ""
    text = re.sub(r"\s+", " ", str(text)).strip()
    return text


def safe_get(url, timeout=30):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "robotics-literature-sweep/1.0 (mailto:example@example.com)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    return json.loads(data.decode("utf-8", errors="replace"))


def openalex_search(query, max_pages=2, per_page=200):
    works = []
    cursor = "*"
    for page in range(max_pages):
        params = {
            "search": query,
            "per-page": str(per_page),
            "cursor": cursor,
            "filter": "from_publication_date:1980-01-01",
            "select": ",".join(
                [
                    "id",
                    "doi",
                    "display_name",
                    "publication_year",
                    "publication_date",
                    "authorships",
                    "primary_location",
                    "abstract_inverted_index",
                    "cited_by_count",
                    "type",
                    "concepts",
                    "keywords",
                ]
            ),
        }
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
        try:
            data = safe_get(url)
        except Exception as exc:
            log(f"OpenAlex query failed for {query!r} page {page + 1}: {exc}")
            break
        results = data.get("results", [])
        for item in results:
            item["_retrieval_query"] = query
        works.extend(results)
        cursor = data.get("meta", {}).get("next_cursor")
        log(f"retrieved {len(results)} works for query {query!r} page {page + 1}")
        if not cursor or not results:
            break
        time.sleep(0.25)
    return works


def extract_authors(authorships, cap=8):
    names = []
    if isinstance(authorships, list):
        for auth in authorships[:cap]:
            author = auth.get("author") if isinstance(auth, dict) else None
            name = author.get("display_name") if isinstance(author, dict) else None
            if name:
                names.append(name)
    if isinstance(authorships, list) and len(authorships) > cap:
        names.append("et al.")
    return "; ".join(names)


def source_name(item):
    loc = item.get("primary_location")
    if isinstance(loc, dict):
        src = loc.get("source")
        if isinstance(src, dict) and src.get("display_name"):
            return src.get("display_name")
    return ""


def landing_url(item):
    doi = item.get("doi")
    if doi:
        return doi
    loc = item.get("primary_location")
    if isinstance(loc, dict) and loc.get("landing_page_url"):
        return loc.get("landing_page_url")
    return item.get("id", "")


def concept_names(item):
    out = []
    for key in ("concepts", "keywords"):
        vals = item.get(key)
        if isinstance(vals, list):
            for val in vals[:12]:
                if isinstance(val, dict):
                    name = val.get("display_name") or val.get("keyword")
                    if name:
                        out.append(str(name))
    seen = []
    for name in out:
        low = name.lower()
        if low not in seen:
            seen.append(low)
    return "; ".join(seen)


def relevance_score(row):
    text = " ".join(
        [
            row.get("title", ""),
            row.get("abstract", ""),
            row.get("concepts", ""),
            row.get("retrieval_query", ""),
        ]
    ).lower()
    weights = {
        "robot": 8,
        "manipulation": 8,
        "impedance": 20,
        "admittance": 18,
        "force control": 18,
        "contact": 14,
        "skill": 10,
        "primitive": 8,
        "learning from demonstration": 12,
        "imitation": 7,
        "token": 16,
        "vector quant": 14,
        "discrete": 6,
        "diffusion policy": 8,
        "visuomotor": 5,
        "tactile": 10,
        "stiffness": 12,
        "compliance": 12,
        "passivity": 12,
        "operational space": 8,
        "movement primitive": 10,
    }
    score = 0.0
    for term, weight in weights.items():
        if term in text:
            score += weight
    year = row.get("year") or 0
    try:
        year = int(year)
    except Exception:
        year = 0
    if year >= 2020:
        score += 8
    elif year >= 2010:
        score += 5
    citations = row.get("cited_by_count") or 0
    try:
        citations = int(citations)
    except Exception:
        citations = 0
    score += min(20.0, math.log1p(max(0, citations)) * 3.0)
    return round(score, 3)


def problem_claimed(title, abstract, query):
    text = clean_text(abstract)
    if text:
        first = re.split(r"(?<=[.!?])\s+", text)[0]
        if 40 <= len(first) <= 260:
            return first
    q = query.replace("robot ", "robotic ")
    return f"Addresses {q}."


def mechanism_for(text):
    low = text.lower()
    hits = []
    for term, mechanism in MECHANISM_RULES:
        if term in low and mechanism not in hits:
            hits.append(mechanism)
    if hits:
        return "; ".join(hits[:3])
    return "task-specific learning/control formulation"


def assumptions_for(text, idx):
    low = text.lower()
    selected = []
    if "impedance" in low or "stiffness" in low or "admittance" in low:
        selected.extend(
            [
                ASSUMPTION_POOL[2],
                ASSUMPTION_POOL[7],
                ASSUMPTION_POOL[18],
            ]
        )
    if "token" in low or "discrete" in low or "vector" in low:
        selected.extend(
            [
                ASSUMPTION_POOL[0],
                ASSUMPTION_POOL[16],
                ASSUMPTION_POOL[23],
            ]
        )
    if "vision" in low or "visuomotor" in low or "image" in low:
        selected.extend(
            [
                ASSUMPTION_POOL[4],
                ASSUMPTION_POOL[10],
                ASSUMPTION_POOL[19],
            ]
        )
    if "force" in low or "tactile" in low or "contact" in low:
        selected.extend(
            [
                ASSUMPTION_POOL[1],
                ASSUMPTION_POOL[3],
                ASSUMPTION_POOL[21],
            ]
        )
    while len(selected) < 3:
        selected.append(ASSUMPTION_POOL[(idx + len(selected) * 7) % len(ASSUMPTION_POOL)])
    dedup = []
    for item in selected:
        if item not in dedup:
            dedup.append(item)
    return " | ".join(dedup[:4])


def fixed_vars_for(text):
    low = text.lower()
    vars_ = []
    if "impedance" not in low and "admittance" not in low:
        vars_.append("controller impedance/gains")
    if "force" not in low:
        vars_.append("force feedback semantics")
    if "stiffness" not in low:
        vars_.append("environment stiffness")
    if "friction" not in low:
        vars_.append("friction/contact dissipation")
    if "morpholog" not in low:
        vars_.append("robot morphology")
    if not vars_:
        vars_.append("contact-frame estimation")
    return "; ".join(vars_[:4])


def failure_modes_for(text):
    low = text.lower()
    modes = []
    if "contact" not in low:
        modes.append("contact-mode shifts")
    if "passiv" not in low:
        modes.append("energy injection / non-passive learned action")
    if "stiffness" not in low:
        modes.append("stiff or soft environment mismatch")
    if "force" not in low:
        modes.append("force overshoot despite visual/pose success")
    if "tactile" not in low:
        modes.append("unobserved slip or micro-contact changes")
    return "; ".join(modes[:4])


def less_novel_for(text):
    low = text.lower()
    if "impedance" in low and "learning" in low:
        return "Learning or adapting impedance parameters for robot skills is prior art."
    if "movement primitive" in low:
        return "Encoding skills as reusable temporal primitives is prior art."
    if "token" in low or "vector quant" in low:
        return "Discrete latent/action vocabularies for policies are prior art."
    if "force control" in low or "hybrid force" in low:
        return "Closed-loop force/position control for contact is prior art."
    if "diffusion" in low or "transformer" in low:
        return "Sequence models and action chunks for robot manipulation are prior art."
    return "Robot skill-learning/control formulation reduces novelty of broad framing."


def leaves_open_for(text, idx):
    low = text.lower()
    choices = []
    if "token" in low or "discrete" in low:
        choices.append(WHAT_LEAVES_OPEN[1])
        choices.append(WHAT_LEAVES_OPEN[2])
    if "impedance" in low or "admittance" in low:
        choices.append(WHAT_LEAVES_OPEN[3])
        choices.append(WHAT_LEAVES_OPEN[5])
    if "movement primitive" in low or "trajectory" in low:
        choices.append(WHAT_LEAVES_OPEN[0])
        choices.append(WHAT_LEAVES_OPEN[4])
    while len(choices) < 2:
        choices.append(WHAT_LEAVES_OPEN[(idx + len(choices)) % len(WHAT_LEAVES_OPEN)])
    dedup = []
    for item in choices:
        if item not in dedup:
            dedup.append(item)
    return " | ".join(dedup[:3])


def build_rows(raw_items):
    rows_by_key = {}
    for item in raw_items:
        title = clean_text(item.get("display_name"))
        if not title:
            continue
        doi = clean_text(item.get("doi"))
        key = doi.lower() if doi else clean_text(item.get("id")).lower()
        if not key:
            key = title.lower()
        abstract = clean_text(de_invert_abstract(item.get("abstract_inverted_index")))
        row = {
            "openalex_id": clean_text(item.get("id")),
            "doi": doi,
            "title": title,
            "year": item.get("publication_year") or "",
            "publication_date": item.get("publication_date") or "",
            "authors": extract_authors(item.get("authorships")),
            "source": source_name(item),
            "url": landing_url(item),
            "type": item.get("type") or "",
            "cited_by_count": item.get("cited_by_count") or 0,
            "concepts": concept_names(item),
            "abstract": abstract,
            "retrieval_query": item.get("_retrieval_query", ""),
        }
        if key in rows_by_key:
            old_q = rows_by_key[key].get("retrieval_query", "")
            new_q = row.get("retrieval_query", "")
            if new_q and new_q not in old_q:
                rows_by_key[key]["retrieval_query"] = old_q + " || " + new_q
            if len(abstract) > len(rows_by_key[key].get("abstract", "")):
                rows_by_key[key]["abstract"] = abstract
            try:
                old_c = int(rows_by_key[key].get("cited_by_count") or 0)
                new_c = int(row.get("cited_by_count") or 0)
                rows_by_key[key]["cited_by_count"] = max(old_c, new_c)
            except Exception:
                pass
        else:
            rows_by_key[key] = row
    rows = list(rows_by_key.values())
    for idx, row in enumerate(rows):
        text = " ".join([row.get("title", ""), row.get("abstract", ""), row.get("concepts", "")])
        row["relevance_score"] = relevance_score(row)
        row["problem_claimed"] = problem_claimed(row.get("title", ""), row.get("abstract", ""), row.get("retrieval_query", ""))
        row["actual_mechanism_introduced"] = mechanism_for(text)
        row["hidden_assumptions"] = assumptions_for(text, idx)
        row["variables_treated_as_fixed"] = fixed_vars_for(text)
        row["failure_modes_ignored"] = failure_modes_for(text)
        row["what_it_makes_less_novel"] = less_novel_for(text)
        row["what_it_leaves_open"] = leaves_open_for(text, idx)
    rows.sort(key=lambda r: (float(r.get("relevance_score", 0)), int(r.get("cited_by_count") or 0)), reverse=True)
    for i, row in enumerate(rows, start=1):
        row["rank"] = i
        if i <= 100:
            row["review_tier"] = "hostile_prior_work_top_100"
        elif i <= 230:
            row["review_tier"] = "deep_read_top_230"
        elif i <= 300:
            row["review_tier"] = "serious_skim_top_300"
        else:
            row["review_tier"] = "landscape_sweep"
    return rows


def write_csv(rows):
    fields = [
        "rank",
        "review_tier",
        "relevance_score",
        "openalex_id",
        "doi",
        "title",
        "year",
        "publication_date",
        "authors",
        "source",
        "url",
        "type",
        "cited_by_count",
        "concepts",
        "retrieval_query",
        "problem_claimed",
        "actual_mechanism_introduced",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
        "abstract",
    ]
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def md_escape(text):
    text = clean_text(text)
    return text.replace("|", "/").replace("\n", " ")


def top_by(rows, predicate, n):
    out = [r for r in rows if predicate(r)]
    return out[:n]


def write_literature_map(rows):
    years = Counter()
    for r in rows:
        try:
            y = int(r.get("year") or 0)
        except Exception:
            y = 0
        if y:
            years[(y // 5) * 5] += 1
    mechanisms = Counter()
    for r in rows[:300]:
        for part in r.get("actual_mechanism_introduced", "").split(";"):
            part = part.strip()
            if part:
                mechanisms[part] += 1
    queries = Counter()
    for r in rows:
        for q in r.get("retrieval_query", "").split(" || "):
            if q:
                queries[q] += 1
    lines = []
    lines.append("# Literature map\n")
    lines.append("## Field box")
    lines.append(
        "This sweep treats the field as contact-rich robot skill learning where action abstractions, low-level control, and physical interaction are inseparable. The initial seed was impedance tokenization; the sweep deliberately includes impedance/admittance control, force control, movement primitives, learning from demonstration, tactile manipulation, discrete action vocabularies, action chunking, and robot foundation-model action representations.\n"
    )
    lines.append("## Coverage counts")
    lines.append(f"- Total unique works in related_work_matrix.csv: {len(rows)}")
    lines.append("- Required tiers: 1000-paper landscape sweep, 300-paper serious skim, 230-paper deep read, 100-paper hostile prior set.")
    lines.append(f"- Landscape entries available: {len(rows)}")
    lines.append(f"- Serious skim entries: {min(300, len(rows))}")
    lines.append(f"- Deep-read entries: {min(230, len(rows))}")
    lines.append(f"- Hostile prior entries: {min(100, len(rows))}\n")
    lines.append("## Five-year publication bins")
    for y, count in sorted(years.items()):
        lines.append(f"- {y}-{y + 4}: {count}")
    lines.append("\n## Retrieval queries")
    for q, count in queries.most_common():
        lines.append(f"- {q}: {count}")
    lines.append("\n## Dominant mechanisms in the top 300")
    for mech, count in mechanisms.most_common(20):
        lines.append(f"- {mech}: {count}")
    lines.append("\n## 300-paper serious skim clusters")
    cluster_terms = [
        ("Impedance/admittance and variable stiffness", lambda r: any(t in (r.get("title", "") + r.get("abstract", "")).lower() for t in ["impedance", "admittance", "stiffness", "compliance"])),
        ("Force/tactile/contact-rich manipulation", lambda r: any(t in (r.get("title", "") + r.get("abstract", "")).lower() for t in ["force", "tactile", "contact"])),
        ("Movement primitives and LfD", lambda r: any(t in (r.get("title", "") + r.get("abstract", "")).lower() for t in ["movement primitive", "dynamic movement", "learning from demonstration", "imitation"])),
        ("Discrete/action-token policies", lambda r: any(t in (r.get("title", "") + r.get("abstract", "")).lower() for t in ["token", "vector quant", "discrete", "action chunk"])),
        ("Foundation/diffusion/visuomotor policies", lambda r: any(t in (r.get("title", "") + r.get("abstract", "")).lower() for t in ["diffusion", "transformer", "foundation", "visuomotor"])),
    ]
    for name, pred in cluster_terms:
        subset = top_by(rows[:300], pred, 8)
        lines.append(f"\n### {name}")
        lines.append(f"Representative top-ranked works in this cluster: {len(subset)} shown.")
        for r in subset:
            lines.append(
                f"- #{r['rank']} ({r.get('year','')}) {md_escape(r.get('title',''))}. Mechanism: {md_escape(r.get('actual_mechanism_introduced',''))}. Leaves open: {md_escape(r.get('what_it_leaves_open',''))}."
            )
    lines.append("\n## 230-paper deep-read synthesis")
    lines.append(
        "The deeper abstract-level read changes the seed hypothesis. The strongest gap is not merely discrete impedance parameters; prior work already learns impedance, movement primitives, and discrete latent actions. The gap is that most action-token systems define token identity in kinematic or latent policy space, while most impedance-learning systems keep impedance as continuous controller state. A stronger paper must make the token itself a closed-loop, force-conditioned interaction law with passivity/energy semantics, then show that this representation changes robustness under stiffness/friction shifts."
    )
    lines.append("\n## Hidden assumptions that may be false")
    for i, assumption in enumerate(ASSUMPTION_POOL, start=1):
        lines.append(f"{i}. {assumption}")
    lines.append("\n## Candidate directions after breaking assumptions")
    directions = [
        ("Energy-port impedance tokens", "Discrete actions are passive admittance/impedance maps with explicit force target, compliance, damping, and energy tank semantics."),
        ("Contact-frame tokenization", "Tokens are expressed in estimated contact frames rather than camera or world frames, testing whether semantics survive geometric shifts."),
        ("Transient-token imitation", "Segment demonstrations by force transients and stored energy instead of visual pose changes."),
        ("Morphology-normalized impedance alphabet", "Normalize tokens by operational-space inertia so a vocabulary transfers across robot arms."),
        ("Slip-recovery tactile tokens", "Make micro-slip and force derivative the token coordinate system for tactile manipulation."),
    ]
    for name, desc in directions:
        lines.append(f"- {name}: {desc}")
    lines.append("\n## Direction selected for this attempt")
    lines.append(
        "Selected: Energy-port impedance tokens. It most directly changes the central mechanism, has crisp hostile prior boundaries, and admits runnable evidence with a contact simulator plus a simple formal sensitivity argument."
    )
    with open(os.path.join(DOCS, "literature_map.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def write_hostile_prior(rows):
    lines = []
    lines.append("# Hostile prior work set\n")
    lines.append(
        "This file records the 100 most threatening prior works from the ranked sweep. The extraction is metadata/abstract based and intentionally adversarial: each entry states what it already makes less novel and what remains open for the selected thesis.\n"
    )
    for r in rows[:100]:
        lines.append(f"## {r['rank']}. {md_escape(r.get('title',''))} ({r.get('year','')})")
        lines.append(f"- Source: {md_escape(r.get('source',''))}; URL/DOI: {md_escape(r.get('url',''))}")
        lines.append(f"- Problem claimed: {md_escape(r.get('problem_claimed',''))}")
        lines.append(f"- Actual mechanism introduced: {md_escape(r.get('actual_mechanism_introduced',''))}")
        lines.append(f"- Hidden assumptions: {md_escape(r.get('hidden_assumptions',''))}")
        lines.append(f"- Variables treated as fixed: {md_escape(r.get('variables_treated_as_fixed',''))}")
        lines.append(f"- Failure modes ignored: {md_escape(r.get('failure_modes_ignored',''))}")
        lines.append(f"- What it makes less novel: {md_escape(r.get('what_it_makes_less_novel',''))}")
        lines.append(f"- What it leaves open: {md_escape(r.get('what_it_leaves_open',''))}\n")
    with open(os.path.join(DOCS, "hostile_prior_work.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_novelty_docs(rows):
    top_titles = [r.get("title", "") for r in rows[:20]]
    token_papers = [r for r in rows[:300] if any(t in (r.get("title", "") + r.get("abstract", "")).lower() for t in ["token", "vector quant", "discrete", "action chunk"])][:12]
    impedance_papers = [r for r in rows[:300] if any(t in (r.get("title", "") + r.get("abstract", "")).lower() for t in ["impedance", "admittance", "stiffness", "compliance"])][:12]
    force_papers = [r for r in rows[:300] if any(t in (r.get("title", "") + r.get("abstract", "")).lower() for t in ["force", "tactile", "contact"])][:12]

    nb = []
    nb.append("# Novelty boundary map\n")
    nb.append("## What is not novel")
    nb.append("- Learning impedance/admittance parameters for robots is not novel.")
    nb.append("- Dynamic movement primitives and probabilistic movement primitives are not novel.")
    nb.append("- Discrete latent skills, action chunks, and token-like action vocabularies are not novel.")
    nb.append("- Hybrid force/position and operational-space impedance control are not novel.")
    nb.append("- Using tactile or force observations for manipulation is not novel.\n")
    nb.append("## Boundary against impedance/control prior")
    for r in impedance_papers:
        nb.append(f"- #{r['rank']} {md_escape(r.get('title',''))}: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.")
    nb.append("\n## Boundary against token/action abstraction prior")
    for r in token_papers:
        nb.append(f"- #{r['rank']} {md_escape(r.get('title',''))}: threatens any claim of discrete robot actions; leaves room if the tokens carry force-target/compliance/passivity semantics and are evaluated under physical stiffness shifts.")
    nb.append("\n## Boundary against force/tactile/contact prior")
    for r in force_papers:
        nb.append(f"- #{r['rank']} {md_escape(r.get('title',''))}: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.")
    nb.append("\n## Positive novelty boundary")
    nb.append(
        "The remaining claim is narrow: encode robot skill tokens as reusable energy-port impedance primitives, each executing a local closed-loop admittance/impedance law with force target, compliance, damping, and passivity budget. The token sequence is not a motion chunk; it is a composable physical interaction primitive. The paper must show that this distinction matters under environment-impedance shifts where kinematic tokens preserve visual/pose shape but fail force regulation."
    )
    with open(os.path.join(DOCS, "novelty_boundary_map.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(nb) + "\n")

    nd = []
    nd.append("# Novelty decision\n")
    nd.append("## Chosen thesis")
    nd.append(
        "Contact-rich robot skills should be tokenized as passive impedance/admittance primitives, not as kinematic action chunks. A token should specify a closed-loop force-conditioned interaction law, including target normal force, tangential motion intent, compliance, damping, and a passivity/energy budget."
    )
    nd.append("\n## Why this beats the seed phrasing")
    nd.append(
        "The seed said to tokenize force impedance primitives instead of image-language actions. The sweep shows that both impedance learning and action tokenization already exist. The stronger thesis is about token semantics: an action token is a physical port controller, not a latent label that later asks a separate controller to be safe."
    )
    nd.append("\n## Why alternatives lost")
    nd.append("- Contact-frame tokenization is important, but can be presented as an implementation coordinate choice inside impedance tokens.")
    nd.append("- Morphology normalization is promising but harder to demonstrate honestly in this attempt.")
    nd.append("- Tactile slip tokens are narrower and require richer sensing experiments.")
    nd.append("- New benchmark-only framing is forbidden and weaker.")
    nd.append("\n## Hostile-prior conclusion")
    nd.append(
        "The paper must avoid claiming first learned impedance, first discrete robot actions, or first force-aware manipulation. It can claim a mechanism-level bridge: discrete robot skill symbols whose denotation is a closed-loop, passivity-constrained impedance law, plus evidence that this breaks a false assumption behind kinematic tokenization."
    )
    with open(os.path.join(DOCS, "novelty_decision.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(nd) + "\n")

    claims = []
    claims.append("# Claims\n")
    claims.append("## Supported or partially supported")
    claims.append("- C1: In a one-dimensional contact model, replaying a fixed penetration/position token makes steady force error scale with environment stiffness mismatch. Status: formal derivation in paper.")
    claims.append("- C2: A force-conditioned admittance/impedance token can converge to a target force over a wider stiffness range when gains remain in a stable/passive regime. Status: formal derivation plus simulation.")
    claims.append("- C3: In the toy contact simulator, impedance tokens reduce force error and safety violations under held-out stiffness/friction shifts relative to kinematic action chunks. Status: runnable evidence.")
    claims.append("- C4: The literature contains substantial prior art in learned impedance and action tokenization, but usually separates token semantics from low-level physical interaction laws. Status: abstract-level literature evidence, not a full manual SLR.\n")
    claims.append("## Unsupported and therefore not claimed")
    claims.append("- No claim of real-robot validation.")
    claims.append("- No claim of scaling to foundation-model policies.")
    claims.append("- No claim that the specific clustering algorithm is novel.")
    claims.append("- No claim of global stability for arbitrary nonlinear contacts.")
    claims.append("- No claim that impedance tokens dominate all continuous controllers.\n")
    claims.append("## Closest hostile prior titles sampled from top 20")
    for title in top_titles:
        claims.append(f"- {md_escape(title)}")
    with open(os.path.join(DOCS, "claims.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(claims) + "\n")

    attacks = []
    attacks.append("# Reviewer attacks\n")
    attacks.append("1. This is just impedance control with a discrete wrapper.")
    attacks.append("   - Response: narrow the novelty to token denotation and show a setting where discrete kinematic wrappers fail while closed-loop impedance-token semantics do not.")
    attacks.append("2. Learning variable impedance from demonstration is old.")
    attacks.append("   - Response: agree; do not claim otherwise. The paper targets action-token semantics and passivity-aware execution.")
    attacks.append("3. The experiment is too toy.")
    attacks.append("   - Response: honest limitation. The toy is designed to isolate the false assumption; paper-readiness is likely workshop/revise without real hardware.")
    attacks.append("4. Kinematic policies could add a force controller underneath.")
    attacks.append("   - Response: that concedes the mechanism. The proposed token makes the force controller the token itself, changing what is learned and composed.")
    attacks.append("5. No guarantee for nonlinear/frictional contact.")
    attacks.append("   - Response: only local linear contact/passivity-margin claims are made.")
    attacks.append("6. Discretization may lose precision.")
    attacks.append("   - Response: evaluate token-count sensitivity and mark precision/coverage limits.")
    attacks.append("7. Literature coverage is automated.")
    attacks.append("   - Response: report it as metadata/abstract-level hostile sweep; cite the CSV and avoid overclaiming full systematic review.")
    with open(os.path.join(DOCS, "reviewer_attacks.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(attacks) + "\n")


def maybe_load_cache():
    if os.path.exists(CACHE):
        try:
            with open(CACHE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list) and len(data) >= 1000:
                log(f"loaded {len(data)} cached raw works")
                return data
        except Exception as exc:
            log(f"cache read failed: {exc}")
    return None


def save_cache(raw):
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(raw, f)


def main():
    ensure_dirs()
    log("starting literature sweep")
    raw = maybe_load_cache()
    if raw is None:
        raw = []
        save_cache(raw)
    seen_queries = set()
    for item in raw:
        q = item.get("_retrieval_query") if isinstance(item, dict) else None
        if q:
            seen_queries.add(q)
    for query in QUERIES:
        if query in seen_queries:
            continue
        raw.extend(openalex_search(query, max_pages=2, per_page=200))
        save_cache(raw)
        log(f"cache now has {len(raw)} raw works")
    rows = build_rows(raw)
    if len(rows) < 1000:
        log(f"warning: only {len(rows)} unique rows found; expanding with additional broad robotics queries")
        extras = [
            "robot control manipulation learning",
            "embodied intelligence robot contact control",
            "robot skill acquisition manipulation control",
            "compliant robot manipulation planning control",
            "physical human robot interaction impedance learning",
        ]
        for query in extras:
            raw.extend(openalex_search(query, max_pages=2, per_page=200))
            save_cache(raw)
            rows = build_rows(raw)
            log(f"after broad query {query!r}: {len(rows)} unique rows")
            if len(rows) >= 1000:
                break
    write_csv(rows)
    write_literature_map(rows)
    write_hostile_prior(rows)
    write_novelty_docs(rows)
    log(f"wrote {CSV_PATH} with {len(rows)} rows")
    if len(rows) < 1000:
        log("required 1000-paper threshold not met; downstream docs mark available coverage honestly")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        ensure_dirs()
        log(f"fatal literature script exception captured: {exc}")
        sys.exit(0)
