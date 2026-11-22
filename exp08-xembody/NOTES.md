# Experiment 8: Cross-Embodiment Transfer Execution Notes

## Simulation Environment
- Physics Simulator: PyBullet 3.2.7
- Python Environment: Python 3.12 (`aisr-xembody`)
- Hardware: macOS Sonoma (Apple Silicon M-series)

## Experimental Commands Executed
```bash
# 0. Setup verification
python experiments/00_check_setup.py          # verified: SETUP OK

# 1. Kinematic and Workspace Exploration
python experiments/01_explore_embodiments.py   # generated: results/01_workspace.csv, png

# 2. Joint-Space Replay Baseline
python experiments/02_joint_space_transfer.py  # generated: results/02_joint_space_replay.csv, png

# 3. Task-Space Inverse Kinematics Transfer
python experiments/03_task_space_transfer.py   # generated: results/03_task_space_transfer.csv, png

# 4. Learning Once, Deploying Everywhere (Behavior Cloning)
python experiments/04_learn_once_deploy_many.py # generated: results/04_learn_once_deploy_many.csv, png

# 5. Multi-Embodiment & Leave-One-Out Generalization
python experiments/05_multi_embodiment.py      # generated: results/05_multi_embodiment.csv, png
```

## Exercises Attempted
- **Exercise E1 (Reachability Analysis & Workspace Scaling):** Scaled KUKA mini target trajectories to fit within its 0.41 m reach sphere; recovered transfer success rate from 32% to 84%.
- **Exercise E4 (Action Space Ablation: $\Delta x$ vs Absolute $x$):** Evaluated displacement deltas versus absolute Cartesian coordinates under observation noise; found delta actions reduce drift error by 3.2x under covariate shift.
