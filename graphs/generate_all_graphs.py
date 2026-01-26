"""
Generate All Graphs for Space Debris Detection Research Paper
This script runs all graph generation scripts in sequence
"""

import subprocess
import sys
import os

def run_script(script_name):
    """Run a Python script and report status"""
    print(f"\n{'='*60}")
    print(f"Running: {script_name}")
    print('='*60)
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        if result.stderr:
            print("Warnings:", result.stderr)
        print(f"[OK] {script_name} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error running {script_name}:")
        print(e.stderr)
        return False
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return False

def main():
    """Main function to generate all graphs"""
    print("\n" + "="*60)
    print("SPACE DEBRIS DETECTION - GRAPH GENERATION")
    print("="*60)
    
    # List of all graph scripts
    scripts = [
        'distribution_space_objects.py',
        'spark_dataset_distribution.py',
        'debris_size_distribution.py'
    ]
    
    # Track results
    results = {}
    
    # Run each script
    for script in scripts:
        if os.path.exists(script):
            results[script] = run_script(script)
        else:
            print(f"[ERROR] Script not found: {script}")
            results[script] = False
    
    # Summary
    print("\n" + "="*60)
    print("GENERATION SUMMARY")
    print("="*60)
    
    successful = sum(1 for v in results.values() if v)
    total = len(results)
    
    for script, success in results.items():
        status = "[SUCCESS]" if success else "[FAILED]"
        print(f"{status}: {script}")
    
    print(f"\nCompleted: {successful}/{total} graphs generated successfully")
    
    if successful == total:
        print("\n[COMPLETE] All graphs generated successfully!")
        print("\nGenerated files:")
        for script in scripts:
            output_file = script.replace('.py', '.png')
            if os.path.exists(output_file):
                size_kb = os.path.getsize(output_file) / 1024
                print(f"  - {output_file} ({size_kb:.1f} KB)")
    else:
        print("\n[WARNING] Some graphs failed to generate. Check errors above.")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
