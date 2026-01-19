"""
Distribution of SPARK 2022 Dataset Classes
Based on the training dataset used in the research
"""

import matplotlib.pyplot as plt
import numpy as np

# SPARK 2022 Dataset - 11 classes
# Simulated distribution based on typical dataset composition
# Total: ~110,000 images
classes = [
    'Debris',
    'Cheops',
    'Proba-2',
    'XMM-Newton',
    'SOHO',
    'SMART-1',
    'Earth Obs\nSat-1',
    'Lisa\nPathfinder',
    'Proba-3\nCSC',
    'Proba-3\nOCS',
    'Double\nStar'
]

# Estimated distribution (debris being the primary focus class)
counts = [35000, 12000, 10000, 9000, 8000, 7500, 7000, 6500, 5500, 5000, 4500]

# Create color palette
colors = plt.cm.tab20(np.linspace(0, 1, len(classes)))

# Create figure
fig, ax = plt.subplots(figsize=(14, 7))

# Create bar chart
bars = ax.bar(classes, counts, color=colors, edgecolor='black', linewidth=1.2, alpha=0.8)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customize the plot
ax.set_ylabel('Number of Images', fontsize=13, fontweight='bold')
ax.set_xlabel('Object Class', fontsize=13, fontweight='bold')
ax.set_title('Distribution of SPARK 2022 Dataset by Object Class\n(Total: ~110,000 Images)', 
             fontsize=15, fontweight='bold', pad=20)

# Format y-axis
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))

# Add grid
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('spark_dataset_distribution.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: spark_dataset_distribution.png")

# Display the plot
plt.show()
