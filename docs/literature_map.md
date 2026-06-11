# Literature map

## Field box
This sweep treats the field as contact-rich robot skill learning where action abstractions, low-level control, and physical interaction are inseparable. The initial seed was impedance tokenization; the sweep deliberately includes impedance/admittance control, force control, movement primitives, learning from demonstration, tactile manipulation, discrete action vocabularies, action chunking, and robot foundation-model action representations.

## Coverage counts
- Total unique works in related_work_matrix.csv: 5512
- Required tiers: 1000-paper landscape sweep, 300-paper serious skim, 230-paper deep read, 100-paper hostile prior set.
- Landscape entries available: 5512
- Serious skim entries: 300
- Deep-read entries: 230
- Hostile prior entries: 100

## Five-year publication bins
- 1980-1984: 1
- 1985-1989: 9
- 1990-1994: 33
- 1995-1999: 41
- 2000-2004: 94
- 2005-2009: 158
- 2010-2014: 412
- 2015-2019: 1090
- 2020-2024: 2953
- 2025-2029: 721

## Retrieval queries
- tactile manipulation force control robot learning: 400
- options skill learning robotics manipulation: 400
- hybrid force position control robot manipulation: 400
- compliant contact manipulation learning control robot: 400
- variable stiffness actuator robot learning control: 400
- interaction primitives robot learning from demonstration: 400
- probabilistic movement primitives force control robot: 400
- contact rich manipulation robot learning force tactile: 400
- visuomotor policy action chunking robot manipulation: 400
- diffusion policy robot manipulation action chunking: 400
- robot foundation model action tokenization manipulation: 400
- robot impedance control skill learning: 399
- variable impedance control robot learning manipulation: 399
- movement primitives robot skill learning contact: 399
- learning from demonstration compliant manipulation force: 399
- passivity based robot control learning impedance: 399
- operational space control impedance robot manipulation: 399
- force control robot skill learning contact rich manipulation: 399
- vector quantization robot action tokenization skill learning: 399
- behavior cloning action tokenization robot manipulation: 399
- dynamic movement primitives impedance robot learning: 398
- robot manipulation skill primitives discrete latent actions: 398
- discrete latent action robotics imitation learning: 397
- admittance control learning from demonstration robot contact: 396

## Dominant mechanisms in the top 300
- task-specific learning/control formulation: 135
- demonstration-conditioned skill model: 67
- impedance/admittance regulation: 65
- movement primitive parameterization: 32
- force or hybrid force-position control: 24
- variable stiffness/compliance controller: 24
- dynamic movement primitive parameterization: 20
- tactile/force feedback representation: 17
- hierarchical option or skill abstraction: 10
- passivity or energy-based stability constraint: 8
- large pretrained robot/vision-language-action model: 3
- sequence model over observations/actions: 2
- probabilistic movement primitive model: 2
- diffusion or score-based visuomotor policy: 1
- discrete token vocabulary: 1
- operational-space control formulation: 1

## 300-paper serious skim clusters

### Impedance/admittance and variable stiffness
Representative top-ranked works in this cluster: 8 shown.
- #3 (2020) Variable Impedance Control and Learning—A Review. Mechanism: impedance/admittance regulation. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #7 (2018) Efficient Force Control Learning System for Industrial Robots Based on Variable Impedance Control. Mechanism: impedance/admittance regulation; force or hybrid force-position control. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #12 (2024) Variable impedance control on contact-rich manipulation of a collaborative industrial mobile manipulator: An imitation learning approach. Mechanism: impedance/admittance regulation; demonstration-conditioned skill model. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #16 (2024) Data-Efficient Reinforcement Learning for Variable Impedance Control. Mechanism: impedance/admittance regulation. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #26 (2023) Geometric Reinforcement Learning for Robotic Manipulation. Mechanism: variable stiffness/compliance controller. Leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes.
- #38 (2023) Embodied Communication: How Robots and People Communicate Through Physical Interaction. Mechanism: impedance/admittance regulation. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #39 (2019) Assisting Operators in Heavy Industrial Tasks: On the Design of an Optimized Cooperative Impedance Fuzzy-Controller With Embedded Safety Rules. Mechanism: impedance/admittance regulation. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #41 (2022) Pneumatic Soft Robots: Challenges and Benefits. Mechanism: task-specific learning/control formulation. Leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness.

