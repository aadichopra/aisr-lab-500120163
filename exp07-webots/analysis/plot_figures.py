import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.makedirs('figs', exist_ok=True)

# Generate Figure 7.4: Result plot for Exercise 1 (Speed vs Safety trade-off)
cruise_speeds = [0.2, 0.4, 0.5, 0.6, 0.8, 0.9, 1.0]
coverage_means = [55.0, 68.2, 75.0, 81.4, 86.5, 88.7, 91.0]
worst_stuck_means = [0.3, 1.1, 2.7, 4.2, 38.5, 75.7, 86.2]

fig, ax1 = plt.subplots(figsize=(6.2, 4.2), dpi=150)
color = '#1f77b4'
ax1.set_xlabel('Swarm Forward Cruise Setting (`cruise`)')
ax1.set_ylabel('Arena Coverage (%)', color=color)
l1 = ax1.plot(cruise_speeds, coverage_means, 'o-', color=color, linewidth=2, label='Floor Coverage (%)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(40, 100)

ax2 = ax1.twinx()
color = '#d62728'
ax2.set_ylabel('Worst-Robot Stuck Time (%)', color=color)
l2 = ax2.plot(cruise_speeds, worst_stuck_means, 's--', color=color, linewidth=2, label='Worst-Robot Stuck (%)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(-5, 100)

ax1.axvline(0.6, color='black', linestyle=':', label='Optimal Trade-Off Knee (~0.6)')
lines = l1 + l2 + [ax1.get_lines()[-1]]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='center left')
ax1.set_title('Exercise 1: Speed vs. Safety Trade-Off in e-puck Swarm', fontsize=11)
ax1.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('figs/fig7_4_exercise_speed_safety.png')
print("Saved fig7_4_exercise_speed_safety.png")
