# Submission Attack Log

Checked: 2026-06-13 00:45:33 +01:00

## Hostile Round 1: Discretization may lose physical precision

Result: Recoverable.

Action: Added token-parameter stress for admittance scale and work budget. The baseline impedance token has force error 1.629 N and contact loss 0.019; 0.25x admittance raises these to 4.223 N and 0.276.

## Hostile Round 2: Energy budget coverage may be too tight

Result: Recoverable.

Action: Added work-budget stress. A 0.05 J budget raises force error to 3.968 N and contact loss to 0.140, showing the token library must cover the physical work needed by the contact.

## Hostile Round 3: The paper sounds like arbitrary impedance tokens work

Result: Claim narrowed.

Action: Manuscript, claims, reviewer attacks, and final audit now say the supported claim is about token semantics with adequate physical parameter coverage, not arbitrary token dictionaries.
