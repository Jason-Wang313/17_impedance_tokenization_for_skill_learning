# Impedance Tokenization for Skill Learning

This repository contains the artifacts for an anonymous ICLR-style robotics paper:

**Impedance Tokenization for Skill Learning**

The central thesis is that contact-rich robot skills should be tokenized as passive impedance/admittance primitives, not as kinematic action chunks. A token denotes a closed-loop physical interaction law with force target, compliance/admittance, damping, tangential intent, contact frame, and a bounded positive-work budget.

## Contents

- `paper/main.tex`: ICLR 2026-style manuscript.
- `paper/main.pdf`: compiled paper.
- `docs/related_work_matrix.csv`: 5,512-paper landscape sweep with review tiers.
- `docs/literature_map.md`: field-box and cluster summary.
- `docs/hostile_prior_work.md`: 100-paper hostile prior-work set.
- `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, `docs/reviewer_attacks.md`, `docs/final_audit.md`: adversarial novelty and readiness artifacts.
- `scripts/build_literature.py`: OpenAlex-backed literature builder.
- `scripts/run_impedance_token_experiment.py`: contact-wiping simulator and plot generator.
- `scripts/validate_artifacts.py`: artifact-count validator.
- `results/`: experiment metrics and aggregate tables.
- `figures/`: generated plots used in the paper.

## Reproduce Evidence

Install the small Python dependency set:

```powershell
python -m pip install -r requirements.txt
```

Regenerate the literature artifacts from the local cache when present, or from OpenAlex when network access is available:

```powershell
python scripts\build_literature.py
```

Regenerate the simulator results and figures:

```powershell
python scripts\run_impedance_token_experiment.py
```

Validate the required artifact counts:

```powershell
python scripts\validate_artifacts.py
```

Expected validator summary:

- 5,512 related-work rows.
- 100 hostile prior-work entries.
- 230 deep/hostile entries.
- 300 skim/deep/hostile entries.
- 2,304 experiment runs.

## Build Paper

The paper uses the official ICLR 2026 LaTeX template cached under `paper/`.

```powershell
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The required batch output PDF was copied to:

```text
C:\Users\wangz\Downloads\17.pdf
```

## Honest Scope

This is not a real-robot validation. The strongest evidence is a formal one-dimensional contact check plus a 2,304-case toy contact-wiping simulator. The paper intentionally avoids claiming first learned impedance, first discrete robot action tokens, or global nonlinear passivity.

## Submission-Hardening v2

- Added token-parameter stress in `results/token_parameter_stress.csv`.
- Baseline impedance token: mean absolute force error 1.629 N, safety violation 0.000, contact loss 0.019.
- 0.25x admittance token: force error 4.223 N and contact loss 0.276.
- 0.05 J work-budget token: force error 3.968 N and contact loss 0.140.
- Decision remains workshop-only until demonstrated with learned token libraries, hardware contact, and stronger continuous-controller baselines.
