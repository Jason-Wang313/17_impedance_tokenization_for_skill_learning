import csv
import os
from collections import Counter


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


REQUIRED_DOCS = [
    "docs/related_work_matrix.csv",
    "docs/literature_map.md",
    "docs/hostile_prior_work.md",
    "docs/novelty_boundary_map.md",
    "docs/novelty_decision.md",
    "docs/claims.md",
    "docs/reviewer_attacks.md",
]


def rel(path):
    return os.path.join(ROOT, path)


def main():
    failures = []
    for path in REQUIRED_DOCS:
        if not os.path.exists(rel(path)):
            failures.append(f"missing {path}")

    matrix_path = rel("docs/related_work_matrix.csv")
    rows = []
    if os.path.exists(matrix_path):
        with open(matrix_path, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        tiers = Counter(row.get("review_tier", "") for row in rows)
        print(f"related_work_rows={len(rows)}")
        print(f"tier_counts={dict(tiers)}")
        if len(rows) < 1000:
            failures.append("related work matrix has fewer than 1000 rows")
        if tiers.get("serious_skim_top_300", 0) + tiers.get("deep_read_top_230", 0) + tiers.get("hostile_prior_work_top_100", 0) < 300:
            failures.append("serious skim/deep tiers do not cover at least 300 entries")
        if tiers.get("deep_read_top_230", 0) + tiers.get("hostile_prior_work_top_100", 0) < 200:
            failures.append("deep read tier does not cover at least 200 entries")
        if tiers.get("hostile_prior_work_top_100", 0) < 100:
            failures.append("hostile prior tier has fewer than 100 entries")

    metrics_path = rel("results/experiment_metrics.csv")
    if os.path.exists(metrics_path):
        with open(metrics_path, newline="", encoding="utf-8") as f:
            metrics = list(csv.DictReader(f))
        print(f"experiment_metric_rows={len(metrics)}")
        if len(metrics) != 2304:
            failures.append("experiment_metrics.csv should have 2304 rows")
    else:
        failures.append("missing results/experiment_metrics.csv")

    for path in [
        "results/aggregate_by_stiffness.csv",
        "results/experiment_table.tex",
        "results/experiment_summary.md",
        "figures/force_error_by_stiffness.pdf",
        "figures/safety_by_stiffness.pdf",
    ]:
        if not os.path.exists(rel(path)):
            failures.append(f"missing {path}")

    if failures:
        print("VALIDATION_FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("VALIDATION_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
