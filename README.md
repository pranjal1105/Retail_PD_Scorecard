Retail Probability of Default (PD) Scorecard Model

Dataset: Home Credit Default Risk

📌 Project Overview

This project presents the development of an end-to-end Retail Application Probability of Default (PD) Scorecard Model using traditional credit risk modeling techniques.

The objective was to build an interpretable, production-style scorecard aligned with banking standards for underwriting and risk-based decisioning.

The model estimates borrower-level default probability and converts it into an operational credit score using standard score scaling methodology.

🎯 Business Objective

To develop a regulatory-compliant, interpretable retail credit scorecard capable of:

Predicting Probability of Default (PD)

Ranking applicants by risk

Supporting approval strategy decisions

Enabling portfolio segmentation

This project follows the classical WOE–IV–Logistic Regression scorecard development framework widely used in banking institutions.

🏗️ Modeling Framework
1️⃣ Data Preparation

Data cleaning and preprocessing

Train–test split (80% / 20%)

Missing value imputation

All transformations performed on training data only to prevent data leakage

2️⃣ Feature Engineering

Weight of Evidence (WOE) binning using quantile segmentation (pd.qcut())

Stored:

Bin edges

WOE mappings

Information Value (IV) calculation

Variable selection threshold: IV ≥ 0.05

3️⃣ Model Development
Single Factor Analysis (SFA)

Evaluated individual predictive strength

Verified directional consistency

Multi-Factor Analysis (MFA)

Logistic Regression using statsmodels

Removed variables with sign inconsistency

Checked multicollinearity (VIF < 2)

Final model: 9 variables

📊 Model Performance
Metric	Train	Test
AUC	~0.73	~0.73
KS	~0.34	~0.34
Somer’s D	~0.46	~0.46

No significant overfitting observed

Stable discrimination across datasets

🎯 Scorecard Scaling

Score scaling performed using industry-standard methodology:

Base Score: 600

Points to Double the Odds (PDO): 20

Base Odds: 50

Generated borrower-level credit scores for both train and test datasets.

📈 Post-Model Analysis

Decile segmentation using train-based cutoffs

Applied identical bins to test dataset

Created Grade Bands (A–E)

Verified:

Monotonic bad rate behavior

Train–test stability

Conducted approval strategy analysis

📂 Repository Structure
Retail-PD-Scorecard/
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_woe_iv_binning.ipynb
│   ├── 03_model_building.ipynb
│   ├── 04_validation.ipynb
│   ├── 05_score_scaling.ipynb
│   ├── 06_strategy_analysis.ipynb
│
├── src/
│   ├── woe.py
│   ├── model.py
│   ├── scoring.py
│   ├── validation.py
│
├── reports/
│   └── Retail_PD_Scorecard_Summary.pdf
│
└── README.md
🛠️ Tech Stack

Python

pandas

numpy

statsmodels

scikit-learn

matplotlib

seaborn

📌 Key Highlights

End-to-end credit risk scorecard development

WOE–IV framework implementation

Multicollinearity control (VIF < 2)

Score scaling implementation (PDO methodology)

Stability validation and strategy simulation

Production-style train/test transformation logic

🚀 How to Reproduce

Clone the repository

Install dependencies:

pip install -r requirements.txt

Run notebooks sequentially

Review model outputs and validation metrics

📌 Future Enhancements

Portfolio Stability Index (PSI) monitoring

Reject inference framework

Cross-validation enhancement

Model calibration assessment

Packaging into deployable scoring API

📬 Author

Pranjal Saxena
Credit Risk & Backend-Focused Developer
India
