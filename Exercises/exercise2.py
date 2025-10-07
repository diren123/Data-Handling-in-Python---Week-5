# Week 5: Data Handling in Python
# Exercise 2

# Display Hello World!
print("Hello World")

# Display a message using variables
username = 'Bob'
age = 32
print(username, 'is', age, 'years old')

# What's wrong here?
# username = 'Bob'
# age = 32
# print(username + 'is' + age + 'years old')

# Fix 1: print(username + 'is' + str(age) + 'years old')

# Get User Input
username = input('Please Enter Your Name: ')
age = input('Please Enter Your Age: ')
print(username, 'is', age, 'years old')

# Arithmetic Operations
# A box contains 50 crayons, which have to be distributed to 6 children.
# Each child has to get the same number of whole crayons (no breaking).
# Calculate the number of crayons each child will get.

number_of_crayons_in_a_box = 50
number_of_children = 6
crayons_per_child = int(number_of_crayons_in_a_box/number_of_children)

print('Each child will get ' + str(crayons_per_child) + ' crayons')

# Casting Variables

# 1.
# Capture user input to get the length of the first side of a rectangle.
# Use a suitable variable name such as length.
# You must cast (convert) the text you input to an integer type (int).

length = int(input("Please Enter the Length of the Length of the Rectangle: "))

# 2.
# Input the length of the second side of the rectangle.
# Use a suitable variable name such as width.
# Again, cast the input text to an integer type (int).

width = int(input("Please Enter the Length of the Width of the Rectangle: "))

# 3.
# Calculate and display the perimeter of the rectangle.

perimeter = (length * 2) + (width * 2)
print("The Perimeter of the Rectangle is: " + str(perimeter))

# Extension Activities (for Python Pros)
# 1.
# Write a piece of code which calculates the amount of change needed
# to be given from an input amount in £.
# To start you off, we’ve given you a list of denominations of UK currency.

denoms = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

get_change_from = float(input("I want change for: "))
change = []
remaining = round(get_change_from, 2)

for denom in denoms:
    count = int(remaining//denom)

    if count > 0:
        change.append((denom, count))
        remaining = round(remaining - denom * count, 2)

# Output result
print("\nChange to give: ")
for denom, count in change:
    if denom >= 1:
        print(f"£{denom:.0f} x {count}")
    else:
        print(f"{int(denom * 100)}p x {count}")

# Test Case 1: £68.37
# Answer: £50, £10, £5, £2, £1, 20p, 10p, 5p, 2p
