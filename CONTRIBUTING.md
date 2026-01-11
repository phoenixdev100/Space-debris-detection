# Contributing to Space Debris Detection

Thank you for your interest in contributing to the Space Debris Detection project! 🛰️

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Space-debris-detection.git
   cd Space-debris-detection
   ```

3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/phoenixdev100/Space-debris-detection.git
   ```

4. **Create a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Development Setup

### Project Structure

```
Space-debris-detection/
├── src/                    # Source code
├── assets/                 # Input data
├── graphs/                 # Graph generation scripts
├── output/                 # Generated outputs
├── docs/                   # Documentation
└── tests/                  # Unit tests (to be added)
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_detection.py

# Run with coverage
python -m pytest --cov=src tests/
```

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

- **Clear title** describing the problem
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)

### Suggesting Enhancements

For feature requests:

- **Describe the feature** and its benefits
- **Explain use cases** where it would be helpful
- **Provide examples** if possible
- **Consider alternatives** you've thought about

### Pull Requests

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Test your changes** thoroughly

4. **Commit with clear messages**:
   ```bash
   git commit -m "Add: Brief description of changes"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** on GitHub

## Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

- **Line length**: Maximum 100 characters
- **Indentation**: 4 spaces (no tabs)
- **Naming conventions**:
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`

### Documentation

- **Docstrings**: Use Google-style docstrings for all functions and classes
- **Comments**: Explain "why", not "what"
- **Type hints**: Use type hints for function parameters and return values

Example:

```python
def detect_debris(frame: np.ndarray, threshold: float = 0.5) -> List[Detection]:
    """
    Detect debris objects in a video frame.
    
    Args:
        frame: Input video frame as numpy array
        threshold: Confidence threshold for detection (0.0 to 1.0)
        
    Returns:
        List of Detection objects containing bounding boxes and labels
        
    Raises:
        ValueError: If threshold is not between 0 and 1
    """
    if not 0 <= threshold <= 1:
        raise ValueError("Threshold must be between 0 and 1")
    
    # Detection logic here
    return detections
```

### Code Organization

- **One class per file** when possible
- **Group related functions** together
- **Import order**: stdlib, third-party, local
- **Avoid circular imports**

### Git Commit Messages

Follow the conventional commits format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Example:
```
feat: Add adaptive threshold adjustment

- Implement dynamic confidence threshold
- Add detection history tracking
- Update visualization to show current threshold
```

## Testing Guidelines

### Writing Tests

- **Test file naming**: `test_<module_name>.py`
- **Test function naming**: `test_<function_name>_<scenario>`
- **Use fixtures** for common setup
- **Mock external dependencies** (file I/O, network calls)

Example:

```python
import pytest
import numpy as np
from src.detection import detect_debris

def test_detect_debris_with_valid_frame():
    """Test debris detection with a valid input frame."""
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    detections = detect_debris(frame)
    assert isinstance(detections, list)

def test_detect_debris_with_invalid_threshold():
    """Test that invalid threshold raises ValueError."""
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    with pytest.raises(ValueError):
        detect_debris(frame, threshold=1.5)
```

### Test Coverage

- Aim for **80%+ code coverage**
- Focus on **critical paths** and edge cases
- Test **error handling** thoroughly

## Submitting Changes

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts with main branch

### Pull Request Checklist

- [ ] Clear title and description
- [ ] References related issues
- [ ] Screenshots/GIFs for UI changes
- [ ] Updated CHANGELOG.md (if applicable)
- [ ] Requested review from maintainers

### Review Process

1. **Automated checks** run on your PR
2. **Maintainer review** within 3-5 days
3. **Address feedback** and update PR
4. **Approval and merge** by maintainer

## Questions?

If you have questions:

- Check existing **issues** and **discussions**
- Open a new **discussion** for general questions
- Open an **issue** for bugs or feature requests

## Recognition

Contributors will be:

- Listed in **CONTRIBUTORS.md**
- Mentioned in **release notes**
- Credited in **documentation**

Thank you for contributing! 🚀
