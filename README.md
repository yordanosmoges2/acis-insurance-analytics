# ACIS Insurance Analytics

This project analyzes insurance data to understand claims, loss ratios, and risk patterns using Exploratory Data Analysis (EDA).  
Data is version-controlled using DVC for reproducibility.

---

## Quick Start

```bash
# 1️⃣ Clone repo
git clone <YOUR_REPO_URL>
cd acis-insurance-analytics

# 2️⃣ Activate environment
python -m venv venv
venv\Scripts\activate    # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Pull dataset (DVC)
dvc pull

# 5️⃣ Run Notebook
jupyter notebook notebooks/task1_eda.ipynb
📊 Project Structure
acis-insurance-analytics/
│
├── data/                         # DVC-tracked dataset folder
│   └── MachineLearningRating_v3/
│
├── notebooks/
│   └── task1_eda.ipynb           # Core EDA work
│
├── src/
│   ├── data_loader.py            # Data loading utilities
│   └── eda_utils.py              # Feature engineering & visualization helpers
│
├── reports/
│   └── interim_report.md         # Findings summary
│
├── requirements.txt              # Python dependency list
├── dvc.lock / dvc.yaml           # DVC metadata (optional pipeline stages)
├── README.md
└── .gitignore / .dvcignore