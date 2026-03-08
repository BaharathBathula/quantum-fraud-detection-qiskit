# Project Overview

## Title
Quantum Fraud Detection using Qiskit

## Objective
Build a hybrid quantum-classical machine learning workflow for financial fraud detection.

## Methods
- Classical SVM baseline
- Quantum feature mapping with ZZFeatureMap
- FidelityQuantumKernel
- QSVC for quantum classification

## Why small sample size?
Quantum kernel methods are computationally expensive, so this project uses a small balanced sample for proof-of-concept experimentation.

## Future scope
- Add ROC-AUC
- Add confusion matrix
- Test more feature maps
- Compare with Logistic Regression and XGBoost
- Run on IBM Quantum backends
