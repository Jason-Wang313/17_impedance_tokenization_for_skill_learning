# Hostile prior work set

This file records the 100 most threatening prior works from the ranked sweep. The extraction is metadata/abstract based and intentionally adversarial: each entry states what it already makes less novel and what remains open for the selected thesis.

## 1. Proactive human–robot collaboration: Mutual-cognitive, predictable, and self-organising perspectives (2022)
- Source: Robotics and Computer-Integrated Manufacturing; URL/DOI: https://doi.org/10.1016/j.rcim.2022.102510
- Problem claimed: Human–Robot Collaboration (HRC) has a pivotal role in smart manufacturing for strict requirements of human-centricity, sustainability, and resilience.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 2. A survey of robot manipulation in contact (2022)
- Source: Robotics and Autonomous Systems; URL/DOI: https://doi.org/10.1016/j.robot.2022.104224
- Problem claimed: Addresses robotic impedance control skill learning // variable impedance control robotic learning manipulation // admittance control learning from demonstration robotic contact // force control robotic skill learning contact rich manipulation // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // learning from demonstration compliant manipulation force // contact rich manipulation robotic learning force tactile // tactile manipulation force control robotic learning // robotic manipulation skill primitives discrete latent actions // discrete latent action robotics imitation learning // options skill learning robotics manipulation // passivity based robotic control learning impedance // hybrid force position control robotic manipulation // compliant contact manipulation learning control robotic // variable stiffness actuator robotic learning control // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robotic // operational space control impedance robotic manipulation.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 3. Variable Impedance Control and Learning—A Review (2020)
- Source: Institutional Research Information System (Università degli Studi di Trento); URL/DOI: https://doi.org/10.3389/frobt.2020.590681
- Problem claimed: Robots that physically interact with their surroundings, in order to accomplish some tasks or assist humans in their activities, require to exploit contact forces in a safe and proficient manner.
- Actual mechanism introduced: impedance/admittance regulation
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 4. Human–robot collaboration in industrial environments: A literature review on non-destructive disassembly (2021)
- Source: Robotics and Computer-Integrated Manufacturing; URL/DOI: https://doi.org/10.1016/j.rcim.2021.102208
- Problem claimed: Nowadays, numerous companies and industries introduce recycling processes in their production, aiming to increase the sustainable use of the planet’s natural resources.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Success is mostly determined by observation-action prediction accuracy. / Human demonstrations reveal intended impedance rather than only surface motion.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 5. A review on interaction control for contact robots through intent detection (2022)
- Source: Progress in Biomedical Engineering; URL/DOI: https://doi.org/10.1088/2516-1091/ac8193
- Problem claimed: Addresses robotic impedance control skill learning // variable impedance control robotic learning manipulation // admittance control learning from demonstration robotic contact // force control robotic skill learning contact rich manipulation // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // contact rich manipulation robotic learning force tactile // tactile manipulation force control robotic learning // options skill learning robotics manipulation // passivity based robotic control learning impedance // compliant contact manipulation learning control robotic // variable stiffness actuator robotic learning control // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robot.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 6. Dynamic movement primitives in robotics: A tutorial survey (2023)
- Source: The International Journal of Robotics Research; URL/DOI: https://doi.org/10.1177/02783649231201196
- Problem claimed: Biological systems, including human beings, have the innate ability to perform complex tasks in a versatile and agile manner.
- Actual mechanism introduced: movement primitive parameterization; dynamic movement primitive parameterization; demonstration-conditioned skill model
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 7. Efficient Force Control Learning System for Industrial Robots Based on Variable Impedance Control (2018)
- Source: Sensors; URL/DOI: https://doi.org/10.3390/s18082539
- Problem claimed: Learning variable impedance control is a powerful method to improve the performance of force control.
- Actual mechanism introduced: impedance/admittance regulation; force or hybrid force-position control
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 8. Progress and prospects of the human–robot collaboration (2017)
- Source: Autonomous Robots; URL/DOI: https://doi.org/10.1007/s10514-017-9677-2
- Problem claimed: Addresses robotic impedance control skill learning // variable impedance control robotic learning manipulation // admittance control learning from demonstration robotic contact // force control robotic skill learning contact rich manipulation // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // learning from demonstration compliant manipulation force // contact rich manipulation robotic learning force tactile // tactile manipulation force control robotic learning // passivity based robotic control learning impedance // hybrid force position control robotic manipulation // compliant contact manipulation learning control robotic // variable stiffness actuator robotic learning control // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robot.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Human demonstrations reveal intended impedance rather than only surface motion. / Tactile observations are just additional sensors, not an action-coordinate system. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 9. Past, Present, and Future of Aerial Robotic Manipulators (2021)
- Source: IEEE Transactions on Robotics; URL/DOI: https://doi.org/10.1109/tro.2021.3084395
- Problem claimed: Addresses variable impedance control robotic learning manipulation // admittance control learning from demonstration robotic contact // dynamic movement primitives impedance robotic learning // learning from demonstration compliant manipulation force // tactile manipulation force control robotic learning // passivity based robotic control learning impedance // hybrid force position control robotic manipulation // compliant contact manipulation learning control robotic // variable stiffness actuator robotic learning control // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robotic // operational space control impedance robotic manipulation.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 10. Survey on human–robot collaboration in industrial settings: Safety, intuitive interfaces and applications (2018)
- Source: Mechatronics; URL/DOI: https://doi.org/10.1016/j.mechatronics.2018.02.009
- Problem claimed: Addresses robotic impedance control skill learning // variable impedance control robotic learning manipulation // admittance control learning from demonstration robotic contact // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // learning from demonstration compliant manipulation force // tactile manipulation force control robotic learning // options skill learning robotics manipulation // hybrid force position control robotic manipulation // compliant contact manipulation learning control robotic // variable stiffness actuator robotic learning control // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robotic // operational space control impedance robotic manipulation.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Low-level servo dynamics do not affect high-level skill composition. / Learning can ignore passivity margins without causing brittle contact behavior. / Action symbols can be treated as kinematic commands rather than interaction laws.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 11. A review on reinforcement learning for contact-rich robotic manipulation tasks (2022)
- Source: Robotics and Computer-Integrated Manufacturing; URL/DOI: https://doi.org/10.1016/j.rcim.2022.102517
- Problem claimed: Research and application of reinforcement learning in robotics for contact-rich manipulation tasks have exploded in recent years.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment

