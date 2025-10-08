import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

print(pd.__version__)

df = pd.DataFrame({
    'participant': [1,2,3,4],
    'age': [50, None, 30, np.nan],
    'satisfaction': [None, 8, 9, None]
})

print("Data Frame: ")
print(df)

print("True/False: ")
# .isna() any() sum()
print(df.isna().any())

print("Output 3: ")
print(df.isna().sum())

# dropna()
print("Testing dropna(): ")
print(df.dropna())

print("Testing dropna() 2: ")
print(df.dropna(thresh = 2))

# fillna()
print("Entire Data Frame: ")
print(df)

print("Testing fillna(): ")
print(
    df.fillna({
        'age': df['age'].mean(),
        'satisfaction': df['satisfaction'].mode()[0]
    })
)

# duplicated()
loan_dup = pd.read_excel('loan_data.xlsx')
print("Loan Duplicate Data: ")
print(loan_dup)

print("Duplicates Output 1: ")
print(loan_dup.duplicated(subset = ['Income']).sum())

print("Duplicates Output 2: ")
print(loan_dup.duplicated(keep = "last").sum())

df1 = pd.read_excel('loan_data.xlsx')
print(df1)

print("Axis 1 Testing: ")
print(df1.drop("ID", axis=1)) # axis 0 is row, axis 1 is columns

print("Axis 0 Testing")
print(df1.drop(0, axis=0).head())

# replace()
print("Testing Replace: ")
print(df1.replace(to_replace = {
    'Long Term': '12 Month',
    'Short Term': '6 Month'
}).head())

print("Lamda Function: ")
print(df1.select_dtypes(np.number).apply(lambda col: col.round(2)))

