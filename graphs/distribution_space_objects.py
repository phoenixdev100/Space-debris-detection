"""
Distribution of Space Objects by Type
Based on research paper data on orbital debris detection
"""

import matplotlib.pyplot as plt
import numpy as np

# Data based on ESA and NASA estimates mentioned in the paper
# Section 1.1: The Crowded Cosmos
object_types = ['Debris\n(>10cm)', 'Debris\n(1-10cm)', 'Debris\n(>1mm)', 'Active\nSatellites']
object_counts = [34000, 900000, 100000000, 8000]

# Colors matching the reference image style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create bar chart
bars = ax.bar(object_types, object_counts, color=colors, edgecolor='black', linewidth=1.2)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Customize the plot
ax.set_ylabel('Count (Objects)', fontsize=12, fontweight='bold')
ax.set_xlabel('Object Type', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Space Objects by Type', fontsize=14, fontweight='bold', pad=20)

# Format y-axis to show values in scientific notation for readability
ax.ticklabel_format(style='plain', axis='y')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))

# Add grid for better readability
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('distribution_space_objects.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: distribution_space_objects.png")

# Display the plot
plt.show()
