#  Loan Repayment Behaviour Analytics

> *A journey from open loan-repayment data to a transparent, ethical, and data-driven borrower-insight model.*

---

##  Overview

Late repayments in financial or government systems often signal stress, confusion, or disengagement.  
This project explores **open loan-repayment data** to understand what distinguishes on-time payers from customers who repay late or default.  

The analysis is designed with public-sector fairness in mind—mirroring the approach Inland Revenue takes in supporting customers through early, transparent, and human-centred engagement.

---

##  Project Objective

Conduct advanced analysis of open loan-repayment data to identify **transparent, fair, and actionable factors** that distinguish on-time payers from late or defaulting customers.  
Build interpretable predictive models that can help shape ethical, proactive outreach strategies—drawing inspiration from **Inland Revenue’s principles of early intervention, self-service enablement, and supportive compliance**.

---

##  Analytical Flow

| Step | Stage | Key Tasks | Output |
|------|--------|------------|---------|
| **1** | Data Intake | Load & clean raw Kaggle loan dataset | `loan_data_clean_start.csv` |
| **2** | Exploratory Data Analysis | Identify key variables, missingness, and segment behaviour | Correlation maps, hypotheses |
| **3** | Feature Engineering | Create interpretable metrics (income-to-loan ratio, EMI, etc.) | `loan_features.csv` |
| **4** | Modelling *(next step)* | Logistic Regression & Random Forest | Risk-probability table |
| **5** | Explainability & Reporting *(planned)* | Feature importance, SHAP plots, Power BI dashboard | Insight report |

---

##  Key Insights (so far)

- **Income-to-loan ratio** and **credit history** are strongest signals of repayment success.  
- **Graduate and self-employed segments** show distinctive risk patterns when controlling for income.  
- Early-stage analysis confirms feasibility of fair, transparent segmentation to support data-led outreach.

---

##  Tools & Environment

| Category | Tools |
|-----------|-------|
| Languages | Python ( pandas, scikit-learn, matplotlib ), SQL (optional) |
| Environment | Jupyter / Colab |
| Storage | Local CSV files → Power BI dashboard |
| Dashboard | Power BI (summary KPIs, segmentation, fairness metrics) |

---

##  Folder Structure

```text
Loan_Repayment_Behaviour_Analytics/
│
├── notebooks/
│   ├── 01_data_intake.ipynb
│   ├── 02_eda.ipynb
│   └── 03_feature_engineering.ipynb
│
├── data/
│   ├── raw/                # Original Kaggle data
│   ├── interim/            # Cleaned/intermediate CSVs
│   └── processed/          # Model-ready features
│
├── src/
│   ├── utils_paths.py      # Path helper
│   └── utils_visuals.py    # Visualization helpers (planned)
│
├── images/                 # Saved charts
├── reports/                # Power BI exports
└── README.md
```
---

##  Example Dashboard KPIs (planned)

| KPI | Description |
|-----|-------------|
| **Repayment Rate** | % of loans paid on time |
| **Late/Default Rate Change** | Monthly or annual trend |
| **Engagement Rate** | % of customers responding to outreach |
| **Model Fairness Index** | Equity of predictions across segments |
| **Average Time-to-Resolution** | Time taken to resolve high-risk cases |

---

##  Development Timeline

| Day | Focus | Deliverable | Status
|-----|--------|-------------|--------|
| **Day 1** | Data intake & cleaning | `loan_data_clean_start.csv` | Completed |
| **Day 2** | Exploratory analysis |  Correlations, hypotheses | Completed |
| **Day 3** | Feature engineering |  `loan_features.csv` | Completed |
| **Day 4-5** | Modelling | Logistic & RF baselines |  |
| **Day 6** | Explainability & fairness check | SHAP & bias tests |  |
| **Day 7** | Dashboard & publication | Power BI + GitHub release |  |

---

##  Next Steps

- Build **`04_model_baselines.ipynb`**  
  (Logistic Regression, Random Forest, cross-validation, feature importance)  
- Integrate **SHAP explainability** to visualize fairness.  
- Create **Power BI dashboard** for interactive policy simulation.

---

##  Author

**Madhuri Mapari**  
[maparimadhuri@gmail.com](mailto:maparimadhuri@gmail.com)

---

##  License
Licensed under the **Apache 2.0** License — free for educational and fair-use demonstration purposes.
