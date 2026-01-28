"""
Debris Population and Collision Probabilities Over Time
Figure 5: The debris population and collision probabilities over time
Projections showing different mitigation scenarios
"""

import matplotlib.pyplot as plt
import numpy as np

# Time span: 0 to 50 years from present (2024-2074)
years = np.arange(0, 51, 1)

# ============= LEFT PANEL: Debris Population Over Time =============

# Scenario 1: No Mitigation (worst case - exponential growth)
no_mitigation_debris = 1000 + 100 * years + 2 * years**1.5

# Scenario 2: Active Removal (Low) - moderate growth with some removal
active_removal_low = 1000 + 70 * years + 0.5 * years**1.3

# Scenario 3: Active Removal (High) - controlled growth with aggressive removal
active_removal_high = 1000 + 40 * years + 0.2 * years**1.1

# Scenario 4: Passive Growth - natural decay, slow growth
passive_growth = 1000 + 20 * years + 0.1 * years**1.05

# Scenario 5: Combined Approach - best case with multiple strategies
combined_approach = 1000 - 5 * years + 0.05 * years**0.9

# ============= RIGHT PANEL: Collision Probabilities Over Time =============

# Collision probability (scaled to show realistic trends)
# Higher debris = higher collision probability

# No Mitigation - exponential increase in collision risk
no_mitigation_collision = 1.0 + 0.3 * years + 0.01 * years**1.6

# Active Removal (Low) - moderate collision risk
active_removal_low_collision = 1.0 + 0.15 * years + 0.003 * years**1.4

# Active Removal (High) - controlled collision risk
active_removal_high_collision = 1.0 + 0.08 * years + 0.001 * years**1.2

# Passive Growth - slow increase in collision risk
passive_growth_collision = 1.0 + 0.04 * years + 0.0005 * years**1.1

# Combined Approach - minimal collision risk
combined_approach_collision = 1.0 - 0.01 * years + 0.0001 * years**0.8

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ============= LEFT SUBPLOT: Debris Population =============

# Plot lines
ax1.plot(years, no_mitigation_debris, label='No Mitigation', 
         color='#5B9BD5', linewidth=2, linestyle='-')
ax1.plot(years, active_removal_low, label='Active Removal (Low)', 
         color='#ED7D31', linewidth=2, linestyle='-')
ax1.plot(years, active_removal_high, label='Active Removal (High)', 
         color='#A5A5A5', linewidth=2, linestyle='-')
ax1.plot(years, passive_growth, label='Passive Growth', 
         color='#70AD47', linewidth=2, linestyle='-')
ax1.plot(years, combined_approach, label='Combined Approach', 
         color='#9E9E9E', linewidth=2, linestyle='--')

# Customize left subplot
ax1.set_xlabel('Years', fontsize=11, fontweight='bold')
ax1.set_ylabel('Number of Objects (>10 cm)', fontsize=11, fontweight='bold')
ax1.set_title('Debris Population Over Time', fontsize=13, fontweight='bold', pad=15)
ax1.legend(loc='upper left', fontsize=9, framealpha=0.9)
ax1.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 7000)

# ============= RIGHT SUBPLOT: Collision Probabilities =============

# Plot lines
ax2.plot(years, no_mitigation_collision, label='No Mitigation', 
         color='#5B9BD5', linewidth=2, linestyle='-')
ax2.plot(years, active_removal_low_collision, label='Active Removal (Low)', 
         color='#ED7D31', linewidth=2, linestyle='-')
ax2.plot(years, active_removal_high_collision, label='Active Removal (High)', 
         color='#A5A5A5', linewidth=2, linestyle='-')
ax2.plot(years, passive_growth_collision, label='Passive Growth', 
         color='#70AD47', linewidth=2, linestyle='-')
ax2.plot(years, combined_approach_collision, label='Combined Approach', 
         color='#9E9E9E', linewidth=2, linestyle='--')

# Customize right subplot
ax2.set_xlabel('Years', fontsize=11, fontweight='bold')
ax2.set_ylabel('Collision Probability', fontsize=11, fontweight='bold')
ax2.set_title('Collision Probabilities Over Time', fontsize=13, fontweight='bold', pad=15)
ax2.legend(loc='upper left', fontsize=9, framealpha=0.9)
ax2.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax2.set_xlim(0, 50)
ax2.set_ylim(0, 18)

# Add figure caption
fig.text(0.5, 0.02, 'Figure 5. The debris population and collision probabilities over time', 
         ha='center', fontsize=12, style='italic')

# Adjust layout
plt.tight_layout(rect=[0, 0.05, 1, 1])

# Save the figure
plt.savefig('debris_collision_projections.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: debris_collision_projections.png")

# Display the plot
plt.show()
