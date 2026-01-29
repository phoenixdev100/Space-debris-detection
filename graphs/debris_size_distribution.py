"""
Distribution of Space Debris by Size Category
Based on ESA and NASA estimates from Section 1.1 of the research paper
"""

import matplotlib.pyplot as plt
import numpy as np

# Data from the paper: Section 1.1 - The Crowded Cosmos
# ESA and NASA estimates of debris population
debris_categories = [
    'Large Debris\n(>10 cm)',
    'Medium Debris\n(1-10 cm)', 
    'Small Debris\n(1-10 mm)',
    'Micro Debris\n(<1 mm)'
]

# Counts from the paper
debris_counts = [
    34000,      # ~34,000 objects larger than 10 cm
    900000,     # ~900,000 objects between 1 cm and 10 cm
    100000000,  # >100 million particles larger than 1 mm
    500000000   # Estimated micro debris
]

# Colors similar to the reference image
colors = ['#3498db', '#e67e22', '#2ecc71', '#e74c3c']

# Create figure with larger size for better visibility
fig, ax = plt.subplots(figsize=(12, 7))

# Create bar chart
bars = ax.bar(debris_categories, debris_counts, color=colors, 
              edgecolor='black', linewidth=1.5, alpha=0.85)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    # Format large numbers
    if height >= 1000000:
        label = f'{height/1000000:.0f}M'
    elif height >= 1000:
        label = f'{height/1000:.0f}K'
    else:
        label = f'{int(height):,}'
    
    ax.text(bar.get_x() + bar.get_width()/2., height,
            label,
            ha='center', va='bottom', fontsize=12, fontweight='bold')

# Customize the plot
ax.set_ylabel('Count (Objects)', fontsize=13, fontweight='bold')
ax.set_xlabel('Debris Size Category', fontsize=13, fontweight='bold')
ax.set_title('Distribution of Space Debris by Size Category\n(ESA & NASA Estimates)', 
             fontsize=15, fontweight='bold', pad=20)

# Use logarithmic scale for y-axis due to large range
ax.set_yscale('log')

# Format y-axis
def format_func(value, tick_number):
    if value >= 1e9:
        return f'{value/1e9:.0f}B'
    elif value >= 1e6:
        return f'{value/1e6:.0f}M'
    elif value >= 1e3:
        return f'{value/1e3:.0f}K'
    else:
        return f'{int(value)}'

ax.yaxis.set_major_formatter(plt.FuncFormatter(format_func))

# Add grid
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5, which='both')
ax.set_axisbelow(True)

# Add annotation about total mass
ax.text(0.98, 0.97, 'Total Mass: >9,000 metric tons', 
        transform=ax.transAxes, fontsize=10, 
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('debris_size_distribution.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: debris_size_distribution.png")

# Display the plot
plt.show()
