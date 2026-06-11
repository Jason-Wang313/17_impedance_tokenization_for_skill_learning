# Novelty decision

## Chosen thesis
Contact-rich robot skills should be tokenized as passive impedance/admittance primitives, not as kinematic action chunks. A token should specify a closed-loop force-conditioned interaction law, including target normal force, tangential motion intent, compliance, damping, and a passivity/energy budget.

## Why this beats the seed phrasing
The seed said to tokenize force impedance primitives instead of image-language actions. The sweep shows that both impedance learning and action tokenization already exist. The stronger thesis is about token semantics: an action token is a physical port controller, not a latent label that later asks a separate controller to be safe.

## Why alternatives lost
- Contact-frame tokenization is important, but can be presented as an implementation coordinate choice inside impedance tokens.
- Morphology normalization is promising but harder to demonstrate honestly in this attempt.
- Tactile slip tokens are narrower and require richer sensing experiments.
- New benchmark-only framing is forbidden and weaker.

## Hostile-prior conclusion
The paper must avoid claiming first learned impedance, first discrete robot actions, or first force-aware manipulation. It can claim a mechanism-level bridge: discrete robot skill symbols whose denotation is a closed-loop, passivity-constrained impedance law, plus evidence that this breaks a false assumption behind kinematic tokenization.