## 12. Variable impedance control on contact-rich manipulation of a collaborative industrial mobile manipulator: An imitation learning approach (2024)
- Source: Robotics and Computer-Integrated Manufacturing; URL/DOI: https://doi.org/10.1016/j.rcim.2024.102896
- Problem claimed: • Developed a learning-based VIC using inverse reinforcement learning for robotic tasks.
- Actual mechanism introduced: impedance/admittance regulation; demonstration-conditioned skill model
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 13. Robot Learning from Demonstration in Robotic Assembly: A Survey (2018)
- Source: Robotics; URL/DOI: https://doi.org/10.3390/robotics7020017
- Problem claimed: Learning from demonstration (LfD) has been used to help robots to implement manipulation tasks autonomously, in particular, to learn manipulation behaviors from observing the motion executed by human demonstrators.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: Learning can ignore passivity margins without causing brittle contact behavior. / Action symbols can be treated as kinematic commands rather than interaction laws. / Controller gains are fixed implementation details, not learnable skill variables.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 14. Robotic disassembly of electric vehicle batteries: Technologies and opportunities (2024)
- Source: Computers & Industrial Engineering; URL/DOI: https://doi.org/10.1016/j.cie.2024.110727
- Problem claimed: • The uncertainty of EV batteries challenges robotic automation.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Controller gains are fixed implementation details, not learnable skill variables. / A single compliance schedule suffices for both free-space and contact phases. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 15. A Survey on Imitation Learning for Contact-Rich Tasks in Robotics (2025)
- Source: ArXiv.org; URL/DOI: https://doi.org/10.48550/arxiv.2506.13498
- Problem claimed: This paper comprehensively surveys research trends in imitation learning for contact-rich robotic tasks.
- Actual mechanism introduced: demonstration-conditioned skill model; large pretrained robot/vision-language-action model
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 16. Data-Efficient Reinforcement Learning for Variable Impedance Control (2024)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2024.3355311
- Problem claimed: One of the most crucial steps toward achieving human-like manipulation skills in robots is to incorporate compliance into the robot controller.
- Actual mechanism introduced: impedance/admittance regulation
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 17. A Review of Intent Detection, Arbitration, and Communication Aspects of Shared Control for Physical Human–Robot Interaction (2018)
- Source: Applied Mechanics Reviews; URL/DOI: https://doi.org/10.1115/1.4039145
- Problem claimed: As robotic devices are applied to problems beyond traditional manufacturing and industrial settings, we find that interaction between robots and humans, especially physical interaction, has become a fast developing field.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The same token should mean the same Cartesian displacement across contacts. / The important latent state is object pose rather than stored/contact energy. / Force setpoints and impedance gains can be separated without loss.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 18. Challenges and solutions for application and wider adoption of wearable robots (2021)
- Source: Wearable Technologies; URL/DOI: https://doi.org/10.1017/wtc.2021.13
- Problem claimed: The science and technology of wearable robots are steadily advancing, and the use of such robots in our everyday life appears to be within reach.
- Actual mechanism introduced: hierarchical option or skill abstraction
- Hidden assumptions: Safety can be recovered after token selection rather than built into the token semantics. / Robot morphology changes can be absorbed by retuning gains after learning. / A policy can first choose motion and then let a controller handle contact.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 19. Haptics in Robot-Assisted Surgery: Challenges and Benefits (2016)
- Source: IEEE Reviews in Biomedical Engineering; URL/DOI: https://doi.org/10.1109/rbme.2016.2538080
- Problem claimed: Robotic surgery is transforming the current surgical practice, not only by improving the conventional surgical methods but also by introducing innovative robot-enhanced approaches that broaden the capabilities of clinicians.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: Tactile observations are just additional sensors, not an action-coordinate system. / Force/torque feedback is optional instead of structurally central. / Low-level servo dynamics do not affect high-level skill composition.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 20. A User Study on Kinesthetic Teaching of Redundant Robots in Task and Configuration Space (2013)
- Source: Journal of Human-Robot Interaction; URL/DOI: https://doi.org/10.5898/jhri.2.1.wrede
- Problem claimed: The recent advent of compliant and kinematically redundant robots poses new research challenges for human-robot interaction.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force setpoints and impedance gains can be separated without loss. / Environment stiffness remains near the training range. / Demonstrations provide enough coverage of force transients.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 21. Dexterous Robotic Manipulation of Deformable Objects with Multi-Sensory Feedback - a Review (2010)
- Source: InTech eBooks; URL/DOI: https://doi.org/10.5772/9183
- Problem claimed: Dexterous Robotic Manipulation of Deformable Objects with Multi-Sensory Feedback -a Review 589 corresponding position at the contact points with the object.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 22. Trends of Human-Robot Collaboration in Industry Contexts: Handover, Learning, and Metrics (2021)
- Source: Sensors; URL/DOI: https://doi.org/10.3390/s21124113
- Problem claimed: Repetitive industrial tasks can be easily performed by traditional robotic systems.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Low-level servo dynamics do not affect high-level skill composition. / Learning can ignore passivity margins without causing brittle contact behavior. / Action symbols can be treated as kinematic commands rather than interaction laws.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 23. A Metaverse: Taxonomy, Components, Applications, and Open Challenges (2022)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2021.3140175
- Problem claimed: Unlike previous studies on the Metaverse based on Second Life, the current Metaverse is based on the social value of Generation Z that online and offline selves are not different.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: The important latent state is object pose rather than stored/contact energy. / Force setpoints and impedance gains can be separated without loss. / Environment stiffness remains near the training range.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment

