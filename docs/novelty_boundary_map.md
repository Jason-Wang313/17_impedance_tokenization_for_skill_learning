# Novelty boundary map

## What is not novel
- Learning impedance/admittance parameters for robots is not novel.
- Dynamic movement primitives and probabilistic movement primitives are not novel.
- Discrete latent skills, action chunks, and token-like action vocabularies are not novel.
- Hybrid force/position and operational-space impedance control are not novel.
- Using tactile or force observations for manipulation is not novel.

## Boundary against impedance/control prior
- #3 Variable Impedance Control and Learning—A Review: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #7 Efficient Force Control Learning System for Industrial Robots Based on Variable Impedance Control: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #12 Variable impedance control on contact-rich manipulation of a collaborative industrial mobile manipulator: An imitation learning approach: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #16 Data-Efficient Reinforcement Learning for Variable Impedance Control: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #26 Geometric Reinforcement Learning for Robotic Manipulation: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #38 Embodied Communication: How Robots and People Communicate Through Physical Interaction: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #39 Assisting Operators in Heavy Industrial Tasks: On the Design of an Optimized Cooperative Impedance Fuzzy-Controller With Embedded Safety Rules: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #41 Pneumatic Soft Robots: Challenges and Benefits: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #42 Learning Deep Robotic Skills on Riemannian Manifolds: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #43 Robot learning from demonstration of force-based manipulation tasks: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #45 Learning periodic skills for robotic manipulation: Insights on orientation and impedance: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.
- #56 Haptics Electromyography Perception and Learning Enhanced Intelligence for Teleoperated Robot: threatens any claim of learned impedance; leaves room only if token identity is the closed-loop interaction law, not just a gain schedule.

## Boundary against token/action abstraction prior
- #34 Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware: threatens any claim of discrete robot actions; leaves room if the tokens carry force-target/compliance/passivity semantics and are evaluated under physical stiffness shifts.
- #50 Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation: threatens any claim of discrete robot actions; leaves room if the tokens carry force-target/compliance/passivity semantics and are evaluated under physical stiffness shifts.
- #61 Modeling robot discrete movements with state-varying stiffness and damping: A framework for integrated motion generation and impedance control: threatens any claim of discrete robot actions; leaves room if the tokens carry force-target/compliance/passivity semantics and are evaluated under physical stiffness shifts.
- #151 Model Predictive Control with Gaussian Processes for Flexible Multi-Modal Physical Human Robot Interaction: threatens any claim of discrete robot actions; leaves room if the tokens carry force-target/compliance/passivity semantics and are evaluated under physical stiffness shifts.
- #251 A unified formulation of geometry-aware discrete dynamic movement primitives: threatens any claim of discrete robot actions; leaves room if the tokens carry force-target/compliance/passivity semantics and are evaluated under physical stiffness shifts.
- #268 Task-Based Robot Grasp Planning Using Probabilistic Inference: threatens any claim of discrete robot actions; leaves room if the tokens carry force-target/compliance/passivity semantics and are evaluated under physical stiffness shifts.

## Boundary against force/tactile/contact prior
- #2 A survey of robot manipulation in contact: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #3 Variable Impedance Control and Learning—A Review: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #5 A review on interaction control for contact robots through intent detection: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #6 Dynamic movement primitives in robotics: A tutorial survey: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #7 Efficient Force Control Learning System for Industrial Robots Based on Variable Impedance Control: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #11 A review on reinforcement learning for contact-rich robotic manipulation tasks: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #12 Variable impedance control on contact-rich manipulation of a collaborative industrial mobile manipulator: An imitation learning approach: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #15 A Survey on Imitation Learning for Contact-Rich Tasks in Robotics: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #16 Data-Efficient Reinforcement Learning for Variable Impedance Control: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #21 Dexterous Robotic Manipulation of Deformable Objects with Multi-Sensory Feedback - a Review: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #24 Dexterous Manipulation for Multi-Fingered Robotic Hands With Reinforcement Learning: A Review: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.
- #26 Geometric Reinforcement Learning for Robotic Manipulation: threatens any claim that force feedback is new; leaves room if force feedback defines the action coordinate system.

## Positive novelty boundary
The remaining claim is narrow: encode robot skill tokens as reusable energy-port impedance primitives, each executing a local closed-loop admittance/impedance law with force target, compliance, damping, and passivity budget. The token sequence is not a motion chunk; it is a composable physical interaction primitive. The paper must show that this distinction matters under environment-impedance shifts where kinematic tokens preserve visual/pose shape but fail force regulation.
