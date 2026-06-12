# Experiment Rigor Checklist

- Main grid: 3 methods x 8 stiffness values x 4 friction values x 3 offsets x 8 seeds = 2,304 runs.
- V2 stress grid: 8 impedance-token variants x 8 stiffness values x 4 friction values x 3 offsets x 8 seeds = 6,144 runs.
- Main raw output: `results/experiment_metrics.csv`.
- Main aggregate output: `results/aggregate_by_stiffness.csv`.
- V2 stress output: `results/token_parameter_stress.csv`.
- Manuscript tables: `results/experiment_table.tex`, `results/token_parameter_table.tex`.
- Baselines: kinematic chunks, gain schedule, impedance token, and stressed impedance-token variants.
- Remaining empirical gap: no hardware, no learned token dictionary, no high-dimensional contact geometry, no modern continuous-controller baseline.