## 24. Dexterous Manipulation for Multi-Fingered Robotic Hands With Reinforcement Learning: A Review (2022)
- Source: Frontiers in Neurorobotics; URL/DOI: https://doi.org/10.3389/fnbot.2022.861825
- Problem claimed: With the increasing demand for the dexterity of robotic operation, dexterous manipulation of multi-fingered robotic hands with reinforcement learning is an interesting subject in the field of robotics research.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 25. Social Cognition for Human-Robot Symbiosis—Challenges and Building Blocks (2018)
- Source: Frontiers in Neurorobotics; URL/DOI: https://doi.org/10.3389/fnbot.2018.00034
- Problem claimed: The next generation of robot companions or robot working partners will need to satisfy social requirements somehow similar to the famous laws of robotics envisaged by Isaac Asimov time ago (Asimov, 1942).
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Low-level servo dynamics do not affect high-level skill composition. / Learning can ignore passivity margins without causing brittle contact behavior.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 26. Geometric Reinforcement Learning for Robotic Manipulation (2023)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2023.3322654
- Problem claimed: Reinforcement learning (RL) is a popular technique that allows an agent to learn by trial and error while interacting with a dynamic environment.
- Actual mechanism introduced: variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: controller impedance/gains; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 27. Control Techniques for Safe, Ergonomic, and Efficient Human-Robot Collaboration in the Digital Industry: A Survey (2021)
- Source: IEEE Transactions on Automation Science and Engineering; URL/DOI: https://doi.org/10.1109/tase.2021.3131011
- Problem claimed: The fourth industrial revolution, also known as Industry 4.0, is reshaping the way individuals live and work while providing a substantial influence on the manufacturing scenario.
- Actual mechanism introduced: hierarchical option or skill abstraction
- Hidden assumptions: Human demonstrations reveal intended impedance rather than only surface motion. / Tactile observations are just additional sensors, not an action-coordinate system. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 28. Human-Robot Interaction Review: Challenges and Solutions for Modern Industrial Environments (2021)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2021.3099287
- Problem claimed: The demand for collaborative robots is growing in industrial environments due to their versatility and low prices.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Temporal action chunks remain valid when the plant/environment impedance shifts. / Safety can be recovered after token selection rather than built into the token semantics. / Robot morphology changes can be absorbed by retuning gains after learning.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 29. Tutorial Review of Bio-Inspired Approaches to Robotic Manipulation for Space Debris Salvage (2020)
- Source: Biomimetics; URL/DOI: https://doi.org/10.3390/biomimetics5020019
- Problem claimed: We present a comprehensive tutorial review that explores the application of bio-inspired approaches to robot control systems for grappling and manipulating a wide range of space debris targets.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 30. Survey on Recent Advances in Planning and Control for Collaborative Robotics (2024)
- Source: IEEJ Journal of Industry Applications; URL/DOI: https://doi.org/10.1541/ieejjia.24005652
- Problem claimed: Collaborative robots (COBOTs) can efficiently assist humans in interactions with robots and the environment when carrying out different tasks.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: Friction changes do not alter the learned skill vocabulary. / Contact-rich skills can be segmented using visual or pose cues alone. / Benchmark success implies robustness to unmodeled stiffness and damping.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 31. Human–robot skill transmission for mobile robot via learning by demonstration (2021)
- Source: Neural Computing and Applications; URL/DOI: https://doi.org/10.1007/s00521-021-06449-x
- Problem claimed: Addresses robotic impedance control skill learning // variable impedance control robotic learning manipulation // admittance control learning from demonstration robotic contact // force control robotic skill learning contact rich manipulation // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // hybrid force position control robotic manipulation // variable stiffness actuator robotic learning control // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robot.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 32. Toward Robotic Manipulation (2018)
- Source: Annual Review of Control Robotics and Autonomous Systems; URL/DOI: https://doi.org/10.1146/annurev-control-060117-104848
- Problem claimed: This article surveys manipulation, including both biological and robotic manipulation.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The correct skill abstraction is a trajectory fragment rather than a closed-loop primitive. / The same token should mean the same Cartesian displacement across contacts. / The important latent state is object pose rather than stored/contact energy.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 33. Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models (2022)
- Source: Robotics and Computer-Integrated Manufacturing; URL/DOI: https://doi.org/10.1016/j.rcim.2022.102484
- Problem claimed: Industrial robots form an integral part of today's manufacturing industry, due to their high versatility, precision, and fatigue proof nature.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Low-level servo dynamics do not affect high-level skill composition. / Learning can ignore passivity margins without causing brittle contact behavior. / Action symbols can be treated as kinematic commands rather than interaction laws.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 34. Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (2023)
- Source: ; URL/DOI: https://doi.org/10.15607/rss.2023.xix.016
- Problem claimed: Addresses force control robotic skill learning contact rich manipulation // movement primitives robotic skill learning contact // contact rich manipulation robotic learning force tactile // tactile manipulation force control robotic learning // robotic manipulation skill primitives discrete latent actions // discrete latent action robotics imitation learning // behavior cloning action tokenization robotic manipulation // visuomotor policy action chunking robotic manipulation // interaction primitives robotic learning from demonstration.
- Actual mechanism introduced: demonstration-conditioned skill model; sequence model over observations/actions
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Sequence models and action chunks for robot manipulation are prior art.
- What it leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment

## 35. Robotics and Neuroscience (2014)
- Source: Current Biology; URL/DOI: https://doi.org/10.1016/j.cub.2014.07.058
- Problem claimed: Addresses robotic impedance control skill learning // force control robotic skill learning contact rich manipulation // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // contact rich manipulation robotic learning force tactile // tactile manipulation force control robotic learning // robotic manipulation skill primitives discrete latent actions // discrete latent action robotics imitation learning // options skill learning robotics manipulation // compliant contact manipulation learning control robotic // interaction primitives robotic learning from demonstration // operational space control impedance robotic manipulation.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Environment stiffness remains near the training range. / Demonstrations provide enough coverage of force transients. / Discretization error is harmless if tokens are learned from many trajectories.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 36. Guided Reinforcement Learning: A Review and Evaluation for Efficient and Effective Real-World Robotics [Survey] (2022)
- Source: IEEE Robotics & Automation Magazine; URL/DOI: https://doi.org/10.1109/mra.2022.3207664
- Problem claimed: Recent successes aside, reinforcement learning (RL) still faces significant challenges in its application to the real-world robotics domain.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment

