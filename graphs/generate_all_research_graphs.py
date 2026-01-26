"""
Master Script to Generate All Research Paper Graphs
Generates all visualizations one by one with progress tracking
"""

import subprocess
import sys
import os
import time

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)

def print_section(text):
    """Print section divider"""
    print("\n" + "-"*70)
    print(f"  {text}")
    print("-"*70)

def run_script(script_name, description):
    """Run a single graph generation script"""
    print(f"\n[{time.strftime('%H:%M:%S')}] Generating: {description}")
    print(f"Script: {script_name}")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            check=True,
            timeout=30  # 30 second timeout per graph
        )
        
        # Print success message from script
        if "[SUCCESS]" in result.stdout:
            print(result.stdout.strip())
        
        print(f"[OK] {description} - COMPLETED")
        return True
        
    except subprocess.TimeoutExpired:
        print(f"[ERROR] {script_name} - TIMEOUT (>30s)")
        return False
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {script_name} - FAILED")
        if e.stderr:
            print(f"Error details: {e.stderr[:200]}")
        return False
    except Exception as e:
        print(f"[ERROR] {script_name} - UNEXPECTED ERROR: {str(e)}")
        return False

def main():
    """Main execution function"""
    
    print_header("SPACE DEBRIS DETECTION - COMPLETE GRAPH GENERATION")
    print(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Working Directory: {os.getcwd()}")
    
    # Define all graphs to generate
    graphs = [
        # BASIC DISTRIBUTION GRAPHS
        ("distribution_space_objects.py", "Distribution of Space Objects by Type"),
        ("spark_dataset_distribution.py", "SPARK 2022 Dataset Class Distribution"),
        ("debris_size_distribution.py", "Debris Size Distribution (Logarithmic)"),
        ("detailed_debris_distribution.py", "Detailed Debris Distribution by Size"),
        
        # TEMPORAL ANALYSIS
        ("debris_objects_timeline.py", "Debris Objects Timeline (1960-2024)"),
        
        # HEATMAP & MATRIX
        ("object_count_heatmap.py", "Object Count Heatmap (Size vs Type)"),
        
        # PROJECTIONS
        ("debris_collision_projections.py", "Debris & Collision Probability Projections"),
        
        # UNIQUE & ADVANCED GRAPHS
        ("model_performance_comparison.py", "Model Performance Radar Chart"),
        ("accuracy_vs_speed_scatter.py", "Accuracy vs Speed Trade-off Analysis"),
        ("orbital_altitude_distribution.py", "Orbital Altitude Distribution"),
        ("detection_confidence_distribution.py", "Detection Confidence Distribution"),
        ("training_metrics_evolution.py", "Training Metrics Evolution (50 Epochs)"),
    ]
    
    # Track results
    results = {}
    successful = 0
    failed = 0
    
    # Generate each graph
    print_section("GRAPH GENERATION PROGRESS")
    
    for idx, (script, description) in enumerate(graphs, 1):
        print(f"\n[{idx}/{len(graphs)}] ", end="")
        
        if os.path.exists(script):
            success = run_script(script, description)
            results[description] = success
            
            if success:
                successful += 1
            else:
                failed += 1
        else:
            print(f"[SKIP] {script} - FILE NOT FOUND")
            results[description] = False
            failed += 1
        
        # Small delay between graphs
        time.sleep(0.5)
    
    # Summary Report
    print_header("GENERATION SUMMARY")
    
    print(f"\nTotal Graphs: {len(graphs)}")
    print(f"Successful: {successful} ✓")
    print(f"Failed: {failed} ✗")
    print(f"Success Rate: {(successful/len(graphs)*100):.1f}%")
    
    # Detailed Results
    print_section("DETAILED RESULTS")
    
    for idx, (description, success) in enumerate(results.items(), 1):
        status = "[SUCCESS]" if success else "[FAILED]"
        symbol = "✓" if success else "✗"
        print(f"{idx:2d}. {symbol} {status:10s} {description}")
    
    # List Generated Files
    if successful > 0:
        print_section("GENERATED FILES")
        
        png_files = [f for f in os.listdir('.') if f.endswith('.png')]
        png_files.sort()
        
        total_size = 0
        for png_file in png_files:
            size = os.path.getsize(png_file)
            total_size += size
            size_mb = size / (1024 * 1024)
            print(f"  - {png_file:45s} ({size_mb:6.2f} MB)")
        
        print(f"\nTotal Size: {total_size / (1024 * 1024):.2f} MB")
        print(f"Total Files: {len(png_files)} PNG images")
    
    # Final Status
    print_header("COMPLETION STATUS")
    
    if failed == 0:
        print("\n  🎉 ALL GRAPHS GENERATED SUCCESSFULLY! 🎉")
        print("\n  Your research paper visualizations are ready!")
        print("  All PNG files are saved in the current directory.")
    else:
        print(f"\n  ⚠️  {failed} graph(s) failed to generate.")
        print("  Please check the error messages above.")
        print(f"  {successful} graph(s) were generated successfully.")
    
    print(f"\nEnd Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    return successful, failed

if __name__ == "__main__":
    try:
        successful, failed = main()
        
        # Exit code: 0 if all successful, 1 if any failed
        sys.exit(0 if failed == 0 else 1)
        
    except KeyboardInterrupt:
        print("\n\n[INTERRUPTED] Graph generation cancelled by user.")
        sys.exit(2)
    except Exception as e:
        print(f"\n\n[FATAL ERROR] {str(e)}")
        sys.exit(3)
