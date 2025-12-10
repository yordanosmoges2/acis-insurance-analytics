# ACIS Insurance Analytics – Final Project

This project analyzes customer data to predict whether a proposed insurance policy will be accepted.  
The workflow follows the AIDA corporate process and includes EDA, hypothesis validation, machine learning, and model explainability.

---

## 📌 Deliverables by Task

### 🧩 Task 1 — Business Understanding
- Objective: **Predict customer acceptance** of a proposed rating
- Success Metrics:
  - Improve acceptance prediction accuracy
  - Reduce underwriting manual work
  - Identify key premium-driving factors influencing acceptance
- Stakeholders: ACIS Underwriting, Pricing Team, Business Leads

---

### 🔍 Task 2 — Hypothesis + Data Dictionary
- Key Hypotheses:
  - H1: Higher premium → lower acceptance
  - H2: Newer vehicles → higher acceptance
  - H3: Customers selecting **No Excess** more likely to accept
- Data Dictionary Summary:
  - Numeric: Premium, mmcode, Vehicle age, Cylinders
  - Categorical: Product type, Excess level, Province, Risk category
- Target Variable: `Acceptance_Flag`

---

### 📊 Task 3 — EDA & Data Cleaning
- Missing values handled via imputation
- Numeric/categorical separation for modeling
- Distributions, correlations visualized
- Outliers investigated via boxplots
- Business insights extracted (premium + acceptance patterns)

Notebook: `notebooks/task3_eda.ipynb`

---

### 🤖 Task 4 — Modeling
- Model: **Random Forest Classifier** wrapped in `Pipeline`
- Stratified train/test split
- Class imbalance handled using `class_weight="balanced"`
- Evaluation metrics:
  - Accuracy: XX%
  - ROC-AUC: XX%
  - Precision/Recall: reported in notebook

Notebook: `notebooks/task4_modeling.ipynb`

---

### 🧠 Task 5 — Explainability (XAI)
- Feature Importances show strongest drivers:
  - ❗ Premium features most important in decisions
  - 🚗 New registration years increase acceptance
  - ⚠ Excess selection affects customer price sensitivity
- Methods used:
  - Partial Dependence Plots (PDP)
  - Model insights translated for business stakeholders

Notebook: `notebooks/task5_explainability.ipynb`

---

## 📂 Repository Structure

acis-insurance-analytics/
│
├── notebooks/
│ ├─ task3_eda.ipynb
│ ├─ task4_modeling.ipynb
│ └─ task5_explainability.ipynb
│
├── reports/
│ └─ interim_report.md
│
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🛠️ Tools & Technologies
- Python 3.12
- Pandas, NumPy
- Scikit-learn
- Matplotlib

---

## 👤 Yordanos moges
Yam — ACIS Insurance Analytics Project (Tasks 1–5)