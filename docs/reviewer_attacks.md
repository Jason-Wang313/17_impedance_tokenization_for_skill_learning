# Reviewer attacks

1. This is just impedance control with a discrete wrapper.
   - Response: narrow the novelty to token denotation and show a setting where discrete kinematic wrappers fail while closed-loop impedance-token semantics do not.
2. Learning variable impedance from demonstration is old.
   - Response: agree; do not claim otherwise. The paper targets action-token semantics and passivity-aware execution.
3. The experiment is too toy.
   - Response: honest limitation. The toy is designed to isolate the false assumption; paper-readiness is likely workshop/revise without real hardware.
4. Kinematic policies could add a force controller underneath.
   - Response: that concedes the mechanism. The proposed token makes the force controller the token itself, changing what is learned and composed.
5. No guarantee for nonlinear/frictional contact.
   - Response: only local linear contact/passivity-margin claims are made.
6. Discretization may lose precision.
   - Response: evaluate token-count sensitivity and mark precision/coverage limits.
7. Literature coverage is automated.
   - Response: report it as metadata/abstract-level hostile sweep; cite the CSV and avoid overclaiming full systematic review.

## V2 token-library stress

The hardening pass adds a token-parameter stress. The baseline impedance token has mean force error 1.629 N and contact loss 0.019. Reducing admittance to 0.25x raises force error to 4.223 N and contact loss to 0.276. A very tight 0.05 J work budget raises force error to 3.968 N and contact loss to 0.140. The rebuttal to discretization concerns is therefore honest: token semantics help, but the vocabulary still needs adequate physical parameter coverage.
