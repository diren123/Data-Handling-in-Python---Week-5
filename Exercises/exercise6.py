import numpy as np
import pandas as pd

df = pd.read_csv('renfe_trains.csv')

# Initial Data Inspection
# 1.
# Inspect the columns of the DataFrame. Specifically, consider the type of
# each column and whether it seems reasonable. If not, investigate why.
print(df.info())

# 2.
# It seems like we have some bad values in the price value ‘price’.
# You can see them by using the method .value_counts().
print("Output 1: ")
print(df['price'].value_counts())

print("Output 2: ")
print(df[df['price']=='price'])

# 3.
# It looks like some sort of error has meant the column names have been
# fed into the data in intervals. Let’s drop these rows as they are clearly an
# accident.
print("Output 3: ")
df = df[df['price'] != 'price']
print(df['price'].value_counts())

# 4.
# We can now represent price using the appropriate type. Convert it to
# the appropriate data type.
print("Output 4: ")
df['price'] = df['price'].astype(np.float32)
print(df.info())

# Missing Values
# 1.
# Identify whether there are missing values in the DataFrame
