#  Loan Repayment Behaviour Analytics

> *A 21-day analytical journey — from open loan-repayment data to explainable, fair, and actionable insights.*

---

##  Overview

Late repayments often indicate financial stress or disengagement.  
This project explores open loan-repayment data to uncover factors that separate on-time payers from those who default.  
The goal is to build interpretable, fair predictive models — inspired by **Inland Revenue’s customer-centric philosophy** of early intervention and supportive engagement.

---

##  Objective

Conduct advanced analysis of open loan-repayment data to identify **transparent, fair, and actionable** patterns in repayment behaviour.  
The insights will help design ethical, data-driven outreach strategies aligned with Inland Revenue’s values of fairness, empathy, and compliance.

---

##  Project Flow

| Phase | Stage | Key Focus | Output |
|:--|:--|:--|:--|
| **1. Setup & Planning** | Days 1-2 | Create repo, folder structure, utils, and documentation |  `README.md`, `utils_paths.py` |
| **2️. Data Intake & Cleaning** | Days 3-4 | Load, inspect, and clean Kaggle dataset | `loan_data_clean_start.csv` |
| **3️. Exploratory Data Analysis** | Days 5-7 | Discover patterns, correlations, and fairness indicators | [ EDA Explained Report →](docs/EDA_Explained.md) |
| **4️. Feature Engineering** | Days 8-10 | Create behavioural & ratio-based features | `loan_features.csv`, feature dictionary |
| **5️. Modelling (Planned)** | Days 11-13 | Baseline Logistic Regression & Random Forest | `04_model_baselines.ipynb` |
| **6️. Explainability & Fairness (Planned)** | Days 14-15 | SHAP, parity checks | Visual report + Power BI metrics |

---

##  Updated 21-Day Schedule (Progress → Feature Engineering)

| Day Range | Focus Area | Deliverables | Status |
|:--|:--|:--|:--|
| **1-2** | Repository setup, `.gitignore`, project board, utils | Base repo live + paths configured |  Done |
| **3-4** | Data acquisition & intake | Clean CSV, missing-value analysis |  Done |
| **5-7** | Exploratory Data Analysis | Distributions, correlations, fairness snapshot |  Done |
| **8-9** | Feature design | Income-loan ratio, EMI, balance-income, bins |  In Progress |
| **10** | Feature validation + export | Feature dictionary + ready CSV |  Pending |

---

##  Key Insights from EDA

- **Credit History (0.54 corr)** → strongest predictor of approval  
- **Income-to-Loan Ratio** → secondary signal for affordability  
- **Education & Property Area** → mild but ethical drivers  
- **No major demographic bias** → approval rates similar across gender  

Detailed narrative, visuals, and fairness analysis:  
 [**EDA Explained Document →**](docs/EDA_Explained.md)

---

##  Next Steps (Feature Engineering)

1. **Derive new behavioural features**  
   - `IncomeToLoanRatio`, `BalanceIncome`, `EMI`, `FamilySize`
2. **Create categorical bands**  
   - Income bands, Loan amount bands, and Term bands for interpretability
3. **Validate feature distributions**  
   - Ensure no negative or skewed features distort models
4. **Save processed dataset**  
   - `loan_features.csv` in `/data/processed/`

---

##  Tools & Libraries

| Category | Tools |
|:--|:--|
| Languages | Python (pandas, scikit-learn, matplotlib, seaborn), SQL (optional) |
| Environment | Jupyter / Colab |
| Visualization | Power BI (for dashboards) |
| Repository Mgmt | GitHub Project Board & Issues for tracking |

---

##  Repository Structure

```text
Loan_Repayment_Behaviour_Analytics/
│
├── notebooks/
│   ├── 01_data_intake.ipynb
│   ├── 02_eda.ipynb
│   └── 03_feature_engineering.ipynb
│
├── data/
│   ├── raw/          # Original Kaggle data
│   ├── interim/      # Cleaned datasets & EDA outputs
│   └── processed/    # Feature-engineered data
│
├── src/
│   ├── utils_paths.py
│   └── utils_visuals.py
│
├── docs/
│   ├── EDA_Explained.md
│   └── reports/ (coming soon)
│
├── images/
│   └── eda_plots/
│
└── README.md
```

---

##  Author

**Madhuri Mapari**  
📧 maparimadhuri@gmail.com  

---

## ⚖️ License
Licensed under the **Apache 2.0 License** — free for educational and fair-use demonstration.

---