### Force/tactile/contact-rich manipulation
Representative top-ranked works in this cluster: 8 shown.
- #2 (2022) A survey of robot manipulation in contact. Mechanism: task-specific learning/control formulation. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance.
- #3 (2020) Variable Impedance Control and Learning—A Review. Mechanism: impedance/admittance regulation. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #5 (2022) A review on interaction control for contact robots through intent detection. Mechanism: demonstration-conditioned skill model. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary.
- #6 (2023) Dynamic movement primitives in robotics: A tutorial survey. Mechanism: movement primitive parameterization; dynamic movement primitive parameterization; demonstration-conditioned skill model. Leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance.
- #7 (2018) Efficient Force Control Learning System for Industrial Robots Based on Variable Impedance Control. Mechanism: impedance/admittance regulation; force or hybrid force-position control. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #11 (2022) A review on reinforcement learning for contact-rich robotic manipulation tasks. Mechanism: task-specific learning/control formulation. Leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment.
- #12 (2024) Variable impedance control on contact-rich manipulation of a collaborative industrial mobile manipulator: An imitation learning approach. Mechanism: impedance/admittance regulation; demonstration-conditioned skill model. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #15 (2025) A Survey on Imitation Learning for Contact-Rich Tasks in Robotics. Mechanism: demonstration-conditioned skill model; large pretrained robot/vision-language-action model. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary.

### Movement primitives and LfD
Representative top-ranked works in this cluster: 8 shown.
- #5 (2022) A review on interaction control for contact robots through intent detection. Mechanism: demonstration-conditioned skill model. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary.
- #6 (2023) Dynamic movement primitives in robotics: A tutorial survey. Mechanism: movement primitive parameterization; dynamic movement primitive parameterization; demonstration-conditioned skill model. Leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance.
- #12 (2024) Variable impedance control on contact-rich manipulation of a collaborative industrial mobile manipulator: An imitation learning approach. Mechanism: impedance/admittance regulation; demonstration-conditioned skill model. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment.
- #13 (2018) Robot Learning from Demonstration in Robotic Assembly: A Survey. Mechanism: demonstration-conditioned skill model. Leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive.
- #15 (2025) A Survey on Imitation Learning for Contact-Rich Tasks in Robotics. Mechanism: demonstration-conditioned skill model; large pretrained robot/vision-language-action model. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary.
- #19 (2016) Haptics in Robot-Assisted Surgery: Challenges and Benefits. Mechanism: demonstration-conditioned skill model. Leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive.
- #23 (2022) A Metaverse: Taxonomy, Components, Applications, and Open Challenges. Mechanism: demonstration-conditioned skill model. Leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment.
- #25 (2018) Social Cognition for Human-Robot Symbiosis—Challenges and Building Blocks. Mechanism: demonstration-conditioned skill model. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary.

### Discrete/action-token policies
Representative top-ranked works in this cluster: 6 shown.
- #34 (2023) Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware. Mechanism: demonstration-conditioned skill model; sequence model over observations/actions. Leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment.
- #50 (2025) Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation. Mechanism: demonstration-conditioned skill model; diffusion or score-based visuomotor policy; discrete token vocabulary. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary / how to make the action vocabulary invariant to wall/object stiffness.
- #61 (2014) Modeling robot discrete movements with state-varying stiffness and damping: A framework for integrated motion generation and impedance control. Mechanism: impedance/admittance regulation; passivity or energy-based stability constraint; variable stiffness/compliance controller. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes.
- #151 (2022) Model Predictive Control with Gaussian Processes for Flexible Multi-Modal Physical Human Robot Interaction. Mechanism: impedance/admittance regulation. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes.
- #251 (2024) A unified formulation of geometry-aware discrete dynamic movement primitives. Mechanism: impedance/admittance regulation; movement primitive parameterization; dynamic movement primitive parameterization. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes.
- #268 (2015) Task-Based Robot Grasp Planning Using Probabilistic Inference. Mechanism: task-specific learning/control formulation. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary.

