"""
Debris Objects Created Over Time (1960-2024)
Figure 3: The space debris created from 1960 to 2024 from debris, payload, and rocket
Based on historical space debris accumulation data
"""

import matplotlib.pyplot as plt
import numpy as np

# Years from 1960 to 2024
years = np.arange(1960, 2025, 1)

# Simulated data based on historical trends
# Early space age (1960-1980): Slow growth
# Space race peak (1980-2000): Moderate growth
# Modern era (2000-2024): Rapid growth with major events and mega-constellations

# Generate realistic cumulative data
np.random.seed(42)

# Debris (fragments from collisions and explosions)
debris_base = np.concatenate([
    np.linspace(50, 200, 20),      # 1960-1979: Early debris
    np.linspace(200, 1500, 20),    # 1980-1999: Growing debris
    np.linspace(1500, 8500, 22),   # 2000-2021: Rapid increase (Fengyun-1C, Iridium-Cosmos)
    np.linspace(8500, 9800, 3)     # 2022-2024: Continued growth
])

# Add spikes for major events
# 2007: Fengyun-1C ASAT test
debris_base[47] += 1500  # 2007
# 2009: Iridium-Cosmos collision
debris_base[49] += 800   # 2009
# 2021: Russian ASAT test (Kosmos-1408)
debris_base[61] += 400   # 2021

# Smooth cumulative growth
debris = np.cumsum(np.diff(np.concatenate([[0], debris_base])))

# Payload (defunct satellites)
# Includes mega-constellation growth (Starlink, OneWeb, etc.)
payload_base = np.concatenate([
    np.linspace(20, 100, 20),      # 1960-1979
    np.linspace(100, 800, 20),     # 1980-1999
    np.linspace(800, 3200, 22),    # 2000-2021: Commercial satellite boom
    np.linspace(3200, 4500, 3)     # 2022-2024: Mega-constellation era (Starlink, OneWeb)
])
payload = np.cumsum(np.diff(np.concatenate([[0], payload_base])))

# Rocket bodies (spent upper stages)
rocket_base = np.concatenate([
    np.linspace(10, 80, 20),       # 1960-1979
    np.linspace(80, 500, 20),      # 1980-1999
    np.linspace(500, 2100, 22),    # 2000-2021
    np.linspace(2100, 2600, 3)     # 2022-2024: Increased launch activity
])
rocket = np.cumsum(np.diff(np.concatenate([[0], rocket_base])))

# Normalize to match realistic totals (~17,000 objects by 2024)
scale_factor = 17000 / (debris[-1] + payload[-1] + rocket[-1])
debris = debris * scale_factor
payload = payload * scale_factor
rocket = rocket * scale_factor

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Colors matching the reference image
colors = ['#4A90E2', '#F5A623', '#7ED321']  # Blue, Orange, Green

# Create stacked bar chart (using narrow bars to simulate area chart)
width = 1.0
ax.bar(years, debris, width=width, label='Debris', color=colors[0], edgecolor='none', alpha=0.9)
ax.bar(years, payload, width=width, bottom=debris, label='Payload', color=colors[1], edgecolor='none', alpha=0.9)
ax.bar(years, rocket, width=width, bottom=debris+payload, label='Rocket', color=colors[2], edgecolor='none', alpha=0.9)

# Customize the plot
ax.set_xlabel('Creation Year', fontsize=13, fontweight='bold')
ax.set_ylabel('Count', fontsize=13, fontweight='bold')
ax.set_title('Debris Objects Created', fontsize=15, fontweight='bold', pad=20)

# Set x-axis ticks
ax.set_xlim(1960, 2024)
ax.set_xticks(np.arange(1960, 2025, 10))
ax.set_xticklabels(np.arange(1960, 2025, 10), fontsize=11)

# Format y-axis
ax.set_ylim(0, 18000)
ax.set_yticks(np.arange(0, 18001, 2000))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))

# Add grid
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Add legend
ax.legend(loc='upper left', fontsize=11, framealpha=0.9, edgecolor='gray')

# Add figure caption
fig.text(0.5, 0.02, 'Figure 3. The space debris created from 1960 to 2024 from debris, payload, and rocket', 
         ha='center', fontsize=11, style='italic', wrap=True)

# Adjust layout
plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save the figure
plt.savefig('debris_objects_timeline.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: debris_objects_timeline.png")

# Display the plot
plt.show()
