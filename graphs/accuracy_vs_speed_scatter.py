"""
Accuracy vs Speed Trade-off Analysis
Scatter plot showing the sweet spot of the proposed model
"""

import matplotlib.pyplot as plt
import numpy as np

# Model data from Table 3
models = {
    'YOLOv5s': {'mAP': 94.2, 'inference_time': 7.1, 'params': 7.2, 'color': '#3498db'},
    'Faster R-CNN': {'mAP': 94.2, 'inference_time': 45.3, 'params': 41.5, 'color': '#e74c3c'},
    'YOLOv8m': {'mAP': 95.5, 'inference_time': 12.8, 'params': 25.9, 'color': '#f39c12'},
    'Proposed YOLOv8': {'mAP': 97.6, 'inference_time': 13.5, 'params': 27.2, 'color': '#2ecc71'}
}

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each model
for model_name, data in models.items():
    # Size based on parameters (larger params = larger circle)
    size = (data['params'] / 50) * 1000
    
    ax.scatter(data['inference_time'], data['mAP'], 
              s=size, alpha=0.6, color=data['color'], 
              edgecolors='black', linewidth=2, label=model_name)
    
    # Add model name labels
    ax.annotate(model_name, 
               xy=(data['inference_time'], data['mAP']),
               xytext=(10, 10), textcoords='offset points',
               fontsize=11, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor=data['color'], alpha=0.3))

# Add "sweet spot" zone (high accuracy, low inference time)
sweet_spot_x = [0, 15, 15, 0, 0]
sweet_spot_y = [96, 96, 100, 100, 96]
ax.fill(sweet_spot_x, sweet_spot_y, alpha=0.1, color='green', 
        label='Optimal Zone\n(High Accuracy + Fast)')

# Add annotations for trade-offs
ax.annotate('Slow but\nAccurate', xy=(45, 94.5), fontsize=10, 
           style='italic', color='red', ha='center')
ax.annotate('Fast but\nLess Accurate', xy=(7, 93.5), fontsize=10, 
           style='italic', color='blue', ha='center')
ax.annotate('BEST:\nFast & Accurate!', xy=(13.5, 98.2), fontsize=11, 
           style='italic', color='green', ha='center', fontweight='bold')

# Customize plot
ax.set_xlabel('Inference Time (ms/image) - Lower is Better', fontsize=13, fontweight='bold')
ax.set_ylabel('mAP@0.5 (%) - Higher is Better', fontsize=13, fontweight='bold')
ax.set_title('Accuracy vs Speed Trade-off Analysis\n(Circle size = Model Parameters)', 
            fontsize=15, fontweight='bold', pad=20)

# Set limits
ax.set_xlim(0, 50)
ax.set_ylim(93, 99)

# Add grid
ax.grid(True, alpha=0.3, linestyle='--')

# Legend
ax.legend(loc='lower right', fontsize=10, framealpha=0.9)

# Add caption
fig.text(0.5, 0.02, 
         'The proposed YOLOv8+LASF achieves the best accuracy with minimal speed penalty', 
         ha='center', fontsize=11, style='italic')

plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save
plt.savefig('accuracy_vs_speed_scatter.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: accuracy_vs_speed_scatter.png")

plt.show()
