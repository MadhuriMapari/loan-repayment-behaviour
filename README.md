# The Trust Equation — Data Stories Behind Loan Repayment  

*A data storytelling project that turns credit records into insights on trust, fairness, and financial wellbeing.*

---

##  Why This Project Matters  

Every repayment tells a story — of confidence, hardship, or opportunity.  
This project transforms open loan-repayment data into **evidence-based insights** that help financial and government organisations engage customers early, fairly, and effectively.

It’s not just about predicting who will repay.  
It’s about understanding **why people repay**, **how trust is built**, and **how data can be used responsibly** to support them.

---

##  From Data to Decisions  

| Stage | Focus | Deliverable | Status |
|:--|:--|:--|:--|
| 1️ | **Data Collection & Cleaning** | Consolidated and validated open loan data (600+ records) | Done |
| 2 | **Exploratory Data Analysis (EDA)** | Mapped patterns of income, credit history, and default | Done |
| 3 | **Fairness & Segmentation** | Quantified demographic and geographic equity | Done |
| 4 | **Feature Engineering** | Derived indicators for income comfort, EMI ratio, and payment resilience | In Progress |
| 5 | **Predictive Modelling** | Logistic Regression & Random Forest with SHAP-based explainability | Planned |
| 6 | **Actionable Dashboard** | Power BI storytelling dashboard for decision-makers | Planned |

---

##  Headline Insights  

> **Credit History is Destiny, but Income Comfort Builds Confidence.**

| Factor | What We Learned | What It Means |
|:--|:--|:--|
| **Credit History** | ~80 % approval for clean records, ~20 % for poor ones | Trust is the strongest currency in lending. |
| **Income-to-Loan Ratio** | Better predictor than income alone | Sustainable affordability beats raw wealth. |
| **Property Area** | Semi-urban borrowers most consistent | Economic balance drives repayment stability. |
| **Demographics** | Gender and education differences < 5 % | Lending patterns are largely fair and inclusive. |

---

##  Visual Storytelling  

<p align="center">
  <img src="images/advanced_eda_viz/correlation_heatmap.png" alt="Correlation Heatmap" width="30%"/>
  <img src="images/advanced_eda_viz/violin_Credit_History_by_target.png" alt="Credit History Violin Plot" width="30%"/>
  <img src="images/advanced_eda_viz/boxen_Credit_History_by_target.png" alt="Credit History Boxen Plot" width="30%"/>
</p>

**Figure:**  
(1) Correlations show credit history as the most influential factor.  
(2) Violin plots reveal distribution of repayment probability.  
(3) Boxen plots highlight variability between risk groups.

---

## ️ Analytical Backbone  

| Concept | Formula | Role in the Analysis |
|:--|:--|:--|
| **Approval Rate** | $\hat{p}=x/n$ | Quantifies success ratio within each borrower segment. |
| **Confidence Interval** | $\hat{p}\pm1.96\sqrt{\hat{p}(1-\hat{p})/n}$ | Measures reliability of observed rates. |
| **Correlation** | $r_{XY}=\mathrm{Cov}(X,Y)/(\sigma_X\sigma_Y)$ | Evaluates feature influence on repayment. |
| **Fairness Gap** | $\Delta_{AB}=|\hat{p}_A-\hat{p}_B|$ | Tests equity across customer subgroups. |

These metrics ground the visuals in statistical credibility — every conclusion is testable and traceable.

---

##  What Stakeholders Can Take Away  

- **For Financial Institutions:** Identify early signs of payment stress and offer tailored repayment pathways.  
- **For Policymakers:** Track fairness in credit access and outcomes to maintain trust in public programmes.  
- **For Data Teams:** Build interpretable, bias-aware models that align with both performance and equity.  
- **For Citizens:** Transparent analytics that explain *why* decisions are made — not just *what* decisions are made.

---

##  Full Analytical Report  

📘 [Read the complete EDA report →](docs/EDA_Explained_Full.md)  
Includes detailed visuals, formula explanations, and fairness analysis.

---

##  Why This Work Stands Out  

✔ **Ethical by design** — fairness and transparency are built in, not added later.  
✔ **Cross-audience clarity** — written for analysts *and* decision-makers.  
✔ **Evidence-driven** — every finding backed by measurable data.  
✔ **Scalable vision** — roadmap extends to modelling, dashboards, and deployment.

---

##  Author  

**Madhuri Mapari**  
*Data & AI Specialist — blending analytics, fairness, and storytelling to power responsible decisions.*

---

*Updated October 2025 • Part of the Loan Repayment Behaviour Analytics Project*
