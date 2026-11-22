# CSAI4014: Algorithms for Intelligent Systems and Robotics — Laboratory Repository

**Academic Year:** 2026–2027 (Autumn Semester)  
**Program:** B.Tech Computer Science and Engineering (AI & ML), Semester VII  
**Institution:** School of Computer Science, University of Petroleum and Energy Studies (UPES), Dehradun  
**Course Teacher:** Dr. Resham Raj Shivwanshi  

---

## Student Details
- **Name:** Aadi Chopra
- **SAP ID:** 500120163
- **Roll No.:** R2142231902
- **Batch / Cohort:** B2 AIML (Batch B)
- **Partner Details:** Solo submission (self: Aadi Chopra, SAP ID: 500120163)
- **Repository URL:** [https://github.com/aadichopra/aisr-lab-500120163](https://github.com/aadichopra/aisr-lab-500120163)

---

## Repository Layout
```text
aisr-lab-500120163/
├── README.md                          # Repository overview, author info, environment & citations
├── exp01-signals/                     # Exp 1: Time and Frequency Domain, and the Pendulum
│   ├── exp01.ipynb                    # Executable Jupyter notebook
│   └── figs/                          # Figures 1.1 to 1.5 (signals, spectra, aliasing, phase portraits)
├── exp02-queens/                      # Exp 2: The Eight Queens Problem (Backtracking vs Permutations)
│   ├── exp02.ipynb                    # CSP formulation, solver benchmarks (n=4 to 10)
│   └── figs/                          # Figures 2.1 (8x8 board) and 2.2 (runtime log curve)
├── exp03-search/                      # Exp 3: Breadth-First and Depth-First Search
│   ├── exp03.ipynb                    # Grid maze traversal, frontier tracking, path validation
│   └── figs/                          # Figures 3.1 (maze paths) and 3.2 (frontier size evolution)
├── exp04-hillclimb/                   # Exp 4: Hill Climbing and Local Optima
│   ├── exp04.ipynb                    # Plain hill climbing, random restarts, success probability
│   └── figs/                          # Figures 4.1 (landscape trajectories) and 4.2 (success vs restarts)
├── exp05-rl/                          # Exp 5: Tabular Q-Learning in Gridworld
│   ├── exp05.ipynb                    # MDP formulation, epsilon-greedy exploration evaluation
│   └── figs/                          # Figures 5.1 (learning curves) and 5.2 (extracted policy grid)
├── exp06-neural/                      # Exp 6: Simple Two-Layer Neural Network (NumPy XOR)
│   ├── exp06.ipynb                    # Forward propagation, analytical backpropagation, learning rate sweep
│   └── figs/                          # Figures 6.1 (loss curves) and 6.2 (decision boundary)
├── exp07-webots/                      # Exp 7: Mobile Robot Simulation in Webots (Swarm & Lidar)
│   ├── controllers/                   # e-puck Braitenberg vehicle & Pioneer 3-DX lidar controllers
│   ├── runs/                          # Trajectory logs (.csv) for swarm and Pioneer parameter sweeps
│   ├── figs/                          # Figures 7.1 to 7.4 (arena, swarm tracks, lidar path, speed-safety)
│   └── NOTES.md                       # Simulation commands, parameter configurations, and observations
└── exp08-xembody/                     # Exp 8: Cross-Embodiment Manipulation Transfer (PyBullet)
    ├── results/                       # Experimental CSV metrics and result plots (01 to 05)
    ├── figs/                          # Figures 8.1 to 8.5 (workspace, joint replay, task transfer, BC)
    ├── exercises/                     # Exercise analysis (workspace scaling E1, action space ablation E4)
    └── NOTES.md                       # Setup instructions, simulation commands, and question answers
```

---

## Computational Environment
- **Operating System:** macOS Sonoma 14.x (Apple Silicon M-series ARM64)
- **Primary Languages:** Python 3.11 / 3.12
- **Core Scientific Libraries:** NumPy 2.0.1, SciPy 1.18.1, Matplotlib 3.11.2, collections
- **Simulators:** 
  - Cyberbotics Webots R2025a (Mobile robot kinematics, distance sensors, SICK lidar)
  - PyBullet 3.2.7 (Rigid body physics, 6-DOF and 7-DOF manipulator kinematics)

---

## References and Sources
1. A. V. Oppenheim and R. W. Schafer, *Discrete-Time Signal Processing*, 3rd ed. Upper Saddle River, NJ, USA: Pearson, 2010.
2. K. J. Åström and R. M. Murray, *Feedback Systems: An Introduction for Scientists and Engineers*. Princeton, NJ, USA: Princeton Univ. Press, 2008.
3. S. Russell and P. Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed. Hoboken, NJ, USA: Pearson, 2020.
4. R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed. Cambridge, MA, USA: MIT Press, 2018.
5. O. Michel, "Webots: Professional mobile robot simulation," *Int. J. Adv. Robotic Systems*, vol. 1, no. 1, pp. 39–42, 2004.
6. Open X-Embodiment Collaboration, "Open X-Embodiment: Robotic learning datasets and RT-X models," in *Proc. IEEE ICRA*, 2024.
7. E. Coumans and Y. Bai, "PyBullet, a Python module for physics simulation for games, robotics and machine learning," 2016–2024. [Online]. Available: http://pybullet.org
8. Course Laboratory Manual and Experiment Repositories:
   - AISR Lab Manual, Chapters 1–7 (CSAI4014, UPES Dehradun).
   - Webots Robotics Sim: `https://github.com/reshamrajs/webots-robotics-sim`
   - AISR Cross-Embodiment Transfer PyBullet repository.

---

## Academic Integrity & Use of AI Assistants
In accordance with UPES academic policies and the CSAI4014 laboratory guidelines:
- All simulation runs, benchmark timings, and mathematical calculations were independently executed and recorded by me.
- AI assistants (Gemini / Claude Code) were consulted for debugging code structure, syntax verification, and formatting report styling. All derived mathematical formulations, code logic, and analysis statements are thoroughly understood and can be defended and modified during the viva examination.
