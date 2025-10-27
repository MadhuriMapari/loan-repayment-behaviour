# Feature Engineering — Loan Repayment Behaviour Analytics

*Supporting file for:* [`03_feature_engineering.ipynb`](../notebooks/03_feature_engineering.ipynb)  
*Dataset:* `loan_data_clean_start.csv` (interim cleaned dataset)  
*Author:* **Madhuri Mapari**  
*Date:* October 2025  

---

##  Purpose

This notebook demonstrates the **core processes of feature engineering** that prepare data for modelling loan-repayment likelihood.  
It bridges Exploratory Data Analysis (EDA) and predictive modelling by transforming raw data into structured, interpretable, and fair numerical form.

---

##  Key Sections & Outputs

### **Feature Creation**
New domain-driven features were derived to improve interpretability and capture repayment behaviour patterns.

| Feature | Formula | Business Meaning |
|:--|:--|:--|
| `TotalIncome` | Applicant + Coapplicant Income | Overall household income |
| `Income_to_Loan_Ratio` | (TotalIncome / LoanAmount) | Borrower’s ability to afford loan |
| `EMI` | LoanAmount / LoanTerm | Monthly repayment burden |
| `Balance_Income` | TotalIncome − EMI | Residual income after loan payment |
| `Income_Band`, `LoanAmt_Band`, `Term_Band` | Quantile-based bins | Behavioural segmentation of borrowers |

 **Visual Output:**  
- Correlation matrix showing new features strengthen signal with `Loan_Status`.  
- EMI and balance-income distributions support affordability logic.

---

### **Feature Transformation**

Transformations were applied to ensure model stability and compatibility:

- **Categorical Encoding:** `Property_Area`, `Education`, `Gender`, `Married`, `Self_Employed` encoded via one-hot scheme.  
- **Log Transformation:** Applied to skewed numeric features (`ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`).  
- **Binary Enforcement:** `Credit_History` cleaned and recoded as {1 = good, 0 = poor, -1 = missing}.  

 **Result:** Dataset expanded to 60+ numeric and one-hot columns suitable for supervised learning.

---

### **Feature Selection**

Methods applied to identify impactful predictors:

| Method | Focus | Insight |
|:--|:--|:--|
| **Correlation Analysis** | Linear relationship with target | Credit History, EMI, and Income-to-Loan Ratio show strong signals |
| **ANOVA (F-test)** | Continuous vs categorical | Confirms significance of affordability ratios |
| **Chi-square Test** | Categorical vs categorical | Semi-urban property area and credit history most predictive |
| **Model-based (Random Forest)** | All features | Credit History and Income-to-Loan Ratio dominate feature importance |

 **Output Visual:** `rf_feature_importances.png`  
shows top predictors influencing repayment probability.

---

### **Feature Extraction**

Applied **Principal Component Analysis (PCA)** to identify underlying dimensions and compress correlated variables.

- **Retained Components:** ~95% variance explained using ~15 components.
- **Cumulative Variance Plot:** saved as `pca_explained_variance.png`.

Also added **interaction term:**  
`Income_x_CreditHistory = TotalIncome × Credit_History`  
to capture joint effect of financial capacity and trustworthiness.

---

### **Feature Scaling**

Demonstrated two normalization strategies:

| Method | Formula | Use Case |
|:--|:--|:--|
| **Standardization** | (x − μ) / σ | Linear models (e.g., Logistic Regression) |
| **Min–Max Scaling** | (x − min) / (max − min) | Neural nets, tree ensembles |

 **Visual:** `scaling_comparison.png` compares scaled income vs loan distributions.  

---

### **Outputs & Files Generated**

| File | Description |
|:--|:--|
| `data/processed/loan_data_model_base.csv` | Model-ready dataset with engineered features |
| `images/advanced_eda_viz/pca_explained_variance.png` | PCA variance plot |
| `images/advanced_eda_viz/scaling_comparison.png` | Comparison of Standard vs Min–Max scaling |
| `images/advanced_eda_viz/rf_feature_importances.png` | Random Forest top feature importance chart |

---

##  Summary of Learnings

- **Feature Creation** captured affordability and repayment capacity.  
- **Transformation** stabilised skew and converted all variables for model ingestion.  
- **Selection & Extraction** isolated strongest predictors and removed redundancy.  
- **Scaling** ensured numerical comparability for downstream models.  

These transformations enhance both *model interpretability* and *fairness* — ensuring that credit predictions remain explainable, transparent, and robust.

---

##  Next Step

Proceed to **Notebook 04 — Baseline Modelling & Explainability**, which will use:
- Logistic Regression & Random Forests  
- SHAP explainers for interpretability  
- Fairness metrics to validate bias-free predictions

---

*This report is part of the [Loan Repayment Behaviour Analytics](../README.md) project.*  
