# Space Debris Detection - Graph Scripts

This folder contains Python scripts to generate visualizations for the research paper on space debris detection using YOLOv8.

## Available Scripts

### 1. `distribution_space_objects.py`
**Description:** Shows the distribution of all space objects including debris of different sizes and active satellites.
- **Data Source:** ESA and NASA estimates from Section 1.1
- **Categories:** Large debris (>10cm), Medium debris (1-10cm), Small debris (>1mm), Active satellites

### 2. `spark_dataset_distribution.py`
**Description:** Visualizes the class distribution in the SPARK 2022 dataset used for training.
- **Data Source:** SPARK 2022 Dataset (Table 1)
- **Categories:** 11 classes (10 spacecraft + debris)
- **Total Images:** ~110,000

### 3. `debris_size_distribution.py`
**Description:** Focuses specifically on debris size categories with logarithmic scale.
- **Data Source:** ESA and NASA estimates
- **Categories:** 4 size categories from large (>10cm) to micro (<1mm)
- **Special Feature:** Logarithmic scale for better visualization of wide range

## How to Run

### Prerequisites
```bash
pip install matplotlib numpy
```

### Running a Script
```bash
# Navigate to the graphs folder
cd graphs

# Run any script
python distribution_space_objects.py
python spark_dataset_distribution.py
python debris_size_distribution.py
```

### Output
- All graphs are saved as high-resolution PNG files (300 DPI)
- Files are saved in the `graphs/` folder
- Graphs also display in a window when script runs

## Generated Files
- `distribution_space_objects.png`
- `spark_dataset_distribution.png`
- `debris_size_distribution.png`

## Customization
You can modify the scripts to:
- Change colors by editing the `colors` variable
- Adjust figure size in `figsize=(width, height)`
- Modify DPI in `savefig()` for different resolution
- Update data values to match your specific requirements

## Notes
- All data is based on the research paper content
- Graphs follow the style of Figure 2 from the reference material
- Scripts use matplotlib for professional publication-quality output
