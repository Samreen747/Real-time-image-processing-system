# Real-Time Image Processing and Feature Extraction System

## Overview
This project is a real-time image processing system built using OpenCV and NumPy.  
It captures live video from a webcam and applies multiple transformations to enhance image quality and extract meaningful features such as edges and contrast variations.

The system acts as a preprocessing pipeline for computer vision and AI-based applications.

---

##  Problem Statement
Raw images captured from cameras often suffer from:
- Noise and distortions
- Poor lighting and low contrast
- Difficulty in detecting important features like edges and boundaries

These issues reduce the effectiveness and accuracy of computer vision and AI systems.

---


Before applying Machine Learning or AI models, image data must be:
- Cleaned (noise removal)
- Enhanced (better contrast)
- Structured (feature extraction)

This project demonstrates how preprocessing improves image quality and makes data suitable for further analysis.

It serves as a **foundation for advanced AI systems** such as object detection, face recognition, and autonomous vision.

---


---

## Work flow
1. Captures live frames from the webcam  
2. Converts each frame to grayscale  
3. Applies Gaussian blur to remove noise  
4. Enhances contrast using histogram equalization  
5. Detects edges using Canny edge detection  
6. Combines all processed outputs into a single display grid  
7. Displays results in real-time  

---

##  Output
The system displays a real-time window with a 2×2 grid:


###  Visualization Layout
- Top Row: Grayscale | Blurred Image  
- Bottom Row: Histogram Equalized | Edge Detection
- Press **Q** to exit.

---

##  Features
- Real-time webcam capture
- Grayscale conversion
- Gaussian filtering (noise reduction)
- Histogram equalization (contrast enhancement)
- Canny edge detection (edge extraction)
- Combined visualization of outputs

---

##  Applications
- Preprocessing for AI/ML models  
- Surveillance and monitoring systems  
- Medical image enhancement  
- Edge detection in autonomous vehicles  
- Industrial quality inspection  

---

##  Requirements

### Software
- Python 3.x

### Libraries
Install using: pip install opencv-python numpy

---

## How to Run
1. Clone the repository or download the project  
2. Navigate to the project folder  
3. Run the script: image_preprocessing.py
   
