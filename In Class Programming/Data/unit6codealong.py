import pandas as pd
import numpy as np

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