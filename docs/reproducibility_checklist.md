# Reproducibility Checklist

Run from the repository root:

```powershell
python scripts\run_impedance_token_experiment.py
```

Expected artifacts:

- `results/experiment_metrics.csv`
- `results/aggregate_by_stiffness.csv`
- `results/experiment_table.tex`
- `results/experiment_summary.md`
- `results/token_parameter_stress.csv`
- `results/token_parameter_table.tex`
- `figures/force_error_by_stiffness.pdf`
- `figures/force_error_by_stiffness.png`
- `figures/safety_by_stiffness.pdf`
- `figures/safety_by_stiffness.png`

Artifact-count validation remains available via:

```powershell
python scripts\validate_artifacts.py
```
