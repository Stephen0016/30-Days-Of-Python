# Day 2: 30 Days of python programming

# Write a python comment saying 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
# Declare a last name variable and assign a value to it
# Declare a full name variable and assign a value to it
# Declare a country variable and assign a value to it
# Declare a city variable and assign a value to it
# Declare an age variable and assign a value to it
# Declare a year variable and assign a value to it
# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it
# Declare a variable is_light_on and assign a value to it
# Declare multiple variable on one line
# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
# Using the len() built-in function find the length of your first name
# Compare the length of your first name and your last name
# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable _total
# Subtract num_two from num_one and assign the value to a variable _diff
# Multiply num_two and num_one and assign the value to a variable _product
# Divide num_one by num_two and assign the value to a variable _division
# Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
# Calculate num_one to the power of num_two and assign the value to a variable _exp
# Find floor division of num_one by num_two and assign the value to a variable _floor_division
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable area_of_circle
# Calculate the circumference of a circle and assign the value to a variable circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in python shell or in your file to check for the reserved words

firstname = 'Stephen'
lastname = 'Cao'
fullname = firstname + ' ' + lastname
country = 'China'
city = 'Shanghai'
age = 25
year = 2021
is_married = False
is_true = True
is_light_on = True
height, gender = 175,'Male'
# print(fullname,height,gender)
print(type(fullname))
print(len(firstname))
print(len(firstname) > len(lastname))
num_one, num_two = 5,4
_total = num_one + num_two
_diff = num_one - num_two
_product = num_one * num_two
_division = num_one / num_two
_remainder = num_one % num_two
_exp = num_one ** num_two
_floor_division = num_one // num_two
a = input("your name?")