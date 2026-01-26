"""
Generate All Unique Graphs for Research Paper
Runs all unique visualization scripts
"""

import subprocess
import sys

scripts = [
    'model_performance_comparison.py',
    'accuracy_vs_speed_scatter.py',
    'orbital_altitude_distribution.py',
    'detection_confidence_distribution.py',
    'training_metrics_evolution.py'
]

print("="*60)
print("GENERATING UNIQUE RESEARCH GRAPHS")
print("="*60)

for script in scripts:
    print(f"\nRunning: {script}")
    try:
        result = subprocess.run([sys.executable, script], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

print("\n" + "="*60)
print("ALL UNIQUE GRAPHS GENERATED!")
print("="*60)
