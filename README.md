# Project Overview — Loan Repayment Behaviour

### Understanding repayment patterns through transparent, ethical, and data-driven modelling

---

### Overview

Late repayments often signal financial stress or disengagement.  
This project analyses open loan-repayment data to uncover transparent, fair, and actionable patterns that distinguish consistent payers from late or defaulting customers.

The analysis demonstrates how data science can support early and empathetic engagement by identifying behavioural and financial factors linked to repayment outcomes.

---

### Objective

To conduct a structured, explainable analysis of loan-repayment behaviour and build models that:
- Identify key drivers of repayment and financial stress.  
- Support fair, transparent decision-making.  
- Provide interpretable risk segmentation for targeted communication.

---

### Project Flow – From Data to Decisions

| Phase | Focus | Deliverables | Efforts(Days) | Status |
|:--|:--|:--|:--|:--|
| 1 | Setup & Planning | Repo, folder structure, utilities | 1 – 2 | Done |
| 2 | Data acquisition & intake | Consolidated open loan data -Clean CSV, missing-value analysis | 3 – 4 | Done |
| 3 | Exploratory Data Analysis | Patterns of income,Distributions, correlations, fairness snapshot | 5 – 7 | Done |
| 4 | Feature Engineering | Derived affordability and resilience indicators - Ratio features, VIF & leakage audit | 8 – 10 | Done |
| 5 | Baseline Modelling | Logistic Regression & Random Forest pipelines ... | 11 – 15 | In progress |
| 6 | Explainability & Fairness | SHAP explainers, calibration, dashboard | 16-18 | upcoming |
| 7 | Dashboard & Reporting | Power BI / Markdown reports | 19 – 21 | Planned |
---

### Headline Insights (to date)

- Clean credit history correlates strongly with approvals; poor/unknown history lowers them markedly.
- Affordability ratios (income-to-loan; EMI burden) explain outcomes better than raw income alone.
- Regional segments vary in stability; semi-urban borrowers are consistently solid in this dataset.
- Observed demographic gaps are small in this sample; will be rechecked with model-based tests.

---

### Key Artifacts
- `data/processed/loan_data_model_base.csv` — model‑ready dataset  
- `data/processed/feature_dictionary.csv` — column roles & descriptions  
- `docs/EDA_Explained.md` — narrative EDA report  
- `docs/Feature_Engineering_Explained.md` — feature work & rationale  

---

### Getting Started

```
# 1. Clone the repository
git clone https://github.com/MadhuriMapari/loan-repayment-behaviour.git
cd loan-repayment-behaviour

# (optional) create & activate venv
python -m venv .venv

# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
jupyter lab
```

---

What to run (in order)
- ```notebooks/01_data_intake.ipynb```
- ```notebooks/02_eda_advanced.ipynb```
- ```notebooks/03_feature_engineering.ipynb``` : writes data/processed/loan_data_model_base.csv
- ```notebooks/04_model_baselines.ipynb``` : trains/evaluates baselines; saves plots under images/model_baselines/

---

## Next Milestones
1. Finalise baseline metrics: ROC-AUC, PR-AUC, lift@top10, calibration error.
2. Add SHAP summary & dependence plots; short fairness snapshot by key groups.
3. Publish concise model summary and recommendations for outreach actions.

**License**: Apache-2.0