## 37. An Adaptive Imitation Learning Framework for Robotic Complex Contact-Rich Insertion Tasks (2022)
- Source: Frontiers in Robotics and AI; URL/DOI: https://doi.org/10.3389/frobt.2021.777363
- Problem claimed: Complex contact-rich insertion is a ubiquitous robotic manipulation skill and usually involves nonlinear and low-clearance insertion trajectories as well as varying force requirements.
- Actual mechanism introduced: force or hybrid force-position control; movement primitive parameterization; dynamic movement primitive parameterization
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 38. Embodied Communication: How Robots and People Communicate Through Physical Interaction (2023)
- Source: Annual Review of Control Robotics and Autonomous Systems; URL/DOI: https://doi.org/10.1146/annurev-control-070122-102501
- Problem claimed: Addresses robotic impedance control skill learning // admittance control learning from demonstration robotic contact // force control robotic skill learning contact rich manipulation // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // contact rich manipulation robotic learning force tactile // compliant contact manipulation learning control robotic // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robot.
- Actual mechanism introduced: impedance/admittance regulation
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: force feedback semantics; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 39. Assisting Operators in Heavy Industrial Tasks: On the Design of an Optimized Cooperative Impedance Fuzzy-Controller With Embedded Safety Rules (2019)
- Source: Frontiers in Robotics and AI; URL/DOI: https://doi.org/10.3389/frobt.2019.00075
- Problem claimed: Human-robot cooperation is increasingly demanded in industrial applications.
- Actual mechanism introduced: impedance/admittance regulation
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 40. Learning for a Robot: Deep Reinforcement Learning, Imitation Learning, Transfer Learning (2021)
- Source: Sensors; URL/DOI: https://doi.org/10.3390/s21041278
- Problem claimed: Dexterous manipulation of the robot is an important part of realizing intelligence, but manipulators can only perform simple tasks such as sorting and packing in a structured environment.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 41. Pneumatic Soft Robots: Challenges and Benefits (2022)
- Source: Actuators; URL/DOI: https://doi.org/10.3390/act11030092
- Problem claimed: Addresses variable impedance control robotic learning manipulation // admittance control learning from demonstration robotic contact // tactile manipulation force control robotic learning // compliant contact manipulation learning control robotic // variable stiffness actuator robotic learning control.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Safety can be recovered after token selection rather than built into the token semantics. / Robot morphology changes can be absorbed by retuning gains after learning. / A policy can first choose motion and then let a controller handle contact.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 42. Learning Deep Robotic Skills on Riemannian Manifolds (2022)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2022.3217800
- Problem claimed: In this paper, we propose RiemannianFlow, a deep generative model that allows robots to learn complex and stable skills evolving on the Riemannian manifold.
- Actual mechanism introduced: variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 43. Robot learning from demonstration of force-based manipulation tasks (2013)
- Source: ; URL/DOI: https://doi.org/10.5821/dissertation-2117-95104
- Problem claimed: One of the main challenges in Robotics is to develop robots that can interact with humans in a natural way, sharing the same dynamic and unstructured environments.
- Actual mechanism introduced: impedance/admittance regulation; demonstration-conditioned skill model; variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 44. Soft Pneumatic Actuators: A Review of Design, Fabrication, Modeling, Sensing, Control and Applications (2022)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2022.3179589
- Problem claimed: Soft robotics is a rapidly evolving field where robots are fabricated using highly deformable materials and usually follow a bioinspired design.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: Friction changes do not alter the learned skill vocabulary. / Contact-rich skills can be segmented using visual or pose cues alone. / Benchmark success implies robustness to unmodeled stiffness and damping.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 45. Learning periodic skills for robotic manipulation: Insights on orientation and impedance (2024)
- Source: Robotics and Autonomous Systems; URL/DOI: https://doi.org/10.1016/j.robot.2024.104763
- Problem claimed: Many daily tasks exhibit a periodic nature, necessitating that robots possess the ability to execute them either alone or in collaboration with humans.
- Actual mechanism introduced: impedance/admittance regulation; movement primitive parameterization; dynamic movement primitive parameterization
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Action symbols can be treated as kinematic commands rather than interaction laws.
- Variables treated as fixed: force feedback semantics; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 46. Learning Force‐Relevant Skills from Human Demonstration (2019)
- Source: Complexity; URL/DOI: https://doi.org/10.1155/2019/5262859
- Problem claimed: Many human manipulation skills are force relevant, such as opening a bottle cap and assembling furniture.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 47. Hand synergies: Integration of robotics and neuroscience for understanding the control of biological and artificial hands (2016)
- Source: Physics of Life Reviews; URL/DOI: https://doi.org/10.1016/j.plrev.2016.02.001
- Problem claimed: Addresses robotic impedance control skill learning // variable impedance control robotic learning manipulation // force control robotic skill learning contact rich manipulation // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // learning from demonstration compliant manipulation force // contact rich manipulation robotic learning force tactile // tactile manipulation force control robotic learning // compliant contact manipulation learning control robotic // variable stiffness actuator robotic learning control // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robot.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Contact-rich skills can be segmented using visual or pose cues alone. / Benchmark success implies robustness to unmodeled stiffness and damping. / The correct skill abstraction is a trajectory fragment rather than a closed-loop primitive.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 48. Human augmentation by wearable supernumerary robotic limbs: review and perspectives (2021)
- Source: Progress in Biomedical Engineering; URL/DOI: https://doi.org/10.1088/2516-1091/ac2294
- Problem claimed: Supernumerary robotic limbs (SRLs) are wearable robots designed to enhance the sensorimotor abilities of humans.
- Actual mechanism introduced: hierarchical option or skill abstraction
- Hidden assumptions: Action symbols can be treated as kinematic commands rather than interaction laws. / Controller gains are fixed implementation details, not learnable skill variables. / A single compliance schedule suffices for both free-space and contact phases.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 49. Passive Motion Paradigm: An Alternative to Optimal Control (2011)
- Source: Frontiers in Neurorobotics; URL/DOI: https://doi.org/10.3389/fnbot.2011.00004
- Problem claimed: IN THE LAST YEARS, OPTIMAL CONTROL THEORY (OCT) HAS EMERGED AS THE LEADING APPROACH FOR INVESTIGATING NEURAL CONTROL OF MOVEMENT AND MOTOR COGNITION FOR TWO COMPLEMENTARY RESEARCH LINES: behavioral neuroscience and humanoid robotics.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 50. Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation (2025)
- Source: ; URL/DOI: https://doi.org/10.15607/rss.2025.xxi.052
- Problem claimed: Addresses force control robotic skill learning contact rich manipulation // movement primitives robotic skill learning contact // learning from demonstration compliant manipulation force // contact rich manipulation robotic learning force tactile // tactile manipulation force control robotic learning // robotic foundation model action tokenization manipulation // visuomotor policy action chunking robotic manipulation // diffusion policy robotic manipulation action chunking // compliant contact manipulation learning control robot.
- Actual mechanism introduced: demonstration-conditioned skill model; diffusion or score-based visuomotor policy; discrete token vocabulary
- Hidden assumptions: Action symbols can be treated as kinematic commands rather than interaction laws. / Discretization error is harmless if tokens are learned from many trajectories. / Temporal action chunks remain valid when the plant/environment impedance shifts. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch
- What it makes less novel: Discrete latent/action vocabularies for policies are prior art.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary / how to make the action vocabulary invariant to wall/object stiffness

