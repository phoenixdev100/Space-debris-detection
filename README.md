<h1 align="center">🛰️ Space Debris Detection System</h1>

A Python-based computer vision system for detecting and tracking space debris using OpenCV and YOLOv8. This project simulates real-time space debris detection with advanced tracking algorithms, visualization, and comprehensive analytics.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Project Structure](#project-structure)
- [Detection Categories](#detection-categories)
- [Visualization & Analytics](#visualization--analytics)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)


## 🌟 Overview

This project implements a sophisticated space debris detection system that processes video footage to identify, track, and categorize various types of space debris. Using computer vision techniques and deep learning models, it provides real-time detection with color-coded visualization based on debris size and threat level.

### Key Capabilities

- **Real-time Detection**: Process video frames to detect debris objects
- **Multi-category Classification**: Identify debris from large rocket stages to micro particles
- **Advanced Tracking**: Frame-to-frame particle association with trajectory prediction
- **Comprehensive Analytics**: Generate research-quality graphs and statistics
- **Adaptive Thresholding**: Dynamic confidence adjustment for optimal detection

## ✨ Features

### Detection & Tracking
- ✅ YOLOv8-based object detection (with fallback simulation mode)
- ✅ Spatial partitioning grid for efficient particle queries
- ✅ Particle trajectory tracking with motion prediction
- ✅ Adaptive confidence thresholding
- ✅ Color-coded bounding boxes by debris size

### Visualization
- ✅ Real-time video processing with annotated output
- ✅ Particle trails showing movement history
- ✅ On-screen legend and statistics
- ✅ Size-specific formatting (box thickness, text size)

### Analytics & Research
- ✅ 12+ research-quality graph generators
- ✅ Distribution analysis (size, altitude, confidence)
- ✅ Model performance comparisons
- ✅ Collision projection modeling
- ✅ Training metrics evolution

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-capable GPU for YOLOv8 acceleration

### Step 1: Clone the Repository

```bash
git clone https://github.com/phoenixdev100/Space-debris-detection.git
cd Space-debris-detection
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python src/spaceDebrisDetection.py --help
```

## 💻 Usage

### Basic Detection

Run the debris detection on the sample video:

```bash
python src/spaceDebrisDetection.py
```

Press **'q'** to quit the video playback.

### Generate Analytics Graphs

Generate all research graphs:

```bash
cd graphs
python generate_all_graphs.py
```

Generate specific graphs:

```bash
python graphs/debris_size_distribution.py
python graphs/orbital_altitude_distribution.py
python graphs/model_performance_comparison.py
```

### Custom Video Input

Process your own video file:

```bash
python src/spaceDebrisDetection.py --input path/to/your/video.mp4
```

## � Documentation

Complete documentation is available in the `docs/` directory:

### Getting Started
- **[Installation Guide](docs/INSTALLATION.md)** - Detailed installation instructions for all platforms
- **[Quick Start](docs/QUICK_START.md)** - Get up and running in 5 minutes
- **[Quick Reference](QUICK_REFERENCE.md)** - Command cheat sheet and quick navigation

### User Guides
- **[Usage Guide](docs/USAGE.md)** - Complete usage instructions and examples
- **[FAQ](docs/FAQ.md)** - Frequently asked questions and troubleshooting
- **[Enhancements](docs/ENHANCEMENTS.md)** - Feature enhancements and detection categories

### Technical Documentation
- **[API Reference](docs/API_REFERENCE.md)** - Complete API documentation for developers
- **[Project Structure](docs/PROJECT_STRUCTURE.md)** - Detailed project organization
- **[Graph Summary](docs/GRAPH_SUMMARY.md)** - Documentation for all visualization graphs

### Development
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute to the project
- **[Changelog](CHANGELOG.md)** - Version history and changes
- **[Documentation Index](docs/INDEX.md)** - Complete documentation index

**💡 Tip**: Start with the [Quick Start Guide](docs/QUICK_START.md) if you're new to the project!

## �📁 Project Structure

```
Space-debris-detection/
│
├── src/                          # Source code
│   └── spaceDebrisDetection.py   # Main detection script
│
├── assets/                       # Input data
│   └── debris.mp4                # Sample debris video
│
├── graphs/                       # Graph generation scripts
│   ├── generate_all_graphs.py    # Generate all graphs
│   ├── debris_size_distribution.py
│   ├── orbital_altitude_distribution.py
│   ├── model_performance_comparison.py
│   ├── training_metrics_evolution.py
│   └── ... (12+ graph scripts)
│
├── output/                       # Generated outputs
│   ├── graphs/                   # Generated graph images
│   └── videos/                   # Processed video outputs
│
├── docs/                         # Documentation
│   ├── ENHANCEMENTS.md           # Feature enhancements
│   └── GRAPH_SUMMARY.md          # Graph documentation
│
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── LICENSE                       # MIT License
└── README.md                     # This file
```

## 🎯 Detection Categories

The system categorizes detected objects into multiple classes:

### 🔴 Large Debris (RED boxes, thick borders)
- Large Debris Panel - Solar panels, large structural components
- Large Satellite Fragment - Major pieces from destroyed satellites
- Large Rocket Stage - Spent rocket boosters and stages

### 🟠 Medium Debris (ORANGE boxes)
- Medium Debris Fragment - Mid-sized structural pieces
- Medium Antenna Piece - Communication equipment fragments
- Medium Solar Panel Fragment - Broken solar panel sections

### 🟢 Small Debris (GREEN boxes)
- Small Bolt/Screw - Hardware components
- Small Paint Fleck - Paint chips from spacecraft
- Small Wire Fragment - Electrical wiring pieces
- Small Insulation - Thermal protection fragments

### 🟢 Micro Debris (GREEN boxes, smaller text)
- Micro Fragment - Tiny debris particles
- Micro Particle - Very small debris pieces
- Micro Debris - Microscopic space junk

### 🔵 Active Objects (BLUE boxes)
- Active Satellite - Functioning satellites
- Communication Satellite - Active communication equipment

## 📊 Visualization & Analytics

### Available Graphs

1. **Distribution of Space Objects** - Overview of all tracked objects
2. **Debris Size Distribution** - Logarithmic scale size categories
3. **Orbital Altitude Distribution** - Altitude-based debris distribution
4. **Detection Confidence Distribution** - Confidence score analysis
5. **Model Performance Comparison** - YOLOv8 vs other models
6. **Training Metrics Evolution** - Loss and accuracy over epochs
7. **Accuracy vs Speed Scatter** - Performance trade-offs
8. **Debris Collision Projections** - Future collision predictions
9. **Object Count Heatmap** - Spatial density visualization
10. **Debris Objects Timeline** - Historical trends
11. **Detailed Debris Distribution** - Category breakdown
12. **SPARK Dataset Distribution** - Training data composition

All graphs are generated at 300 DPI for publication quality.

## 🔧 Technical Details

### Core Technologies

- **OpenCV**: Video processing and computer vision
- **NumPy**: Numerical computations and array operations
- **Matplotlib**: Graph generation and visualization
- **Ultralytics YOLOv8**: Deep learning object detection (optional)

### Key Algorithms

1. **Color-based Masking**: HSV color space filtering for debris detection
2. **Morphological Operations**: Opening and closing for noise reduction
3. **Contour Detection**: Boundary identification for debris objects
4. **Spatial Partitioning**: Grid-based efficient particle queries
5. **Particle Tracking**: Frame-to-frame association with Hungarian algorithm
6. **Adaptive Thresholding**: Dynamic confidence adjustment

### Performance Optimizations

- Spatial grid partitioning for O(1) neighbor queries
- Efficient contour detection with area filtering
- Frame-to-frame tracking to reduce false positives
- Adaptive thresholding based on detection history

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions and classes
- Include unit tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **ESA and NASA** for space debris statistics and research data
- **SPARK 2022 Dataset** for training data
- **Ultralytics** for the YOLOv8 implementation
- **OpenCV Community** for computer vision tools

## 📧 Contact

For questions, suggestions, or collaboration:

- **GitHub**: [@phoenixdev100](https://github.com/phoenixdev100)
- **Repository**: [Space-debris-detection](https://github.com/phoenixdev100/Space-debris-detection)

## 🔮 Future Enhancements

- [ ] Real-time video stream processing
- [ ] 3D trajectory visualization
- [ ] Multi-camera fusion
- [ ] Deep learning model fine-tuning
- [ ] Web-based dashboard
- [ ] API for integration with other systems
- [ ] Mobile app for field deployment

---

**Made with ❤️ for space debris research and planetary protection**
