# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here

#creating a dataframe called bank
bank = pd.read_csv(path, sep=',', delimiter=None, names=None, index_col=None, usecols=None)
print(bank.head(5))
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)





# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis=1)
print(banks.head(5))
print(banks.isnull().sum())

bank_mode = banks.mode()
print(bank_mode)

for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)

print(banks.isnull().sum())
#banks[bank_mode].apply(lambda x:x.fillna(x.mode, inplace=True))

#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, index=['Gender','Married','Self_Employed'], values = 'LoanAmount', aggfunc='mean')
print(avg_loan_amount)



# code ends here



# --------------
# code starts here
#loan_approved_subset = ((banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y'))
#print(loan_approved_subset)

#df[df['Legendary'] == True]['Type 1'].value_counts().idxmax()

#loan_approved_se = ((banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')).count()
loan_approved_se = ((banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')).sum()
print(loan_approved_se)

loan_approved_nse = ((banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')).sum()
print(loan_approved_nse)

percentage_se = (loan_approved_se * 100) / 614
percentage_nse = (loan_approved_nse * 100) / 614

print(percentage_se)
print(percentage_nse)

# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x)/12) 
print(loan_term)

big_loan_term = len(banks[loan_term >= 25])
print(big_loan_term)

# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome','Credit_History']]
#print(loan_groupby)
mean_values = loan_groupby.mean()
print(mean_values)



# code ends here