## 51. A Practical Roadmap to Learning from Demonstration for Robotic Manipulators in Manufacturing (2024)
- Source: Robotics; URL/DOI: https://doi.org/10.3390/robotics13070100
- Problem claimed: This paper provides a structured and practical roadmap for practitioners to integrate learning from demonstration (LfD) into manufacturing tasks, with a specific focus on industrial manipulators.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: Benchmark success implies robustness to unmodeled stiffness and damping. / The correct skill abstraction is a trajectory fragment rather than a closed-loop primitive. / The same token should mean the same Cartesian displacement across contacts.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 52. Lower limb exoskeleton robot and its cooperative control: A review, trends, and challenges for future research (2023)
- Source: Frontiers in Neurorobotics; URL/DOI: https://doi.org/10.3389/fnbot.2022.913748
- Problem claimed: Effective control of an exoskeleton robot (ER) using a human-robot interface is crucial for assessing the robot's movements and the force they produce to generate efficient control signals.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 53. A Survey of Robot Intelligence with Large Language Models (2024)
- Source: Applied Sciences; URL/DOI: https://doi.org/10.3390/app14198868
- Problem claimed: Since the emergence of ChatGPT, research on large language models (LLMs) has actively progressed across various fields.
- Actual mechanism introduced: large pretrained robot/vision-language-action model
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 54. A Planning Framework for Robotic Insertion Tasks via Hydroelastic Contact Model (2023)
- Source: Machines; URL/DOI: https://doi.org/10.3390/machines11070741
- Problem claimed: Robotic contact-rich insertion tasks present a significant challenge for motion planning due to the complex force interaction between robots and objects.
- Actual mechanism introduced: movement primitive parameterization; dynamic movement primitive parameterization
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 55. Review of machine learning methods in soft robotics (2021)
- Source: PLoS ONE; URL/DOI: https://doi.org/10.1371/journal.pone.0246102
- Problem claimed: Soft robots have been extensively researched due to their flexible, deformable, and adaptive characteristics.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: Tactile observations are just additional sensors, not an action-coordinate system. / Force/torque feedback is optional instead of structurally central. / Low-level servo dynamics do not affect high-level skill composition.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment

