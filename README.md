# 🦴 Bone Fracture Classification System

> AI-Powered Bone Fracture Detection and Classification using ResNet50 Transfer Learning, TensorFlow, and Gradio

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.8.0-orange)
![Keras](https://img.shields.io/badge/Keras-2.8.0-red)
![Gradio](https://img.shields.io/badge/Gradio-6.15.1-green)
![Accuracy](https://img.shields.io/badge/Test%20Accuracy-92.73%25-brightgreen)

---

## 📌 Overview

Bone fractures are among the most common orthopedic injuries and require timely diagnosis for effective treatment. Manual interpretation of X-ray images can be time-consuming and may vary depending on clinical expertise.

This project presents an AI-powered Bone Fracture Classification System that automatically analyzes X-ray images and predicts whether a fracture is present.

The system combines Deep Learning, Transfer Learning, Computer Vision, and an interactive Gradio dashboard to provide rapid and reliable fracture assessment. In addition to prediction, the application generates professional PDF diagnostic reports containing patient details, prediction results, confidence scores, risk assessment, AI interpretation, and model information.

This project was developed as a portfolio-focused healthcare AI application demonstrating practical deployment of Deep Learning models in medical image analysis.

---

## 🎯 Project Objectives

* Automate bone fracture detection from X-ray images.
* Reduce diagnosis time through AI-assisted analysis.
* Provide confidence-based predictions for improved decision support.
* Generate professional diagnostic reports automatically.
* Demonstrate practical deployment of Deep Learning models.

---

## 📊 Project Summary

| Feature              | Details                        |
| -------------------- | ------------------------------ |
| Model Architecture   | ResNet50 Transfer Learning     |
| Framework            | TensorFlow 2.8.0 / Keras 2.8.0 |
| Classification Type  | Binary Classification          |
| Classes              | Fractured / Not Fractured      |
| Test Accuracy        | 92.73%                         |
| Dashboard            | Gradio                         |
| Report Generation    | PDF Reports                    |
| Programming Language | Python 3.10                    |

---

## 🚀 Key Features

### 🦴 Bone Fracture Classification

Classifies X-ray images into:

* Fractured
* Not Fractured

### 📈 Confidence Score Analysis

Displays prediction confidence for every uploaded X-ray image.

### ⚠️ Risk Assessment

Provides reliability and risk-level information associated with model predictions.

### 📜 Prediction History

Maintains a history of previous predictions for reference and analysis.

### 📄 Professional PDF Report Generation

Automatically generates downloadable PDF reports containing:

* Patient Information
* Report ID
* Scan Date
* Diagnosis
* Confidence Score
* Risk Assessment
* AI Interpretation
* Model Information
* Disclaimer

### 🖥️ Interactive Gradio Dashboard

Provides an intuitive user interface for image upload, prediction visualization, and report generation.

---

## 🏗️ System Architecture

```text
X-Ray Image
     │
     ▼
Image Preprocessing
     │
     ▼
ResNet50 Feature Extraction
     │
     ▼
Dense Classification Layers
     │
     ▼
Fractured / Not Fractured
     │
     ▼
Confidence Score
     │
     ▼
PDF Diagnostic Report
```

---

## 🧠 Model Architecture

The fracture detection model uses Transfer Learning with ResNet50 as the backbone network.

```text
Input Image
     │
     ▼
ResNet50 (Pretrained on ImageNet)
     │
     ▼
Flatten
     │
     ▼
Dense (128)
     │
     ▼
Dropout
     │
     ▼
Dense (1)
     │
     ▼
Binary Classification
```

The pretrained ResNet50 layers were utilized for feature extraction while custom classification layers were added for fracture prediction.

---

## 📊 Model Performance

| Metric              | Value                     |
| ------------------- | ------------------------- |
| Test Accuracy       | **92.73%**                |
| Dataset Type        | X-Ray Images              |
| Classification Type | Binary                    |
| Classes             | Fractured / Not Fractured |
| Backbone Network    | ResNet50                  |
| Framework           | TensorFlow / Keras        |

### Classification Logic

```python
prediction < threshold  -> Fractured
prediction >= threshold -> Not Fractured
```

This logic was verified using multiple test samples and validation images.

---

## 🛠️ Technology Stack

### Programming Language

* Python 3.10

### Deep Learning

* TensorFlow 2.8.0
* Keras 2.8.0
* ResNet50 Transfer Learning

### Dashboard

* Gradio 6.15.1

### Reporting

* ReportLab 4.5.1

### Supporting Libraries

* NumPy
* Pandas
* OpenCV
* Pillow
* Matplotlib
* Scikit-Learn
* SciPy

---

## 📸 Application Dashboard

The Gradio dashboard allows users to upload X-ray images, view prediction results, confidence scores, risk assessment, prediction history, and generate professional PDF reports.

![Dashboard](screenshots/Screenshot%202026-05-29%20143420.png)

---

## 📄 Sample Diagnostic Report

The system automatically generates professional PDF reports containing patient details, diagnostic results, confidence scores, AI interpretation, and model information.

![PDF Report](screenshots/Screenshot%202026-05-29%20143637.png)

---

## 📂 Project Structure

```text
BoneFractureClassification/

├── app/
│   ├── app.py
│   ├── prediction_history.csv
│   └── reports/
│       └── report_generator.py
│
├── dataset/
│
├── model/
│   └── README.md
│
├── screenshots/
│
├── bone_fracture_training.ipynb
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Shivansh-3010/BoneFractureClassification.git
cd BoneFractureClassification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
cd app
python app.py
```

---

## 📦 Required Package Versions

```text
tensorflow==2.8.0
keras==2.8.0
numpy==1.21.6
pandas==2.0.3
gradio==6.15.1
opencv-python==4.13.0.92
pillow==12.2.0
reportlab==4.5.1
matplotlib==3.5.3
scikit-learn==1.7.2
scipy==1.10.1
h5py==3.16.0
protobuf==3.20.3
tensorboard==2.8.0
tensorflow-io-gcs-filesystem==0.31.0
```

---

## 📌 Model File

The trained model file is not included in this repository due to GitHub file size limitations.

Expected model location:

```text
model/best_bone_fracture_model.keras
```

---

## 🔮 Future Enhancements

* Multi-Class Fracture Classification
* Cloud Deployment
* REST API Integration
* Mobile Application Support
* Expanded Medical Dataset
* Advanced Explainable AI Techniques
* Real-Time Clinical Decision Support

---

## 👨‍💻 Author

### Shivansh Deshwal

Data Science Student

Areas of Interest:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Computer Vision
* Healthcare AI

---

## ⚠️ Disclaimer

This project is intended for educational, research, portfolio, and demonstration purposes only.

The predictions generated by this system should not be considered a substitute for professional medical diagnosis, treatment, or medical advice.

Always consult qualified healthcare professionals for clinical decisions.
