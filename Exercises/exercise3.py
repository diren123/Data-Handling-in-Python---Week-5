# Week 5: Data Handling in Python
# Exercise 3: Data Structures, Flow Control, Functions & Basic Types

# Data Structures - Lists
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

# 1.
# Record the length of the ages list in a variable. Display the length.
length_of_list_ages = len(ages)

# 2.
# # Display the first element of the ages list.
print(ages[0])

# 3.
# Display the last element of the ages list.
print(ages[length_of_list_ages - 1])

# 4.
# Find the ages from the third to the last
print(ages[3:])

# 5.
# Show the first 10 ages backwards
# SOLUTION 1
print(ages[10::-1])

# SOLUTION 2
backward_counter = 9

while(backward_counter > -1):
    print(ages[backward_counter])
    backward_counter -= 1

# 6.
# Spot the missing value in the list of odd numbers and insert it. Hint: .insert()
# SOLUTION 1
odd = [1,3,5,7,9,11,15,17,19,21]
odd.insert(6,13)

# SOLUTION 2
odd = [1,3,5,7,9,11,15,17,19,21]
missing_value = 1

for count in range(len(odd)):
    if odd[count] == missing_value:
        missing_value += 2
    else:
        odd.insert(6,13)
        print("The missing value is: ", missing_value)
        break

# Data Structures - Strings
# 1.
# Spell the greeting backwards. Hint: [::]
greeting = 'Hello'
print(greeting[::-1])

# 2.
# Spell the name of the UK observing which letters should be capital and which lowercase.
UK = 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND'

print(UK.title())

# 3.
# Find the position of the first occurence of the word 'forever'
byron = 'Fare thee well and if forever still forever fare thee well'
print(byron.find('forever'))

# Data Structure = Tuples
# 1.
# Create a tuple with your favourite desserts (at least 3 of them!)
desserts = 'tiramisu', 'ice cream', 'biscuit pudding'

# 2.
# Print the number of your favourite desserts
print(len(desserts))

# 3.
# Print the second of the desserts
print(desserts[1])

# 4.
# Print the last of the desserts
print(desserts[len(desserts) - 1])

# 5.
# Print the first two desserts
print(desserts[:2])

# 6.
# Check if pancakes are included in the desserts
print('pancakes' in desserts)

# 7.
# Write code to ask a customer for their dessert preference and respond depending on its availability. Hint: You need ifs and elses
customer_dessert_preference = input("What dessert do you want? ")

if customer_dessert_preference in desserts:
    print("Dessert Available! :D")
else:
    print("Dessert Not Available :/")

# 8.
# Once a tuple is created, you cannot change its values. Tuples are
# immutable (unchangeable). But there is a workaround! You can convert
# the tuple into a list, change the list, and convert the list back into a
# tuple.

# Change the second dessert to something else.

desserts = list(desserts)
desserts[1] = 'treleche'
desserts = tuple(desserts)
print(desserts)

# Data Structures - Dictionaries
books = {
    "title": "Hamlet",
    "author": "William Shakespeare",
    "language": "English"
}

# 1.
# Print the title value
print(books['title'])

# 2.
# Get a list of the keys of the dictionary
print(books.keys())

# 3.
# Get a list of the values of the dictionary
print(books.values())

# 4.
# Get a list of the key-value items
print(books.items())

# 5.
# Change the title to ‘King Lear’ and check that the dictionary is updated.
books['title'] = 'King Lear'
print(books)

# Selection

# 1.
# Create an IF statement to see if the person’s age is equal to 18 or over.
# Display: You are in category A.
age = 40

if age >= 18:
    print('You are in Category A')

# 2.
# Create an IF statement to see if the person’s age is equal to 16 or over.
# Display: You are in category B.
age = 40

if age > 16:
    print('You are in Category B')

# 3.
# Create an IF statement to see if the person is under 16 years of age.
# Display: You are in category C.
age = 15

if age < 16:
    print('You are in Category C')

# 4.
# Create an if…elif statement to examine the age in one statement.

age = 19

if age >= 18:
    print('You are in Category A')
elif age > 16:
    print('You are in Category B')
else:
    print('You are in Category C')

# While Loops

