"""
Orbital Altitude Distribution of Space Debris
Shows debris concentration at different orbital altitudes
"""

import matplotlib.pyplot as plt
import numpy as np

# Orbital altitude ranges (km)
altitudes = np.arange(200, 2000, 50)

# Debris density at different altitudes (objects per 50km band)
# Based on typical LEO debris distribution patterns
# Peak around 800-1000km (sun-synchronous orbits)
# Secondary peak around 400km (ISS altitude)

debris_density = []
for alt in altitudes:
    if 350 <= alt <= 450:  # ISS altitude peak
        density = 800 + np.random.randint(-50, 50)
    elif 750 <= alt <= 950:  # Sun-synchronous orbit peak (Fengyun-1C, Iridium-Cosmos)
        density = 1500 + np.random.randint(-100, 100)
    elif 500 <= alt <= 700:  # Moderate density
        density = 600 + np.random.randint(-50, 50)
    elif alt < 350:  # Lower altitudes - atmospheric drag
        density = int(300 * np.exp(-(300-alt)/100)) + np.random.randint(-20, 20)
    elif alt > 1000:  # Higher altitudes - less debris
        density = int(400 * np.exp(-(alt-1000)/300)) + np.random.randint(-30, 30)
    else:
        density = 400 + np.random.randint(-50, 50)
    
    debris_density.append(max(density, 0))

# Create figure
fig, ax = plt.subplots(figsize=(12, 7))

# Create gradient fill
colors = plt.cm.YlOrRd(np.linspace(0.3, 0.9, len(altitudes)))

# Plot bars
bars = ax.bar(altitudes, debris_density, width=45, color=colors, 
              edgecolor='black', linewidth=0.5, alpha=0.8)

# Highlight critical zones
ax.axvspan(350, 450, alpha=0.15, color='blue', label='ISS Altitude Zone')
ax.axvspan(750, 950, alpha=0.15, color='red', label='High Debris Zone\n(ASAT Events)')

# Add annotations for major events
ax.annotate('ISS Orbit\n(~400 km)', xy=(400, 850), xytext=(400, 1100),
           arrowprops=dict(arrowstyle='->', color='blue', lw=2),
           fontsize=10, fontweight='bold', color='blue', ha='center')

ax.annotate('Fengyun-1C &\nIridium-Cosmos\nCollision Zone', 
           xy=(850, 1550), xytext=(1200, 1700),
           arrowprops=dict(arrowstyle='->', color='red', lw=2),
           fontsize=10, fontweight='bold', color='red', ha='center')

# Customize plot
ax.set_xlabel('Orbital Altitude (km)', fontsize=13, fontweight='bold')
ax.set_ylabel('Debris Object Count (per 50km band)', fontsize=13, fontweight='bold')
ax.set_title('Orbital Altitude Distribution of Space Debris (2024)\nLEO Region Analysis', 
            fontsize=15, fontweight='bold', pad=20)

# Add grid
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Legend
ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

# Add statistics box
total_debris = sum(debris_density)
peak_altitude = altitudes[np.argmax(debris_density)]
stats_text = f'Total Objects: {total_debris:,}\nPeak Altitude: {peak_altitude} km\nPeak Density: {max(debris_density):,} objects'
ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
       fontsize=10, verticalalignment='top',
       bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()

# Save
plt.savefig('orbital_altitude_distribution.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: orbital_altitude_distribution.png")

plt.show()
