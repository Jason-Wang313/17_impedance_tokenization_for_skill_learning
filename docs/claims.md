# Claims

## Supported or partially supported
- C1: In a one-dimensional contact model, replaying a fixed penetration/position token makes steady force error scale with environment stiffness mismatch. Status: formal derivation in paper.
- C2: A force-conditioned admittance/impedance token can converge to a target force over a wider stiffness range when gains remain in a stable/passive regime. Status: formal derivation plus simulation.
- C3: In the toy contact simulator, impedance tokens reduce force error and safety violations under held-out stiffness/friction shifts relative to kinematic action chunks. Status: runnable evidence.
- C4: The literature contains substantial prior art in learned impedance and action tokenization, but usually separates token semantics from low-level physical interaction laws. Status: abstract-level literature evidence, not a full manual SLR.
- C5: V2 token-parameter stress shows the mechanism depends on token-library coverage: 0.25x admittance raises force error to 4.223 N and contact loss to 0.276, while a 0.05 J work budget raises force error to 3.968 N and contact loss to 0.140. Status: runnable stress evidence.

## Unsupported and therefore not claimed
- No claim of real-robot validation.
- No claim of scaling to foundation-model policies.
- No claim that the specific clustering algorithm is novel.
- No claim of global stability for arbitrary nonlinear contacts.
- No claim that impedance tokens dominate all continuous controllers.
- No claim that arbitrary impedance-token dictionaries are sufficient; admittance and work-budget coverage are required.

## Closest hostile prior titles sampled from top 20
- Proactive human–robot collaboration: Mutual-cognitive, predictable, and self-organising perspectives
- A survey of robot manipulation in contact
- Variable Impedance Control and Learning—A Review
- Human–robot collaboration in industrial environments: A literature review on non-destructive disassembly
- A review on interaction control for contact robots through intent detection
- Dynamic movement primitives in robotics: A tutorial survey
- Efficient Force Control Learning System for Industrial Robots Based on Variable Impedance Control
- Progress and prospects of the human–robot collaboration
- Past, Present, and Future of Aerial Robotic Manipulators
- Survey on human–robot collaboration in industrial settings: Safety, intuitive interfaces and applications
- A review on reinforcement learning for contact-rich robotic manipulation tasks
- Variable impedance control on contact-rich manipulation of a collaborative industrial mobile manipulator: An imitation learning approach
- Robot Learning from Demonstration in Robotic Assembly: A Survey
- Robotic disassembly of electric vehicle batteries: Technologies and opportunities
- A Survey on Imitation Learning for Contact-Rich Tasks in Robotics
- Data-Efficient Reinforcement Learning for Variable Impedance Control
- A Review of Intent Detection, Arbitration, and Communication Aspects of Shared Control for Physical Human–Robot Interaction
- Challenges and solutions for application and wider adoption of wearable robots
- Haptics in Robot-Assisted Surgery: Challenges and Benefits
- A User Study on Kinesthetic Teaching of Redundant Robots in Task and Configuration Space
