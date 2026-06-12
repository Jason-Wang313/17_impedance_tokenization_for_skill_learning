# Experiment summary

Grid: 3 methods x 8 stiffness values x 4 friction values x 3 surface offsets x 8 seeds = 2304 runs.

| method | mean abs force error | safety violation rate | contact loss rate | tangential distance |
|---|---:|---:|---:|---:|
| gain_schedule | 8.422 | 0.250 | 0.000 | 0.267 |
| impedance_token | 1.629 | 0.000 | 0.019 | 0.319 |
| kinematic_chunk | 9.148 | 0.310 | 0.000 | 0.271 |

Interpretation: lower force error, safety violation, and contact loss are better; higher tangential distance is better when force remains near target.

## V2 token-parameter stress

The hardening stress reruns the impedance-token method while perturbing the token's admittance scale or positive-work budget.

| token variant | mean abs force error | safety violation rate | contact loss rate | tangential distance |
|---|---:|---:|---:|---:|
| baseline | 1.629 | 0.000 | 0.019 | 0.319 |
| low_admittance_0p25 | 4.223 | 0.000 | 0.276 | 0.189 |
| low_admittance_0p50 | 2.837 | 0.000 | 0.093 | 0.258 |
| high_admittance_2x | 0.784 | 0.000 | 0.000 | 0.362 |
| high_admittance_4x | 0.337 | 0.000 | 0.000 | 0.385 |
| very_tight_energy_0p05 | 3.968 | 0.000 | 0.140 | 0.202 |
| tight_energy_0p15 | 2.307 | 0.000 | 0.019 | 0.285 |
| tight_energy_0p5 | 1.629 | 0.000 | 0.019 | 0.319 |

Interpretation: impedance tokenization is not calibration-free. If the discrete token set lacks the right admittance or work budget, the advantage narrows or fails.
