# Quantum Fraud Detection using Qiskit

A professional quantum machine learning project demonstrating fraud detection with Qiskit, QSVC, and classical baseline comparison.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-Quantum-purple)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## Overview

This project explores **quantum machine learning for financial fraud detection** using a hybrid quantum-classical workflow.

The implementation includes:

- **ZZFeatureMap** for quantum feature encoding
- **FidelityQuantumKernel** for similarity computation
- **QSVC** for quantum classification
- **Classical SVM** as a baseline benchmark

The project is designed as a **proof-of-concept research portfolio project** and is structured for GitHub visibility, technical storytelling, and future extension.

---

## Project Objectives

- Demonstrate quantum kernel methods on tabular fraud data
- Compare **quantum vs classical** classification performance
- Build a professional, research-style GitHub repository
- Create a foundation for future experiments on IBM Quantum backends

---

## Architecture

```text
Fraud Dataset
    ↓
Data Sampling & Preprocessing
    ↓
Feature Scaling
    ↓
Quantum Feature Mapping (ZZFeatureMap)
    ↓
Fidelity Quantum Kernel
    ↓
QSVC Classification
    ↓
Fraud Prediction & Evaluation