## 56. Haptics Electromyography Perception and Learning Enhanced Intelligence for Teleoperated Robot (2018)
- Source: IEEE Transactions on Automation Science and Engineering; URL/DOI: https://doi.org/10.1109/tase.2018.2874454
- Problem claimed: Due to the lack of transparent and friendly human-robot interaction (HRI) interface, as well as various uncertainties, it is usually a challenge to remotely manipulate a robot to accomplish a complicated task.
- Actual mechanism introduced: variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 57. Perspectives and Challenges in Robotic Neurorehabilitation (2019)
- Source: Applied Sciences; URL/DOI: https://doi.org/10.3390/app9153183
- Problem claimed: The development of robotic devices for rehabilitation is a fast-growing field.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Success is mostly determined by observation-action prediction accuracy. / Human demonstrations reveal intended impedance rather than only surface motion. / Tactile observations are just additional sensors, not an action-coordinate system.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 58. Cobot programming for collaborative industrial tasks: An overview (2019)
- Source: Robotics and Autonomous Systems; URL/DOI: https://doi.org/10.1016/j.robot.2019.03.003
- Problem claimed: Addresses robotic impedance control skill learning // force control robotic skill learning contact rich manipulation // dynamic movement primitives impedance robotic learning // movement primitives robotic skill learning contact // learning from demonstration compliant manipulation force // contact rich manipulation robotic learning force tactile // options skill learning robotics manipulation // compliant contact manipulation learning control robotic // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robotic // operational space control impedance robotic manipulation.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Friction changes do not alter the learned skill vocabulary. / Contact-rich skills can be segmented using visual or pose cues alone. / Benchmark success implies robustness to unmodeled stiffness and damping.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 59. Imitation Learning-Based System for the Execution of Self-Paced Robotic-Assisted Passive Rehabilitation Exercises (2023)
- Source: IEEE Robotics and Automation Letters; URL/DOI: https://doi.org/10.1109/lra.2023.3281884
- Problem claimed: The development of robotic-assisted rehabilitation exercises involving physical human-robot interaction requires extreme care since an injured limb may be in physical contact with the robot, so compliant behavior is imperative for these tasks.
- Actual mechanism introduced: impedance/admittance regulation; force or hybrid force-position control; movement primitive parameterization
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 60. Leveraging Morphological Computation for Controlling Soft Robots: Learning from Nature to Control Soft Robots (2023)
- Source: IEEE Control Systems; URL/DOI: https://doi.org/10.1109/mcs.2023.3253422
- Problem claimed: Traditional robot designs typically employ rigid body parts and high-torque servo motors.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Environment stiffness remains near the training range. / Demonstrations provide enough coverage of force transients. / Discretization error is harmless if tokens are learned from many trajectories.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 61. Modeling robot discrete movements with state-varying stiffness and damping: A framework for integrated motion generation and impedance control (2014)
- Source: ; URL/DOI: https://doi.org/10.15607/rss.2014.x.022
- Problem claimed: Successful execution of many robotic tasks requires precise control of robot motion and its interaction with the environment.
- Actual mechanism introduced: impedance/admittance regulation; passivity or energy-based stability constraint; variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Action symbols can be treated as kinematic commands rather than interaction laws.
- Variables treated as fixed: force feedback semantics; friction/contact dissipation; robot morphology
- Failure modes ignored: force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 62. Efficient learning variable impedance control for industrial robots (2019)
- Source: Bulletin of the Polish Academy of Sciences Technical Sciences; URL/DOI: https://doi.org/10.24425/bpas.2019.128116
- Problem claimed: Compared with the robots, humans can learn to perform various contact tasks in unstructured environments by modulating arm impedance characteristics.
- Actual mechanism introduced: impedance/admittance regulation; force or hybrid force-position control
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 63. Towards Autonomous Robotic Assembly: Using Combined Visual and Tactile Sensing for Adaptive Task Execution (2021)
- Source: Journal of Intelligent & Robotic Systems; URL/DOI: https://doi.org/10.1007/s10846-020-01303-z
- Problem claimed: Abstract Robotic assembly tasks are typically implemented in static settings in which parts are kept at fixed locations by making use of part holders.
- Actual mechanism introduced: impedance/admittance regulation; tactile/force feedback representation
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: force feedback semantics; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 64. A probabilistic framework for learning geometry-based robot manipulation skills (2021)
- Source: Robotics and Autonomous Systems; URL/DOI: https://doi.org/10.1016/j.robot.2021.103761
- Problem claimed: Programming robots to perform complex manipulation tasks is difficult because many tasks require sophisticated controllers that may rely on data such as manipulability ellipsoids, stiffness/damping and inertia matrices.
- Actual mechanism introduced: movement primitive parameterization; demonstration-conditioned skill model; variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 65. Imitation Learning of Compression Pattern in Robotic-Assisted Ultrasound Examination Using Kernelized Movement Primitives (2024)
- Source: IEEE Transactions on Medical Robotics and Bionics; URL/DOI: https://doi.org/10.1109/tmrb.2024.3472856
- Problem claimed: Vascular diseases are commonly diagnosed using Ultrasound (US) imaging, which can be inconsistent due to its high dependence on the operator’s skill.
- Actual mechanism introduced: force or hybrid force-position control; movement primitive parameterization; demonstration-conditioned skill model
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 66. A Survey of Space Robotic Technologies for On-Orbit Assembly (2022)
- Source: Space Science & Technology; URL/DOI: https://doi.org/10.34133/2022/9849170
- Problem claimed: The construction of large structures is one of the main development trends of the space exploration in the future, such as large space stations, large space solar power stations, and large space telescopes.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Benchmark success implies robustness to unmodeled stiffness and damping. / The correct skill abstraction is a trajectory fragment rather than a closed-loop primitive. / The same token should mean the same Cartesian displacement across contacts.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 67. Sensing in Soft Robotics (2023)
- Source: ACS Nano; URL/DOI: https://doi.org/10.1021/acsnano.3c04089
- Problem claimed: Soft robotics is an exciting field of science and technology that enables robots to manipulate objects with human-like dexterity.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 68. Learning object-level impedance control for robust grasping and dexterous manipulation (2014)
- Source: ; URL/DOI: https://doi.org/10.1109/icra.2014.6907861
- Problem claimed: Object-level impedance control is of great importance for object-centric tasks, such as robust grasping and dexterous manipulation.
- Actual mechanism introduced: impedance/admittance regulation; tactile/force feedback representation; variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: force feedback semantics; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; force overshoot despite visual/pose success
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 69. Humanoid Robots in Aircraft Manufacturing: The Airbus Use Cases (2019)
- Source: IEEE Robotics & Automation Magazine; URL/DOI: https://doi.org/10.1109/mra.2019.2943395
- Problem claimed: We report on the results of a collaborative project that investigated the deployment of humanoid robotic solutions in air-craft manufacturing for several assembly op erations where access by wheeled or railported robotic platforms is not possible.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 70. A Framework for Robot Manipulation: Skill Formalism, Meta Learning and Adaptive Control (2019)
- Source: ; URL/DOI: https://doi.org/10.1109/icra.2019.8793542
- Problem claimed: In this paper we introduce a novel framework for expressing and learning force-sensitive robot manipulation skills.
- Actual mechanism introduced: impedance/admittance regulation
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 71. Sensors for Robotic Hands: A Survey of State of the Art (2015)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2015.2482543
- Problem claimed: Recent decades have seen significant progress in the field of artificial hands.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The same token should mean the same Cartesian displacement across contacts. / The important latent state is object pose rather than stored/contact energy. / Force setpoints and impedance gains can be separated without loss.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 72. Arm-hand motion-force coordination for physical interactions with non-flat surfaces using dynamical systems: Toward compliant robotic massage (2020)
- Source: ; URL/DOI: https://doi.org/10.1109/icra40945.2020.9196593
- Problem claimed: Many manipulation tasks require coordinated motions for arm and fingers.
- Actual mechanism introduced: impedance/admittance regulation; force or hybrid force-position control
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Action symbols can be treated as kinematic commands rather than interaction laws.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Closed-loop force/position control for contact is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 73. A Survey on Policy Search Algorithms for Learning Robot Controllers in a Handful of Trials (2019)
- Source: IEEE Transactions on Robotics; URL/DOI: https://doi.org/10.1109/tro.2019.2958211
- Problem claimed: Most policy search (PS) algorithms require thousands of training episodes to find an effective policy, which is often infeasible with a physical robot.
- Actual mechanism introduced: movement primitive parameterization; dynamic movement primitive parameterization
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 74. Interactive Imitation Learning of Bimanual Movement Primitives (2023)
- Source: IEEE/ASME Transactions on Mechatronics; URL/DOI: https://doi.org/10.1109/tmech.2023.3295249
- Problem claimed: Performing bimanual tasks with dual robotic setups can drastically increase the impact on industrial and daily life applications.
- Actual mechanism introduced: impedance/admittance regulation; movement primitive parameterization; demonstration-conditioned skill model
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: force feedback semantics; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 75. Robotic Manipulation and Capture in Space: A Survey (2021)
- Source: Frontiers in Robotics and AI; URL/DOI: https://doi.org/10.3389/frobt.2021.686723
- Problem claimed: Space exploration and exploitation depend on the development of on-orbit robotic capabilities for tasks such as servicing of satellites, removing of orbital debris, or construction and maintenance of orbital assets.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 76. Exploring the synergy of human-robot teaming, digital twins, and machine learning in Industry 5.0: a step towards sustainable manufacturing (2025)
- Source: Journal of Intelligent Manufacturing; URL/DOI: https://doi.org/10.1007/s10845-025-02580-x
- Problem claimed: Abstract Sustainable manufacturing remains a central objective of Industry 5.0.
- Actual mechanism introduced: impedance/admittance regulation; demonstration-conditioned skill model
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 77. Residual Learning From Demonstration: Adapting DMPs for Contact-Rich Manipulation (2022)
- Source: IEEE Robotics and Automation Letters; URL/DOI: https://doi.org/10.1109/lra.2022.3150024
- Problem claimed: Manipulation skills involving contact and friction are inherent to many robotics tasks.
- Actual mechanism introduced: movement primitive parameterization; dynamic movement primitive parameterization; demonstration-conditioned skill model
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 78. Human robot cooperation with compliance adaptation along the motion trajectory (2017)
- Source: Autonomous Robots; URL/DOI: https://doi.org/10.1007/s10514-017-9676-3
- Problem claimed: Addresses robotic impedance control skill learning // variable impedance control robotic learning manipulation // dynamic movement primitives impedance robotic learning // learning from demonstration compliant manipulation force // options skill learning robotics manipulation // passivity based robotic control learning impedance // interaction primitives robotic learning from demonstration // probabilistic movement primitives force control robotic // operational space control impedance robotic manipulation.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 79. Teaching a Robot the Semantics of Assembly Tasks (2017)
- Source: IEEE Transactions on Systems Man and Cybernetics Systems; URL/DOI: https://doi.org/10.1109/tsmc.2016.2635479
- Problem claimed: We present a three-level cognitive system in a learning by demonstration context.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: A policy can first choose motion and then let a controller handle contact. / The contact frame is known or can be inferred without changing the action representation. / Success is mostly determined by observation-action prediction accuracy.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 80. Variable Compliance Control for Robotic Peg-in-Hole Assembly: A Deep-Reinforcement-Learning Approach (2020)
- Source: Applied Sciences; URL/DOI: https://doi.org/10.3390/app10196923
- Problem claimed: Industrial robot manipulators are playing a significant role in modern manufacturing industries.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make contact transients the training signal rather than a nuisance / how to expose when a learned skill is only a replayed kinematic fragment

