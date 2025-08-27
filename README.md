# Garbic Measurement with OpenCV

A Python toolkit for measuring dimensions and performing comparisons using camera images.  
This project applies computer vision techniques (OpenCV, NumPy) to detect edges, estimate object sizes, and compare measurement results across different methods.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## Overview

This repository contains a collection of scripts for measurement tasks using computer vision.  
The methods range from classic edge detection to advanced dimension estimation and comparison algorithms.

Directory structure (main files):


---

## Features

- **Edge Detection**: Detect contours and edges for further measurement (`CalculateEdge.py`).  
- **Dimension Calculation**: Estimate object dimensions from an image (`mainDimensionMethod.py`).  
- **Comparison Methods**: Compare measurements between different images or algorithms (`mainComparisonMethod.py`).  
- **Full Application Flow**: Unified script to run multiple measurement methods (`mainApp.py`).  
- **Demo and Tests**: Example runs and test cases (`test.py`).  
- **Optional YOLO Integration**: Advanced detection-based measurement (`Yolo.py`).  

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/quang-master-2k/aaaaa.git
   cd Garbic_Measurement_openCV
2. **Install dependencies:**
   ```bash
   pip install opencv-python numpy
Add other required libraries if needed.
3. **Read documentation:**
Refer to Code_Guide.docx for method explanation, usage instructions, and input/output expectations.

## Usage
Run different scripts depending on the task:
   ```bash
   python CalculateEdge.py --input path/to/image.jpg --output path/to/output.jpg
   python mainDimensionMethod.py --image path/to/image.jpg --params path/to/params.json
   python mainComparisonMethod.py --base path/to/image1.jpg --compare path/to/image2.jpg
   python mainComparisonMethod.py --base path/to/image1.jpg --compare path/to/image2.jpg
   python mainApp.py
   python test.py

## Contributing

Contributions are welcome! Whether fixing issues, adding methods, or improving documentation—feel free to open a pull request or issue.

## License

Specify your project's license here (e.g., MIT License, Apache 2.0). If not yet defined, consider adding one for clarity.

## Contact

Repository owner: quang-master-2k

For questions or feedback, feel free to open an issue or reach out via GitHub.