### Foundation/diffusion/visuomotor policies
Representative top-ranked works in this cluster: 8 shown.
- #15 (2025) A Survey on Imitation Learning for Contact-Rich Tasks in Robotics. Mechanism: demonstration-conditioned skill model; large pretrained robot/vision-language-action model. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary.
- #34 (2023) Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware. Mechanism: demonstration-conditioned skill model; sequence model over observations/actions. Leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment.
- #50 (2025) Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation. Mechanism: demonstration-conditioned skill model; diffusion or score-based visuomotor policy; discrete token vocabulary. Leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary / how to make the action vocabulary invariant to wall/object stiffness.
- #53 (2024) A Survey of Robot Intelligence with Large Language Models. Mechanism: large pretrained robot/vision-language-action model. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance.
- #107 (2021) What Is Robotics? Why Do We Need It and How Can We Get It?. Mechanism: task-specific learning/control formulation. Leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes.
- #108 (2023) Open X-Embodiment: Robotic Learning Datasets and RT-X Models. Mechanism: sequence model over observations/actions. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance.
- #137 (2016) Synthesizing robotic handwriting motion by learning from human demonstrations. Mechanism: task-specific learning/control formulation. Leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes.
- #138 (2023) Robot tool use: A survey. Mechanism: task-specific learning/control formulation. Leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance.

## 230-paper deep-read synthesis
The deeper abstract-level read changes the seed hypothesis. The strongest gap is not merely discrete impedance parameters; prior work already learns impedance, movement primitives, and discrete latent actions. The gap is that most action-token systems define token identity in kinematic or latent policy space, while most impedance-learning systems keep impedance as continuous controller state. A stronger paper must make the token itself a closed-loop, force-conditioned interaction law with passivity/energy semantics, then show that this representation changes robustness under stiffness/friction shifts.

## Hidden assumptions that may be false
1. Action symbols can be treated as kinematic commands rather than interaction laws.
2. The contact frame is known or can be inferred without changing the action representation.
3. Environment stiffness remains near the training range.
4. Friction changes do not alter the learned skill vocabulary.
5. Force/torque feedback is optional instead of structurally central.
6. Safety can be recovered after token selection rather than built into the token semantics.
7. The same token should mean the same Cartesian displacement across contacts.
8. Controller gains are fixed implementation details, not learnable skill variables.
9. Success is mostly determined by observation-action prediction accuracy.
10. Demonstrations provide enough coverage of force transients.
11. Contact-rich skills can be segmented using visual or pose cues alone.
12. Low-level servo dynamics do not affect high-level skill composition.
13. Robot morphology changes can be absorbed by retuning gains after learning.
14. The important latent state is object pose rather than stored/contact energy.
15. A single compliance schedule suffices for both free-space and contact phases.
16. Human demonstrations reveal intended impedance rather than only surface motion.
17. Discretization error is harmless if tokens are learned from many trajectories.
18. Benchmark success implies robustness to unmodeled stiffness and damping.
19. Learning can ignore passivity margins without causing brittle contact behavior.
20. A policy can first choose motion and then let a controller handle contact.
21. Force setpoints and impedance gains can be separated without loss.
22. Contact mode switches are exogenous labels rather than controlled phenomena.
23. Tactile observations are just additional sensors, not an action-coordinate system.
24. Temporal action chunks remain valid when the plant/environment impedance shifts.
25. The correct skill abstraction is a trajectory fragment rather than a closed-loop primitive.

## Candidate directions after breaking assumptions
- Energy-port impedance tokens: Discrete actions are passive admittance/impedance maps with explicit force target, compliance, damping, and energy tank semantics.
- Contact-frame tokenization: Tokens are expressed in estimated contact frames rather than camera or world frames, testing whether semantics survive geometric shifts.
- Transient-token imitation: Segment demonstrations by force transients and stored energy instead of visual pose changes.
- Morphology-normalized impedance alphabet: Normalize tokens by operational-space inertia so a vocabulary transfers across robot arms.
- Slip-recovery tactile tokens: Make micro-slip and force derivative the token coordinate system for tactile manipulation.

## Direction selected for this attempt
Selected: Energy-port impedance tokens. It most directly changes the central mechanism, has crisp hostile prior boundaries, and admits runnable evidence with a contact simulator plus a simple formal sensitivity argument.