## 81. Model predictive impedance control with Gaussian processes for human and environment interaction (2023)
- Source: Robotics and Autonomous Systems; URL/DOI: https://doi.org/10.1016/j.robot.2023.104431
- Problem claimed: Addresses robotic impedance control skill learning // variable impedance control robotic learning manipulation // admittance control learning from demonstration robotic contact // dynamic movement primitives impedance robotic learning // probabilistic movement primitives force control robot.
- Actual mechanism introduced: impedance/admittance regulation
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior.
- Variables treated as fixed: force feedback semantics; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 82. Composite dynamic movement primitives based on neural networks for human–robot skill transfer (2021)
- Source: Neural Computing and Applications; URL/DOI: https://doi.org/10.1007/s00521-021-05747-8
- Problem claimed: Abstract In this paper, composite dynamic movement primitives (DMPs) based on radial basis function neural networks (RBFNNs) are investigated for robots’ skill learning from human demonstrations.
- Actual mechanism introduced: movement primitive parameterization; dynamic movement primitive parameterization
- Hidden assumptions: Action symbols can be treated as kinematic commands rather than interaction laws. / Discretization error is harmless if tokens are learned from many trajectories. / Temporal action chunks remain valid when the plant/environment impedance shifts. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 83. An Improvement of Robot Stiffness-Adaptive Skill Primitive Generalization Using the Surface Electromyography in Human–Robot Collaboration (2021)
- Source: Frontiers in Neuroscience; URL/DOI: https://doi.org/10.3389/fnins.2021.694914
- Problem claimed: Learning from Demonstration in robotics has proved its efficiency in robot skill learning.
- Actual mechanism introduced: movement primitive parameterization; probabilistic movement primitive model; demonstration-conditioned skill model
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / Force/torque feedback is optional instead of structurally central.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 84. Vision-force-fused curriculum learning for robotic contact-rich assembly tasks (2023)
- Source: Frontiers in Neurorobotics; URL/DOI: https://doi.org/10.3389/fnbot.2023.1280773
- Problem claimed: Contact-rich robotic manipulation tasks such as assembly are widely studied due to their close relevance with social and manufacturing industries.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 85. A Survey of Multifingered Robotic Manipulation: Biological Results, Structural Evolvements, and Learning Methods (2022)
- Source: Frontiers in Neurorobotics; URL/DOI: https://doi.org/10.3389/fnbot.2022.843267
- Problem claimed: Multifingered robotic hands (usually referred to as dexterous hands) are designed to achieve human-level or human-like manipulations for robots or as prostheses for the disabled.
- Actual mechanism introduced: demonstration-conditioned skill model; tactile/force feedback representation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 86. A survey on robotic devices for upper limb rehabilitation (2014)
- Source: Journal of NeuroEngineering and Rehabilitation; URL/DOI: https://doi.org/10.1186/1743-0003-11-3
- Problem claimed: The existing shortage of therapists and caregivers assisting physically disabled individuals at home is expected to increase and become serious problem in the near future.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Success is mostly determined by observation-action prediction accuracy. / Human demonstrations reveal intended impedance rather than only surface motion. / Tactile observations are just additional sensors, not an action-coordinate system.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 87. Gaussian-process-based robot learning from demonstration (2023)
- Source: Journal of Ambient Intelligence and Humanized Computing; URL/DOI: https://doi.org/10.1007/s12652-023-04551-7
- Problem claimed: Abstract Learning from demonstration allows to encode task constraints from observing the motion executed by a human teacher.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to encode force targets and compliance in one discrete primitive

## 88. Active Impedance Control of Bioinspired Motion Robotic Manipulators: An Overview (2018)
- Source: Applied Bionics and Biomechanics; URL/DOI: https://doi.org/10.1155/2018/8203054
- Problem claimed: There are two main categories of force control schemes: hybrid position-force control and impedance control.
- Actual mechanism introduced: impedance/admittance regulation; force or hybrid force-position control; demonstration-conditioned skill model
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; unobserved slip or micro-contact changes
- What it makes less novel: Closed-loop force/position control for contact is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 89. A Survey on Deep Reinforcement Learning Algorithms for Robotic Manipulation (2023)
- Source: Sensors; URL/DOI: https://doi.org/10.3390/s23073762
- Problem claimed: Robotic manipulation challenges, such as grasping and object manipulation, have been tackled successfully with the help of deep reinforcement learning systems.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 90. A Framework for Composite Layup Skill Learning and Generalizing Through Teleoperation (2022)
- Source: Frontiers in Neurorobotics; URL/DOI: https://doi.org/10.3389/fnbot.2022.840240
- Problem claimed: In this article, an impedance control-based framework for human-robot composite layup skill transfer was developed, and the human-in-the-loop mechanism was investigated to achieve human-robot skill transfer.
- Actual mechanism introduced: impedance/admittance regulation; movement primitive parameterization; dynamic movement primitive parameterization
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior.
- Variables treated as fixed: force feedback semantics; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 91. User intent estimation during robot learning using physical human robot interaction primitives (2022)
- Source: Autonomous Robots; URL/DOI: https://doi.org/10.1007/s10514-021-10030-9
- Problem claimed: Abstract As robotic systems transition from traditional setups to collaborative work spaces, the prevalence of physical Human Robot Interaction has risen in both industrial and domestic environments.
- Actual mechanism introduced: movement primitive parameterization
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Encoding skills as reusable temporal primitives is prior art.
- What it leaves open: how to make the action vocabulary invariant to wall/object stiffness / how to make contact transients the training signal rather than a nuisance

