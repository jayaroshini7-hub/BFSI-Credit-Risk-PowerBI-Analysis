# 🏦 BFSI Credit Risk & Loan Default Analysis (Power BI + Statistical Modeling)

## 📌 Business Problem
Retail lending institutions face capital loss when high-risk borrowers default on personal loans. This project analyzes **5,000 borrower profiles** to identify statistically significant drivers of loan default and builds an executive **Power BI Dashboard** to monitor portfolio risk.

## 🛠️ Tools & Statistical Techniques Used
- **Power BI:** Power Query (ETL), Star Schema Data Modeling, DAX Measures, Interactive KPI Cards & Drill-down Visuals.
- **Python (Pandas, NumPy, SciPy):** Synthetic data engineering, Welch’s Two-Sample *t*-test, Chi-Square Test of Independence.

## 📊 Key DAX Measures Engineered
```dax
Total Loan Portfolio (₹) = SUM('bfsi_loan_credit_risk_data'[Loan_Amount_INR])

Default Rate (%) = 
DIVIDE(
    CALCULATE(COUNTROWS('bfsi_loan_credit_risk_data'), 'bfsi_loan_credit_risk_data'[Default_Status] = 1),
    COUNTROWS('bfsi_loan_credit_risk_data'),
    0
)

High Risk Exposure (₹) = 
CALCULATE(
    SUM('bfsi_loan_credit_risk_data'[Loan_Amount_INR]),
    'bfsi_loan_credit_risk_data'[Credit_Score] < 650 && 'bfsi_loan_credit_risk_data'[DTI_Ratio] > 35
)# BFSI-Credit-Risk-PowerBI-Analysis
End-to-end Credit Risk &amp; Loan Default Analysis using Power BI, DAX, and Statistical Hypothesis Testing
