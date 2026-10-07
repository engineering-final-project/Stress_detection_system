# Stress_detection_system

A **Stress Detection System** built using **Python**, **Scikit-learn**, and **SVM (SVC)** to classify stress levels from smartwatch and sensor data.

## Features
- Multi-class stress classification: **No Stress**, **Medium Stress**, **High Stress**
- Sensor parameters: Body Temperature, Blood Oxygen, Heart Rate, Hours of Sleep, Activity Level
- ML Pipeline: `SimpleImputer` → `PolynomialFeatures` → `StandardScaler` → `SVC (Linear)`
- Hyperparameter tuning via `GridSearchCV` with 5-fold cross-validation
- User-friendly GUI for real-time stress prediction using Tkinter
- User authentication system (Registration, Login, Forgot Password)

## Tech Stack
- **Language:** Python
- **ML Libraries:** Scikit-learn (SVM, Pipeline, GridSearchCV)
- **GUI:** Tkinter
- **Database:** SQLite3

