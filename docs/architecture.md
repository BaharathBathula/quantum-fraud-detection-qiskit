# System Architecture

This project demonstrates a hybrid quantum-classical machine learning pipeline.

## Workflow

Fraud Dataset  
↓  
Data Sampling & Preprocessing  
↓  
Feature Scaling  
↓  
Quantum Feature Encoding (ZZFeatureMap)  
↓  
Quantum Kernel Computation (FidelityQuantumKernel)  
↓  
Quantum Support Vector Classification (QSVC)  
↓  
Fraud Prediction & Evaluation

## Explanation

The ZZFeatureMap encodes classical features into quantum states.

The FidelityQuantumKernel measures similarity between quantum states.

The QSVC model uses this kernel to classify fraudulent vs legitimate transactions.
