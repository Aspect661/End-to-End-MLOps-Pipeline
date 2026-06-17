# Wine Quality Predictor — End-to-End MLOps Pipeline

> A production-ready machine learning pipeline that predicts wine quality from physicochemical properties, built with modular architecture, experiment tracking, and a live Flask web interface.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-blue?logo=mlflow)](https://mlflow.org/)
[![DagsHub](https://img.shields.io/badge/DagsHub-Remote%20Tracking-orange)](https://dagshub.com/)
[![ElasticNet](https://img.shields.io/badge/Model-ElasticNet-green)](https://scikit-learn.org/)

---

## Table of Contents

- [Overview](#overview)
- [Project Architecture](#project-architecture)
- [Pipeline Stages](#pipeline-stages)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Experiment Tracking](#experiment-tracking)
- [Web Application](#web-application)
- [Results](#results)

---

## Overview

This project demonstrates a **full ML lifecycle implementation** — from raw data ingestion to a deployed prediction interface — following MLOps best practices. The model predicts wine quality scores based on 11 physicochemical inputs (e.g., acidity, pH, alcohol content) using a regularized regression approach.

While the model itself is intentionally simple (ElasticNet), the **engineering pipeline is the centerpiece**: modular components, schema validation, centralized configuration, and integrated experiment tracking make this project scalable and production-ready.

---

## Project Architecture

```
Data Ingestion → Data Validation → Data Transformation → Model Training → Model Evaluation → Flask App
      ↓                ↓                  ↓                    ↓                ↓
  artifacts/       status.txt        train/test sets       model.joblib    MLflow / DagsHub
```

Each stage is a self-contained component driven by configuration files, ensuring the pipeline is **reproducible, testable, and easy to extend**.

---

## Pipeline Stages

### 1. Data Ingestion
- Downloads the raw `winequality.csv` dataset from a remote GitHub repository
- Extracts and stores the data in the `artifacts/` directory
- Enables full **reproducibility** from a single source of truth

### 2. Data Validation
- Validates that all expected columns (defined in `schema.yaml`) are present in the dataset
- Writes a `status.txt` file to track validation outcomes
- Prevents downstream failures caused by schema drift or corrupt data

### 3. Data Transformation
- Applies feature engineering and preprocessing steps
- Splits data into **train/test sets** using configurable ratios
- Stores transformed artifacts in `artifacts/data_transformation/` for the next stage

### 4. Model Training
- Trains an **ElasticNet regression model** on the preprocessed training data
- Serializes the trained model as a `.joblib` file for persistence and reuse
- Hyperparameters (`alpha`, `l1_ratio`) are fully configurable via `params.yaml`

### 5. Model Evaluation
- Evaluates model performance on the held-out test set
- Computes **RMSE, MAE, and R²** metrics
- Logs all metrics and parameters to **MLflow** (remote tracking via **DagsHub**)
- Enables experiment comparison across runs without manual bookkeeping

### 6. Prediction & Deployment
- A **Flask web application** (`app.py`) serves real-time predictions
- Users input wine physicochemical properties via a browser form
- The `PredictionPipeline` loads the trained model from artifacts and returns a quality score

---

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.8+ |
| ML Framework | Scikit-learn (ElasticNet) |
| Experiment Tracking | MLflow + DagsHub |
| Web Framework | Flask |
| Configuration | YAML (`config.yaml`, `params.yaml`, `schema.yaml`) |
| Serialization | Joblib |
| Environment Management | `.env` + `python-dotenv` |

---

## Project Structure

```
wine-quality-mlops/
├── src/
│   └── mlProject/
│       ├── components/          # Core pipeline logic (ingestion, validation, etc.)
│       ├── config/              # Configuration manager
│       ├── entity/              # Dataclasses / config entities
│       ├── pipeline/            # Stage orchestration scripts
│       └── utils/               # Shared utilities
├── config/
│   ├── config.yaml              # Paths, URLs, artifact locations
│   ├── params.yaml              # Model hyperparameters
│   └── schema.yaml              # Expected dataset schema
├── artifacts/                   # Auto-generated pipeline outputs (gitignored)
├── app.py                       # Flask web application
├── main.py                      # Full pipeline runner
├── requirements.txt
└── .env                         # Credentials (never committed)
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/wine-quality-mlops.git
cd wine-quality-mlops

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your DagsHub credentials
```

### Run the Full Pipeline

```bash
python main.py
```

This executes all 5 stages in sequence: ingestion → validation → transformation → training → evaluation.

### Launch the Web App

```bash
python app.py
```

Navigate to `http://localhost:5000` to use the prediction interface.

---

## Configuration

All pipeline behavior is controlled through three YAML files — **no hardcoded values anywhere**:

| File | Purpose |
|---|---|
| `config/config.yaml` | File paths, data source URLs, artifact directories |
| `config/params.yaml` | Model hyperparameters (`alpha`, `l1_ratio`) |
| `config/schema.yaml` | Expected dataset columns for validation |

Secrets (e.g., DagsHub credentials) are stored in `.env` and loaded via `python-dotenv`. They are **never committed to version control**.

---

## Experiment Tracking

All training runs are tracked via **MLflow**, with a remote backend on **DagsHub**:

- Logged parameters: `alpha`, `l1_ratio`
- Logged metrics: `RMSE`, `MAE`, `R²`
- Artifacts: trained model, evaluation results

To view the experiment dashboard:
```bash
mlflow ui
# or visit your DagsHub repository's Experiments tab
```

---

## Web Application

The Flask app provides a clean interface for real-time inference:

1. Enter wine physicochemical properties (fixed acidity, volatile acidity, citric acid, etc.)
2. Submit the form
3. The `PredictionPipeline` loads the trained model and returns a **quality score**

---

## Results

| Metric | Value |
|---|---|
| RMSE | _fill in_ |
| MAE | _fill in_ |
| R² | _fill in_ |

> Results are logged per-run in MLflow. The table above reflects the best run.

---

## 📝 License

This project is licensed under the MIT License.


### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py