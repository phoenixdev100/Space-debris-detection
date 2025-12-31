# Quick Reference Guide

## 📁 Directory Structure at a Glance

```
Space-debris-detection/
│
├── 📄 README.md              ← Start here! Main documentation
├── 📄 LICENSE                ← MIT License
├── 📄 CONTRIBUTING.md        ← How to contribute
├── 📄 CHANGELOG.md           ← Version history
├── 📄 requirements.txt       ← Install dependencies
├── 📄 RESTRUCTURING_SUMMARY.md ← This restructuring summary
├── 🔧 .gitignore             ← Git ignore rules
│
├── 📂 src/                   ← SOURCE CODE
│   └── spaceDebrisDetection.py (Main detection script - 705 lines)
│
├── 📂 assets/                ← INPUT DATA
│   └── debris.mp4 (17.5 MB sample video)
│
├── 📂 graphs/                ← GRAPH SCRIPTS (18 files)
│   ├── config.py             ← Path configuration
│   ├── update_graph_paths.py ← Utility script
│   ├── README.md             ← Graph documentation
│   └── *.py                  ← 15 graph generation scripts
│
├── 📂 output/                ← GENERATED OUTPUTS (gitignored)
│   ├── graphs/               ← Generated graph images
│   │   └── legacy/           ← Archived old graphs
│   └── videos/               ← Processed videos
│
├── 📂 docs/                  ← DOCUMENTATION (5 files)
│   ├── PROJECT_STRUCTURE.md  ← Detailed structure
│   ├── ENHANCEMENTS.md       ← Feature enhancements
│   ├── GRAPH_SUMMARY.md      ← Graph documentation
│   ├── QUICK_START.md        ← Quick start guide
│   └── UNIQUE_GRAPHS_GUIDE.md ← Unique graphs
│
└── 📂 venv/                  ← Virtual environment (gitignored)
```

---

## 🚀 Common Commands

### Setup
```bash
# Clone repository
git clone https://github.com/phoenixdev100/Space-debris-detection.git
cd Space-debris-detection

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run Detection
```bash
# Run main detection script
python src/spaceDebrisDetection.py

# Press 'q' to quit video playback
```

### Generate Graphs
```bash
# Navigate to graphs directory
cd graphs

# Generate all graphs
python generate_all_graphs.py

# Generate specific graph
python debris_size_distribution.py

# Outputs saved to: ../output/graphs/
```

---

## 📊 File Inventory

### Root Level (7 files)
| File | Size | Purpose |
|------|------|---------|
| README.md | 9.32 KB | Main documentation |
| CONTRIBUTING.md | 6.67 KB | Contribution guide |
| CHANGELOG.md | 6.13 KB | Version history |
| RESTRUCTURING_SUMMARY.md | 9.69 KB | Restructuring details |
| LICENSE | 1.08 KB | MIT License |
| requirements.txt | 0.32 KB | Dependencies |
| .gitignore | 0.74 KB | Git exclusions |

### Directories
| Directory | Files | Subdirs | Purpose |
|-----------|-------|---------|---------|
| src/ | 1 | 0 | Source code |
| assets/ | 1 | 0 | Input data |
| graphs/ | 18 | 0 | Graph scripts |
| output/ | 0 | 2 | Generated outputs |
| docs/ | 5 | 0 | Documentation |
| venv/ | Many | Many | Python packages |

---

## 🎯 Quick Navigation

### Need to...
- **Get started?** → Read `README.md`
- **Install?** → Use `requirements.txt`
- **Contribute?** → Read `CONTRIBUTING.md`
- **See changes?** → Check `CHANGELOG.md`
- **Understand structure?** → See `docs/PROJECT_STRUCTURE.md`
- **Run detection?** → Execute `src/spaceDebrisDetection.py`
- **Generate graphs?** → Run scripts in `graphs/`
- **View outputs?** → Check `output/graphs/`

---

## 📝 Key Features

### Detection System
- ✅ YOLOv8-based object detection
- ✅ Real-time video processing
- ✅ Multi-category classification
- ✅ Adaptive thresholding
- ✅ Particle tracking

### Visualization
- ✅ 15 graph generation scripts
- ✅ Research-quality outputs (300 DPI)
- ✅ Multiple visualization types
- ✅ Automated generation

### Documentation
- ✅ Comprehensive README
- ✅ API documentation
- ✅ Contribution guidelines
- ✅ Project structure docs
- ✅ Quick start guide

---

## 🔍 Important Paths

```bash
# Main script
src/spaceDebrisDetection.py

# Sample video
assets/debris.mp4

# Graph outputs
output/graphs/*.png

# Documentation
docs/*.md

# Configuration
graphs/config.py
requirements.txt
```

---

## ⚙️ Configuration

### Python Dependencies
- opencv-python >= 4.8.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- Pillow >= 10.0.0

### Optional (for YOLOv8)
- ultralytics >= 8.0.0
- torch >= 2.0.0
- torchvision >= 0.15.0

---

## 🎨 Detection Categories

| Category | Color | Examples |
|----------|-------|----------|
| Large Debris | 🔴 RED | Rocket stages, satellite fragments |
| Medium Debris | 🟠 ORANGE | Antenna pieces, panel fragments |
| Small Debris | 🟢 GREEN | Bolts, paint flecks, wires |
| Micro Debris | 🟢 GREEN | Tiny particles |
| Active Objects | 🔵 BLUE | Functioning satellites |

---

## 📈 Graph Types

1. Distribution of Space Objects
2. Debris Size Distribution
3. Orbital Altitude Distribution
4. Detection Confidence Distribution
5. Model Performance Comparison
6. Training Metrics Evolution
7. Accuracy vs Speed Scatter
8. Debris Collision Projections
9. Object Count Heatmap
10. Debris Objects Timeline
11. Detailed Debris Distribution
12. SPARK Dataset Distribution

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

See `CONTRIBUTING.md` for details.

---

## 📄 License

MIT License - See `LICENSE` file

---

## 🔗 Links

- **Repository**: https://github.com/phoenixdev100/Space-debris-detection
- **Issues**: https://github.com/phoenixdev100/Space-debris-detection/issues
- **Discussions**: https://github.com/phoenixdev100/Space-debris-detection/discussions

---

**Last Updated**: 2025-12-30  
**Version**: 2.0  
**Status**: ✅ Production Ready
