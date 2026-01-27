"""
Detailed Distribution of Space Debris by Size
Figure 1: Space debris distribution with their sizes
Based on ESA and NASA orbital debris estimates
"""

import matplotlib.pyplot as plt
import numpy as np

# Data based on research paper Section 1.1
# Three main size categories for tracked/catalogued debris
debris_categories = [
    'Objects (Larger than 10 cm)',
    'Fragments (1 cm to 10 cm)', 
    'Particles (1 mm to 1 cm)'
]

# Counts from ESA and NASA estimates
debris_counts = [
    34000,      # ~34,000 objects larger than 10 cm (catalogued)
    900000,     # ~900,000 objects between 1 cm and 10 cm
    100000000   # >100 million particles between 1 mm and 1 cm
]

# Simplified version for better visualization (using thousands)
debris_counts_display = [34, 900, 100000]  # in thousands

# Colors matching the reference image
colors = ['#0000FF', '#FFA500', '#008000']  # Blue, Orange, Green

# Create figure with specific size
fig, ax = plt.subplots(figsize=(11, 7))

# Create bar chart
x_pos = np.arange(len(debris_categories))
bars = ax.bar(x_pos, debris_counts_display, color=colors, 
              edgecolor='black', linewidth=1.8, width=0.6, alpha=0.9)

# Add value labels on top of bars
for i, (bar, count) in enumerate(zip(bars, debris_counts_display)):
    height = bar.get_height()
    # Format the label
    if count >= 1000:
        label = f'{int(count)}'
    else:
        label = f'{int(count)}'
    
    ax.text(bar.get_x() + bar.get_width()/2., height + max(debris_counts_display)*0.02,
            label,
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize the plot
ax.set_ylabel('Number (Thousands)', fontsize=13, fontweight='bold')
ax.set_xlabel('Debris Size Category', fontsize=13, fontweight='bold')
ax.set_title('Distribution of Space Debris by Size', fontsize=15, fontweight='bold', pad=20)

# Set x-axis labels
ax.set_xticks(x_pos)
ax.set_xticklabels(debris_categories, fontsize=11)

# Format y-axis
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))

# Add grid for better readability
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Set y-axis limits for better visualization
ax.set_ylim(0, max(debris_counts_display) * 1.15)

# Add figure caption
fig.text(0.5, 0.02, 'Figure 1. Space debris distribution with their sizes', 
         ha='center', fontsize=12, style='italic', fontweight='normal')

# Adjust layout to accommodate caption
plt.tight_layout(rect=[0, 0.03, 1, 1])

# Save the figure
plt.savefig('detailed_debris_distribution.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: detailed_debris_distribution.png")

# Display the plot
plt.show()
