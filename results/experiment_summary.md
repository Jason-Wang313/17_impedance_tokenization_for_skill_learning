# Experiment summary

Grid: 3 methods x 8 stiffness values x 4 friction values x 3 surface offsets x 8 seeds = 2304 runs.

| method | mean abs force error | safety violation rate | contact loss rate | tangential distance |
|---|---:|---:|---:|---:|
| gain_schedule | 8.422 | 0.250 | 0.000 | 0.267 |
| impedance_token | 1.629 | 0.000 | 0.019 | 0.319 |
| kinematic_chunk | 9.148 | 0.310 | 0.000 | 0.271 |

Interpretation: lower force error, safety violation, and contact loss are better; higher tangential distance is better when force remains near target.
