# Experiment 7: Webots Simulation Execution Notes

## Environment Setup
- Simulator: Cyberbotics Webots R2025a
- Controller Runtime: Python 3.12 (Apple Silicon M-series macOS)
- Robot Models: 5x e-puck differential-drive robots (Swarm), 1x Pioneer 3-DX with SICK LMS 291 Lidar

## Commands Executed

### Part A: e-puck Reactive Swarm (120 s)
```bash
# Baseline default run (cruise=0.5, gain=4.0)
python3 tools/run_experiment.py swarm --seconds 120

# Aggressive cruise speed sweep (testing speed-safety limits)
python3 tools/run_experiment.py swarm --seconds 120 --set cruise=0.9
python3 tools/run_experiment.py swarm --seconds 120 --set cruise=0.2

# Sensor gain modifications
python3 tools/run_experiment.py swarm --seconds 120 --set gain=1.0
python3 tools/run_experiment.py swarm --seconds 120 --set gain=10.0
```

### Part B: Pioneer 3-DX Lidar Navigation (180 s)
```bash
# Baseline Follow-The-Gap navigation (bubble=0.45m)
python3 tools/run_experiment.py pioneer --seconds 180

# Safety bubble parameter sweep
python3 tools/run_experiment.py pioneer --seconds 180 --set bubble=0.15
python3 tools/run_experiment.py pioneer --seconds 180 --set bubble=0.90
```

### Analysis & Metrics Extraction
```bash
python3 analysis/metrics.py analysis/trajectories.csv swarm
python3 analysis/metrics.py analysis/runs/pioneer_default.csv pioneer
python3 analysis/plot_trajectories.py
```
