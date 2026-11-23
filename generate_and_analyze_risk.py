import numpy as np
import pandas as pd
from scipy import stats

# Set seed for reproducibility
np.random.seed(42)
n = 5000

# Generate realistic synthetic BFSI Loan Dataset
data = pd.DataFrame({
    'Loan_ID': [f'LN{10000+i}' for i in range(n)],
    'Age': np.random.randint(21, 62, n),
    'Annual_Income_INR': np.random.normal(650000, 220000, n).clip(180000, 2500000).round(-3),
    'Loan_Amount_INR': np.random.normal(350000, 150000, n).clip(50000, 1500000).round(-3),
    'Interest_Rate': np.random.uniform(8.5, 22.0, n).round(2),
    'Credit_Score': np.random.normal(690, 65, n).clip(450, 850).astype(int),
    'Employment_Type': np.random.choice(['Salaried', 'Self-Employed', 'Business'], n, p=[0.6, 0.25, 0.15]),
    'City_Tier': np.random.choice(['Tier-1', 'Tier-2', 'Tier-3'], n, p=[0.45, 0.35, 0.20])
})

# Calculate Debt-to-Income (DTI) Ratio
data['DTI_Ratio'] = ((data['Loan_Amount_INR'] / 3) / data['Annual_Income_INR'] * 100).round(2)

# Risk probability logic based on statistical drivers
risk_score = (
    (700 - data['Credit_Score']) * 0.015 +
    (data['DTI_Ratio'] - 20) * 0.04 +
    (data['Interest_Rate'] - 12) * 0.12 +
    np.where(data['Employment_Type'] == 'Self-Employed', 0.4, 0)
)
prob_default = 1 / (1 + np.exp(-risk_score + 1.8))
data['Default_Status'] = np.random.binomial(1, prob_default)

# Save dataset for Power BI ingestion
data.to_csv('bfsi_loan_credit_risk_data.csv', index=False)

# --- Statistical Hypothesis Testing ---
# 1. Two-Sample Welch's t-test: Credit Score of Defaulters vs Non-Defaulters
defaulters = data[data['Default_Status'] == 1]['Credit_Score']
non_defaulters = data[data['Default_Status'] == 0]['Credit_Score']
t_stat, p_val_t = stats.ttest_ind(defaulters, non_defaulters, equal_var=False)

# 2. Chi-Square Test of Independence: Employment Type vs Default Status
contingency = pd.crosstab(data['Employment_Type'], data['Default_Status'])
chi2, p_val_chi, dof, _ = stats.chi2_contingency(contingency)

print(f"Overall Default Rate: {data['Default_Status'].mean()*100:.2f}%")
print(f"Welch's t-test (Credit Score): t = {t_stat:.4f}, p-value = {p_val_t:.4e}")
print(f"Chi-Square Test (Employment vs Default): chi2 = {chi2:.4f}, p-value = {p_val_chi:.4e}")
