import pandas as pd
import openpyxl
import json
import sqlite3

x = [1,3,5,7]
mySeries = pd.Series(x)
print("Outputting mySeries: ")
print(mySeries)

print("Outputting mySeries[2] value: ")
print(mySeries[2])

mySeries2 = pd.Series(x, index=[9,88,7,6])
print("Outputting mySeries2: ")
print(mySeries2)

print("Outputting mySeries2 Indices:")
print(mySeries2.index)

print("Outputting mySeries2 Values:")
print(mySeries2.values)

print("Outputting mySeries2 Location: ") # At Index 88, Fetch Value & Output
print(mySeries2.loc[88])

print("Outputting mySeries2 Location: ")
print(mySeries2.iloc[3])

data = {
    "age": [34, 42, 27],
    "height": [1.78, 1.82, 1.75],
    "weight": [75, 80, 70]
}
df = pd.DataFrame(data)
print(df)

data = {
    "Name": ['Alice', 'Bob', 'Cat'],
    "Age": [30, 43, 20],
    "City": ["Boston", "London", "Rome"]
}
df1 = pd.DataFrame(data, index = ['x', 'y', 'z'])
print(df1)
print(df1.loc['x'])

print(df1.loc[:,'City'])

print(df1.iloc[:,1])

df2 = pd.read_excel('loan_data.xlsx')
print(df2.head(5))

df3 = pd.read_excel('loan_data.xlsx', sheet_name="March")
print(df3.head(5))

# weather1 = pd.read_json("weather.json")
weather1 = json.load(open("weather.json"))
# print(weather1.head(5))

db_conn = sqlite3.connect(r"movies_db.sqlite")

print("*"*60)
movies = pd.read_sql(r"SELECT id, name, year, rating FROM movies", db_conn)
print(movies.head())

