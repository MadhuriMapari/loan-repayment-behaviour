# Understanding Loan Repayment Behaviour — A Story Told by Data

*Exploring how numbers reveal trust, responsibility, and fairness in the world of lending.*

---

###  Why We Needed to Explore First

Before building a model that predicts who might default or repay on time, we need to know **what the data is really saying**.  
Exploratory Data Analysis (EDA) is like meeting a new friend — you listen before you speak.  
It’s where intuition meets evidence.

In our case, the goal was to understand the hidden behavioural patterns behind **loan approvals** — what makes one borrower “trustworthy” to the system and another “risky”?  
By examining real loan-application data, we hoped to find clues in income, credit history, education, and geography.

---

###  The Dataset in Plain Words

The dataset, drawn from the *Loan Prediction Problem* on Kaggle, contains 614 anonymised loan applications.  
Each record is a short story of a potential borrower — their income, education, family structure, and whether they ultimately got approved.

| Example Columns | Meaning |
|:--|:--|
| `ApplicantIncome`, `CoapplicantIncome` | How much money a household earns monthly |
| `LoanAmount`, `Loan_Amount_Term` | How much and how long they plan to borrow |
| `Credit_History` | Whether they have repaid responsibly in the past |
| `Property_Area` | Urban, semi-urban, or rural context |
| `Loan_Status` | Target variable — *approved (Y)* or *rejected (N)* |

This simple structure mirrors the questions any human loan officer would ask:  
**Can the person afford it?**  
**Have they been reliable before?**  
**What’s their background context?**

---

###  Cleaning and Getting Comfortable with the Data

Good analysis starts with trustworthy inputs.  
We noticed small gaps — missing `LoanAmount`, a few `Credit_History` entries left blank — but nothing alarming.  
After replacing missing numeric values with medians and categorical ones with modes, we transformed a few helpful indicators:

```python
df["Loan_Status"] = df["Loan_Status"].map({"Y":1, "N":0})
df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]
df["IncomeToLoanRatio"] = df["TotalIncome"] / (df["LoanAmount"] * 1000)
```

Why these?  
Because real-world lending rarely hinges on raw income — it’s about **affordability**.  
Someone earning $5,000 per month may still struggle if they take a $3,000 EMI.  
The `IncomeToLoanRatio` becomes a window into that relationship.

---

###  Looking at the Distributions — The Shape of Money

Plotting histograms of income and loan amount showed long right tails — a few applicants earning significantly more than others.  
That tells us the dataset isn’t evenly distributed — typical in real finance where inequality exists.

Boxplots highlighted small clusters of unusually high income but small loan requests.  
Instead of removing them, we kept these as *realistic diversity*; people with high incomes sometimes take small loans for convenience or credit building.

Categorical features painted a social snapshot:
- **81 % male** applicants  
- **78 % graduates**  
- **Balance between urban, semi-urban, and rural properties**

Already, we see how economic and social dimensions intersect in lending.

---

###  Who Gets Approved and Why?

Now comes the heart of EDA — connecting behaviour to outcome.  
By grouping each variable by `Loan_Status`, clear differences surfaced:

1. **Credit history is king.**  
   80 % of those with a clean credit record were approved; only 20 % without it.  
   This tells us that financial reputation — not income — is the strongest trust signal.

2. **Education still matters.**  
   Graduates had ~75 % approval, non-graduates ~68 %.  
   The difference isn’t huge, but it points to the indirect influence of financial literacy.

3. **Property area subtly influences opportunity.**  
   Semi-urban residents enjoyed higher approval (~78 %) than rural (~64 %).  
   Possibly because semi-urban economies offer stable jobs yet lower living costs.

4. **Income itself is not destiny.**  
   High income doesn’t guarantee approval, but *income relative to loan size* does.  
   Borrowers with a healthy income-to-loan ratio were far more likely to be accepted.

---

###  Correlations That Tell a Story

A correlation heatmap translated these ideas into numbers.

| Feature | Correlation with Approval |
|:--|--:|
| Credit_History | **0.54** |
| TotalIncome | 0.18 |
| LoanAmount | –0.12 |

That single value — **0.54** — reveals a strong truth: *Past behaviour builds present trust.*  
Everything else, income or education, merely decorates that foundation.

---

###  The Fairness Angle — Who Might Be Left Behind?

Responsible data analysis also asks: *Is the system fair?*  
We compared approval rates across demographic groups:

| Group | Approval Rate |
|:--|--:|
| Male | 71 % |
| Female | 69 % |
| Graduate | 75 % |
| Not Graduate | 68 % |
| Semi-Urban | 78 % |
| Rural | 64 % |

The differences are small but meaningful.  
Lower rural approvals may not mean bias — perhaps lower access to credit history or informal employment records.  
Still, fairness checks will remain a recurring part of this project.

---

###  Turning Observations into Hypotheses

EDA isn’t just about describing patterns; it’s about *guessing wisely*.  
Here’s what we hypothesised for the modelling phase:

1. Applicants with valid credit history are **significantly** more likely to be approved.  
2. Higher `IncomeToLoanRatio` will **positively** influence approval probability.  
3. Educational attainment might **improve repayment reliability**.  
4. Regional differences will persist but should **not** dominate model decisions.

These will later guide feature engineering, model selection, and SHAP interpretability.

---

###  What We Produced

| File | Purpose |
|:--|:--|
| `eda_summary.csv` | Key statistics for each variable |
| `eda_hypotheses.txt` | Generated insights for model phase |
| `segment_fairness.csv` | Early demographic fairness snapshot |
| `images/*.png` | Saved plots — distributions, heatmaps, bar charts |

Every artifact acts as an *audit trail*, ensuring this work remains reproducible and reviewable.

---

###  Insights in Perspective

1. **Credit trust outweighs wealth.**  
   People’s past repayment habits signal reliability better than income alone.

2. **Affordability ratios contextualise fairness.**  
   Looking at money through ratios, not absolutes, prevents hidden bias.

3. **Education and region are weak but ethical indicators.**  
   They explain part of the pattern but should never drive automated decisions.

4. **Data integrity and transparency matter.**  
   Understanding data lineage — how we cleaned and transformed — protects against accidental bias.

---

###  Preparing for the Next Step

With EDA complete, we now move into feature engineering and model building.  
Each insight will become a measurable variable — and every model will be tested not just for accuracy but **for fairness and interpretability**.

The story we uncovered here — of trust, affordability, and opportunity — now becomes the foundation for building responsible AI in finance.

---

###  Author

**Madhuri Mapari**  
Specialising in data ethics, explainable AI, and customer behaviour analytics.

---

*This analysis is part of the broader [Loan Repayment Behaviour Analytics](../README.md) project — a 21-day open-source journey combining Python, Power BI, and fairness-driven AI design.*