## 92. Robot Collisions: A Survey on Detection, Isolation, and Identification (2017)
- Source: IEEE Transactions on Robotics; URL/DOI: https://doi.org/10.1109/tro.2017.2723903
- Problem claimed: Robot assistants and professional coworkers are becoming a commodity in domestic and industrial settings.
- Actual mechanism introduced: demonstration-conditioned skill model
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to encode force targets and compliance in one discrete primitive / how to preserve passivity after learning a discrete action vocabulary

## 93. Review on Control Strategies for Lower Limb Rehabilitation Exoskeletons (2021)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2021.3110595
- Problem claimed: Research on lower limb exoskeleton (LLE) for rehabilitation have developed rapidly to meet the need of the population with neurologic injuries.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force setpoints and impedance gains can be separated without loss. / Environment stiffness remains near the training range. / Demonstrations provide enough coverage of force transients.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to make contact transients the training signal rather than a nuisance

## 94. Compliant Force Control for Robots: A Survey (2025)
- Source: Mathematics; URL/DOI: https://doi.org/10.3390/math13132204
- Problem claimed: Compliant force control is a fundamental capability for enabling robots to interact safely and effectively with dynamic and uncertain environments.
- Actual mechanism introduced: impedance/admittance regulation; force or hybrid force-position control
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 95. A Hybrid Learning and Optimization Framework to Achieve Physically Interactive Tasks With Mobile Manipulators (2022)
- Source: IEEE Robotics and Automation Letters; URL/DOI: https://doi.org/10.1109/lra.2022.3187258
- Problem claimed: This letter proposes a hybrid learning and optimization framework for mobile manipulators for complex and physically interactive tasks.
- Actual mechanism introduced: impedance/admittance regulation; passivity or energy-based stability constraint; variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment / how to make the action vocabulary invariant to wall/object stiffness

## 96. Purposeful Communication in Human–Robot Collaboration: A Review of Modern Approaches in Manufacturing (2022)
- Source: IEEE Access; URL/DOI: https://doi.org/10.1109/access.2022.3227049
- Problem claimed: The uncertainties arising from the imperfection of the shared understanding during human-robot collaboration (HRC) is a critical challenge in developing real-world robots, which has attracted attention in various fields, especially in the manufacturing sector.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Demonstrations provide enough coverage of force transients. / Discretization error is harmless if tokens are learned from many trajectories. / Temporal action chunks remain valid when the plant/environment impedance shifts.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 97. Cutaneous/Tactile Haptic Feedback in Robotic Teleoperation: Motivation, Survey, and Perspectives (2023)
- Source: IEEE Transactions on Robotics; URL/DOI: https://doi.org/10.1109/tro.2023.3344027
- Problem claimed: Cutaneous haptic feedback has recently received great attention from researchers in the robotic teleoperation field, as it has been proven to convey rich information to the human operator while guaranteeing the safety and stability of the control loop.
- Actual mechanism introduced: tactile/force feedback representation
- Hidden assumptions: The contact frame is known or can be inferred without changing the action representation. / Friction changes do not alter the learned skill vocabulary. / Contact mode switches are exogenous labels rather than controlled phenomena.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 98. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023)
- Source: arXiv (Cornell University); URL/DOI: https://doi.org/10.48550/arxiv.2307.05973
- Problem claimed: Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning and planning.
- Actual mechanism introduced: task-specific learning/control formulation
- Hidden assumptions: Force/torque feedback is optional instead of structurally central. / Contact-rich skills can be segmented using visual or pose cues alone. / A policy can first choose motion and then let a controller handle contact. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: controller impedance/gains; force feedback semantics; environment stiffness; friction/contact dissipation
- Failure modes ignored: energy injection / non-passive learned action; stiff or soft environment mismatch; force overshoot despite visual/pose success; unobserved slip or micro-contact changes
- What it makes less novel: Robot skill-learning/control formulation reduces novelty of broad framing.
- What it leaves open: how to preserve passivity after learning a discrete action vocabulary / how to compare token semantics under morphology and contact-frame changes

## 99. A Review of Force Myography Research and Development (2019)
- Source: Sensors; URL/DOI: https://doi.org/10.3390/s19204557
- Problem claimed: Information about limb movements can be used for monitoring physical activities or for human-machine-interface applications.
- Actual mechanism introduced: impedance/admittance regulation; variable stiffness/compliance controller
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment

## 100. Reinforcement Learning on Variable Impedance Controller for High-Precision Robotic Assembly (2019)
- Source: arXiv (Cornell University); URL/DOI: https://doi.org/10.48550/arxiv.1903.01066
- Problem claimed: Precise robotic manipulation skills are desirable in many industrial settings, reinforcement learning (RL) methods hold the promise of acquiring these skills autonomously.
- Actual mechanism introduced: impedance/admittance regulation; force or hybrid force-position control; operational-space control formulation
- Hidden assumptions: Environment stiffness remains near the training range. / Controller gains are fixed implementation details, not learnable skill variables. / Learning can ignore passivity margins without causing brittle contact behavior. / The contact frame is known or can be inferred without changing the action representation.
- Variables treated as fixed: environment stiffness; friction/contact dissipation; robot morphology
- Failure modes ignored: contact-mode shifts; energy injection / non-passive learned action; stiff or soft environment mismatch; unobserved slip or micro-contact changes
- What it makes less novel: Learning or adapting impedance parameters for robot skills is prior art.
- What it leaves open: how to compare token semantics under morphology and contact-frame changes / how to expose when a learned skill is only a replayed kinematic fragment
