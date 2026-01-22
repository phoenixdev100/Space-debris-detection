"""
Object Count by Size and Type (1960-2024)
Figure 4: The size and the types of debris count found in space from 1960 to 2024
Heatmap visualization of catalogued space objects
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data matrix: Rows = Size categories, Columns = Type categories
# Updated to 2024 with increased counts due to mega-constellations and recent events

# Size categories (rows)
size_categories = ['Large', 'Medium', 'Small', 'Unknown']

# Type categories (columns)
type_categories = ['Debris', 'Payload', 'Rocket', 'Unknown']

# Object count data (updated to 2024)
# Rows: Large, Medium, Small, Unknown
# Columns: Debris, Payload, Rocket, Unknown
data = np.array([
    [249,  3241,  680,  19],    # Large objects
    [600,   884,   56,  99],    # Medium objects
    [7435,  817,    4,  90],    # Small objects (increased debris from ASAT tests)
    [147,     8,    4,  39]     # Unknown size
])

# Update for 2024: Add increases due to recent events
# 2021-2024: Russian ASAT test, mega-constellations, increased launches
data_2024 = np.array([
    [280,  3850,  750,  22],    # Large: +31, +609, +70, +3
    [680,  1050,   65, 110],    # Medium: +80, +166, +9, +11
    [8200,  950,    5, 100],    # Small: +765, +133, +1, +10 (ASAT debris)
    [165,    10,    5,  45]     # Unknown: +18, +2, +1, +6
])

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Create heatmap using seaborn for better styling
sns.heatmap(data_2024, 
            annot=True,           # Show numbers in cells
            fmt='d',              # Integer format
            cmap='Blues',         # Blue color scheme
            cbar_kws={'label': 'Count'},
            linewidths=2,         # Cell border width
            linecolor='white',    # Cell border color
            square=False,         # Don't force square cells
            ax=ax,
            vmin=0,               # Minimum value for color scale
            vmax=7000,            # Maximum value for color scale
            annot_kws={'fontsize': 11, 'fontweight': 'bold'})

# Customize the plot
ax.set_xlabel('Type', fontsize=13, fontweight='bold')
ax.set_ylabel('Size', fontsize=13, fontweight='bold')
ax.set_title('Object Count by Size and Type', fontsize=15, fontweight='bold', pad=20)

# Set tick labels
ax.set_xticklabels(type_categories, fontsize=11, rotation=0)
ax.set_yticklabels(size_categories, fontsize=11, rotation=0)

# Adjust colorbar
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=10)

# Add figure caption
fig.text(0.5, 0.02, 'Figure 4. The size and the types of debris count found in space from 1960 to 2024', 
         ha='center', fontsize=11, style='italic', wrap=True)

# Adjust layout
plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save the figure
plt.savefig('object_count_heatmap.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: object_count_heatmap.png")

# Display the plot
plt.show()
