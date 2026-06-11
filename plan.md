# Plan

## Objective
Produce a complete robotics/embodied-intelligence research paper for paper 17, starting from the seed "Impedance Tokenization for Skill Learning" but allowing the final thesis to change if the literature sweep shows a stronger direction.

## Required Outputs
- `docs/related_work_matrix.csv` with at least 1000 entries.
- `docs/literature_map.md`.
- `docs/hostile_prior_work.md`.
- `docs/novelty_boundary_map.md`.
- `docs/novelty_decision.md`.
- `docs/claims.md`.
- `docs/reviewer_attacks.md`.
- `docs/final_audit.md`.
- Complete anonymous ICLR-style LaTeX paper.
- Runnable code/evidence artifacts.
- Final compiled PDF at `C:/Users/wangz/Downloads/17.pdf`.
- Public GitHub repo named `17_impedance_tokenization_for_skill_learning`, pushed if credentials permit.

## Execution Stages
1. Initialize compact run status and inspect/reuse any existing artifacts.
2. Build a robotics skill-learning/control literature corpus:
   - 1000-paper landscape sweep.
   - 300-paper serious skim.
   - 200-250-paper deep read.
   - 100-paper hostile prior-work set.
3. Extract for important prior work:
   - claimed problem,
   - introduced mechanism,
   - hidden assumptions,
   - fixed variables,
   - ignored failure modes,
   - what it makes less novel,
   - what it leaves open.
4. Define the field box, enumerate at least 20 possibly false assumptions, generate candidate paper directions, and choose one only after adversarial novelty analysis.
5. Implement a runnable evidence package with synthetic but physically grounded robot skill-learning/control experiments.
6. Write ICLR-style paper with honest claims and limitations.
7. Compile using direct `pdflatex`/`bibtex` with explicit timeouts; repair LaTeX/BibTeX issues if needed.
8. Copy final PDF exactly to `C:/Users/wangz/Downloads/17.pdf`.
9. Create/push the public GitHub repository if `git`/`gh` authentication allow it; otherwise document the exact blocker.
10. Complete `docs/final_audit.md` with the required twelve audit answers plus desktop-copy status.

## Safety Notes
- Use short, safe probes and explicit timeouts.
- Avoid uncaught nonzero exits in diagnostic scripts.
- Prefer resumable scripts and cached artifacts.
- Do not delete useful existing artifacts unless they are demonstrably invalid.
