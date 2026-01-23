"""
Model Performance Comparison - Radar Chart
Unique visualization comparing YOLOv8 variants and baseline models
across multiple performance metrics
"""

import matplotlib.pyplot as plt
import numpy as np

# Models to compare
models = ['YOLOv5s', 'Faster R-CNN', 'YOLOv8m\n(Baseline)', 'Proposed\nYOLOv8+LASF']

# Performance metrics (normalized to 0-100 scale)
metrics = ['mAP@0.5', 'mAP@0.5:0.95', 'Precision', 'Recall', 'Speed\n(FPS)', 'Efficiency']

# Data from your research paper (Table 3)
# Speed converted to FPS (1000ms / inference_time)
# Efficiency = (mAP@0.5 * 100) / Parameters
data = {
    'YOLOv5s': [94.2, 83.7, 94.1, 91.5, 1000/7.1, (94.2*100)/7.2],
    'Faster R-CNN': [94.2, 85.9, 93.5, 92.8, 1000/45.3, (94.2*100)/41.5],
    'YOLOv8m\n(Baseline)': [95.5, 86.2, 95.8, 93.1, 1000/12.8, (95.5*100)/25.9],
    'Proposed\nYOLOv8+LASF': [97.6, 90.3, 97.6, 95.4, 1000/13.5, (97.6*100)/27.2]
}

# Normalize all metrics to 0-100 scale
normalized_data = {}
for model in models:
    normalized_data[model] = [
        data[model][0],  # mAP@0.5 already 0-100
        data[model][1],  # mAP@0.5:0.95 already 0-100
        data[model][2],  # Precision already 0-100
        data[model][3],  # Recall already 0-100
        (data[model][4] / 140) * 100,  # Speed normalized (140 FPS max)
        (data[model][5] / 400) * 100   # Efficiency normalized
    ]

# Create radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

# Number of variables
num_vars = len(metrics)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

# Colors for each model
colors = ['#3498db', '#e74c3c', '#f39c12', '#2ecc71']

# Plot each model
for idx, model in enumerate(models):
    values = normalized_data[model]
    values += values[:1]  # Complete the circle
    
    ax.plot(angles, values, 'o-', linewidth=2, label=model, color=colors[idx])
    ax.fill(angles, values, alpha=0.15, color=colors[idx])

# Fix axis to go in the right order and start at 12 o'clock
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw axis lines for each angle and label
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics, fontsize=11, fontweight='bold')

# Set y-axis limits
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=9)

# Add grid
ax.grid(True, linestyle='--', alpha=0.7)

# Add title and legend
plt.title('Model Performance Comparison\n(Multi-Metric Radar Chart)', 
          fontsize=15, fontweight='bold', pad=30)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Save
plt.savefig('model_performance_comparison.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: model_performance_comparison.png")

plt.show()
