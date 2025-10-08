# Week 5: Data Handling in Python
# Exercise 5: Introduction to Pandas

import numpy as np
import pandas as pd
import openpyxl
import json

# Series
# 1.
# Create a Series from the Below List:
attempts = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]

attempts = pd.Series(attempts)

print(attempts)

# 2.
# Find the first person’s number of attempts.
print(attempts[0])

# 3.
# Find the first five people
print(attempts[:5])

# 4.
# Find the last three people's number of attempts
print(attempts[-3:])

# DataFrames

# 1.
# Create and display a DataFrame from the below dictionary exam_data

exam_data = {'name': ['Anne', 'Kofi', 'Ridhwaan', 'Zara',
'Muhammad', 'Donald', 'Isabella', 'Sarah', 'Paula', 'John'],
'score': [12.5, 9, 16.5, None, 9, 20, 14.5, None, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no',
'no', 'yes']}

labels = ['Student ' + letter for letter in ['a', 'b', 'c', 'd',
'e', 'f', 'g', 'h', 'i', 'j']]

exam = pd.DataFrame(exam_data)
print("Creating and displaying a data frame from the exam_data dictionary to display the data: ")
print(exam)

# 2.
# Display the first three rows of the data frame
print("Displaying the first three rows of the data frame: ")
print(exam.loc[:2, :])

# 3.
# Display the name and score columns of the data frame
print("Displaying the name and score columns of the data frame: ")
print(exam[['name', 'score']])

# 4.
# Display the name and score columns and rows 1,3,4, and 8
print("Displaying the name and score columns and rows 1,3,4,and 8: ")
print(exam.loc[[1,3,4,8], ['name', 'score']])

# 5.
# Display the rows where the number of attempts is greater than 2
print("Displaying the rows where the number of attempts is greater than 2: ")
print(exam[exam['attempts']>2])

# 6.
# Displaying the rows where score is greater or equal than a pass rate of 10
print("Displaying the rows where score is greater than or equal than a pass rate of 10: ")
print(exam[exam['score']>=10])

# 7. Display the rows where the score is above 15 and the student
# has only made one attempt.
print("Displaying the rows where the score is above 15 and the student has made only one attempt: ")
print(exam[(exam['score']>10) & (exam['attempts'] == 1)])

# 8.
# Set the index of the DataFrame so it is given by labels.
# Hint: df.index = …
# Return the name of student d.

print("Setting the index of the DataFrame so it is given by labels: ")
exam.index = labels
print(exam.loc["Student d", "name"])

# Reading in data
# 1.
# Read the file mortgage_applicants.csv, which sits in the data folder,
# into a variable called mortgage.
# NOT DONE AS I DON'T HAVE THE CSV FILES

# 2.
# Read the file mortgage_applicants.xlsx, which sits in the data folder,
# into a variable called mortgage.
mortgage = pd.read_excel('mortgage_applicants.xlsx')
print("Data in Mortgage Displayed: ")
print(mortgage)

# 3.
# Some weather data is held in a file called weather_data.json. Read it
# into a dataframe called weather.
# weather = json.load(open("weather_data.json"))
weather = pd.read_json("weather_data.json")
print("Weather Data Displayed: ")
print(weather)

# Changing types and parsing items
# 1.
# What data type has each column in mortgage been read in as? Use a method to find out
print("Data types for each column in mortgage: ")
print(mortgage.info())

# 2.
# Convert the ID column so that it is instead represented as a Unicode
# string. Hint: the type is denoted ‘U’
print("Converting the ID column so that it is instead represented as a Unicode string: ")
mortgage = mortgage.astype({'ID': 'string'})
print(mortgage.info())

# 3.
# Convert the day column of the weather Dataframe to an appropriate type
weather['day'] = pd.to_datetime(weather['day'], format='%Y-%m-%d')
print("Converting the day column of the weather Dataframe to an appropriate type: ")
print(weather.info())

# Retrieving rows and columns

# 1.
# Select the Score column of the mortgage DataFrame.
print("Selecting the Score column of the mortgage DataFrame: ")
print(mortgage['Score'])

# 2.
# Selecting the Balance and Income columns
print("Selecting the Balance and Income columns: ")
print(mortgage[['Balance', 'Income']])

# 3.
# Selecting the first row in the mortgage DataFrame
print("Selecting the first row in the mortgage DataFrame: ")
print(mortgage.iloc[0, :])

# 4.
# What is the Debt of the first applicant?
print("Debt of the first applicant: ")
print(mortgage.loc[0, 'Debt'])

# 5.
# What is the Balance and Income of the 10th to 20th applicants?
print("Balance and Income of the 10th to 20th applicants: ")
print(mortgage.loc[10:20, ['Balance', 'Income']])

# 6.
# What are the final 5 people's Scores?
print("Scores of the final 5 people: ")
print(mortgage.iloc[-5:,6])

# 7.
# Using weather, display the weather on the most recent day
print("Weather on the most recent day: ")
print(weather[-1:])

# Querying DataFrames
# 1.
# Compute the monthly earnings of mortgage applicants, just using Income
print("Monthly earnings of mortgage applicants using Income only: ")
print(mortgage['Income']/12)

# 2.
# Ratio of debts to assets for each mortgage applicant
print("Ratio of debts to assets for each mortgage applicant: ")
print(mortgage['Debt']/mortgage['Balance'])

# 3.
# Display all mortgage applicants who have a Balance greater than £1000
print("All mortgage applicants who have a Balance greater than £1000: ")
print(mortgage[mortgage['Balance']>1000])

# 4.
# Display all mortgage applicants who have a Balance greater than £1000 and a Debt below £50
print("Displaying all mortgage applicants who have a Balance greater than £1000 and a Debt below £50: ")
print(mortgage[(mortgage['Balance'] > 1000) & (mortgage['Debt'] < 50)])

# 5.
# Display all loan applicants who have an Income greater than 30,000 who have a 10-year loan, and those with an Income greater than 20,000 who have a 20-year loan (together!)
print("Display all loan applicants, who have an Income greater than 30,000 who have a 10-year loan, and and those with an Income greater than 20,000 who have a 20-year loan: ")
print(mortgage[((mortgage['Income']>30000)&(mortgage['Term']=='10 Years'))|((mortgage['Income']>20000)&(mortgage['Term']=='20 Years'))])

# Aggregating Data Frames
# 1.
# Compute the average Balance of mortgage applicants depending on the Term of their loan
print("Computing the average Balance of mortgage applicants depending on the Term of their loan: ")
print(mortgage[['Balance', 'Term']].groupby('Term').mean())