# 1.
# Create a variable i with the value 1.
# Write a while loop that starts at 1 and ends at 100.
# Within the while loop calculate and display each number and its square.
# End the loop if that square is bigger than 2000.
i = 1

while i < 100:
    square = i ** 2
    if square > 2000:
        break
    print(square)
    i += 1

# 2.
# Calculate how many years it will take an initial investment of £100 to
# grow to a target value of £1000 if the interest rate is 10%.
# Tip: Don’t start writing code until you’ve got a plan of action!
# Make your calculation easier to understand by defining the following
# variables:
# • Initial investment
# • Target value
# • Interest rate

start = float(input("Initial Investment: "))
target = float(input("Target Value: "))
interest = int(input("Interest Rate [%]: "))
interest = interest/100

year = 0
current = start
while current < target:
    year += 1
    current *= (1 + interest)
    print("year", year, "value", round(current,2))

#  For Loops

# Average
# 1.
# Create a list of numbers using a for loop and compute their average.
list_of_numbers = [1,5,3,8,4,7,9,2]

addition = 0
for num in list_of_numbers:
    addition += num
average = addition/len(list_of_numbers)
print("The average value of the list of numbers is: ", average)

# Combinations
sizes = ['Large', 'Medium', 'Small']
garments = ['Shirt', 'Jacket', 'Trousers']

for i in sizes:
    for j in garments:
        print(i,j)

# Functions
# 1.
# Write a function that takes a string as an argument and returns the
# string in uppercase.

text = str(input("Please Enter a String You Want to Convert to Uppercase: "))

def make_upper_case(text):
    return text.upper()

print(make_upper_case(text))

# 2.
# Update the function so that when nothing is passed to the function, the
# argument defaults to an empty string.
# Check that the output of this updated function is 0 when nothing is
# passed to it.

def make_upper_case(text = ""):
    return text.upper()

print(make_upper_case(text))

# File Handling

# 1.
# Read the file data.txt

data = open('data.txt', 'r').read().split('\n')
print(data)

# 2.
# Calculate the sum, minimum, maximum, and the average of the values
# in the file. Hint: All data read in from the file will be of string type

data = open('data.txt', 'r')
nums = []

for num in data:
    nums.append(int(num))
print("Sum: ", sum(nums))
print("Min: ", min(nums))
print("Max: ", max(nums))
print("Avg: ", sum(nums)/len(nums))

data.close()

# 3.
# Output the results to a newly created 
# &
# 4.
# Close the file

file = open('new.txt', 'w')

file.write("Sum: " + str(sum(nums)) + "\n")
file.write("Min: " + str(min(nums)) + "\n")
file.write("Max: " + str(max(nums)) + "\n")
file.write("Avg: " + str(sum(nums)/len(nums)) + "\n")

file.close()

# Append Output File
# Adults only! Ask a customer their age. If they are at least 18 years old,
# print ‘Welcome’
# Otherwise, print ‘Please come back in X years’, where X is the
# remaining time until they turn 18.
# In addition to the screen output, send the output to a text file, adding
# every response to the file.

a = open("age_output.txt", 'a')

age_limit = 18
customers_age = int(input("Please Enter Your Age: "))

if (customers_age >= age_limit):
    print("Welcome!")
    a.write("Age: " + str(customers_age) + '  -->  ')
    a.write("Welcome\n")
else:
    print("Please Come Back In " + str(age_limit - customers_age) + " years")
    a.write("Age: " + str(customers_age) + '  -->  ')
    a.write("Please Come Back In " + str(age_limit - customers_age) + " years\n")

# Extension Activites (for Python Pros)

# Exercise 1: Sets
# 1.
# Create a set containing fruit
fruits = {'banana', 'kiwi', 'orange'}
print(fruits)

# 2.
# Add another fruit to the set and print it.
fruits.add('mango')
print(fruits)

# 3.
# Loop through the set of fruit and print each element.
for fruit in fruits:
    print(fruit)

# 4.
# Consider the following sets
s1 = {'A', 'B', 'C', 'D', 'E'}
s2 = {'D', 'E', 'F', 'G'}

# 5.
# Find and print set S3, which contains all elements belonging to either
# S1 and S2.
