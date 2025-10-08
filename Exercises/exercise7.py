import numpy as np
import pandas as pd

# Pivot Tables

# 1.
# Use a pivot table to explore how price differs with
# respect to the type of fare for each destination.
df = pd.read_csv('renfe_trains_cleaned.csv')

pivot_result = pd.pivot_table(
    df,
    values='price',
    index='fare',
    columns='destination',
    aggfunc=np.mean  # or 'mean'
).round()

print(pivot_result)

# Working with time series
# 1.
# Convert departure & arrival to a more appropriate datatype
print("Time Series Output 1: ")
df[['departure', 'arrival']] = df[['departure', 'arrival']].apply(lambda time: pd.to_datetime(time, format='%Y-%m-%d %H:%M:%S'))
print(df[['departure', 'arrival']])

# 2.
# Calculate the duration of each train journey and add it as a column called duration
print("Time Series Output 2: ")
df['duration'] = df['arrival'] - df['departure']
print(df['duration'])

# 3.
# Make departure the index of the DataFrame
print("Time Series Output 3: ")
df.set_index('departure', inplace=True)

# 4.
# Sort the index low to high (earlier to later). This
# will make slicing possible later.
print("Time Series Output 4: ")
df.sort_index(inplace=True)

# 5.
# Select all journeys which departed on 07/05/19.
print("Time Series Output 5: ")
print(df.loc['2019-05', :])

# 6.
# Select all journeys which departed on 07/05/19 to 11/05/19.
print("Time Series Ouptut 6: ")
print(df.loc['2019-05-07': '2019-05-11', :])

# 7.
# Add one year to each date in the index of the DataFrame 
# (but do not save it!)
print("Time Series Output 7: ")
print(df.index + pd.tseries.offsets.Day(365))

# 8.
# Create a subset of the DataFrame called madrid_to_barca which
# contains only journeys with origin as MADRID and destination as
# BARCELONA
print("Time Series Output 8: ")
madrid_to_barca = df[(df['origin'] == 'MADRID') & (df['destination'] == 'BARCELONA')]
print(madrid_to_barca)

# 9.
# Select only those tickets in madrid_to_barca which are in the Promo
# category for fare and Turista for vehicle_class. Update madrid_to_barca
# to only contain these
print("Time Series Output 9: ")
madrid_to_barca = df[(df['fare'] == 'Promo') & (df['vehicle_class'] == 'Turista')]
print(madrid_to_barca)

# 10.
# Compute a seven day rolling average for price for the madrid_to_barca DataFrame.
# Add it as a column called rolling.
print("Time Series Output 10: ")
madrid_to_barca.loc[:, 'rolling'] = madrid_to_barca['price'].rolling(window='7D').mean().round(2)
print(madrid_to_barca.loc[:, 'rolling'])
