def q1():
    age = 25   # Declare your age as integer variable
    height = 1.75   # Declare your height as a float variable
    asd = 1 + 1j   # Declare a complex number variable


def q4():
    print("Enter the base of the triangle")
    base = input()
    print("Enter the height of the triangle")
    height_tri = input()
    area = 0.5 * float(base) * float(height_tri)
    print('Area is', int(area))
    # Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    #     Enter base: 20
    #     Enter height: 10
    #     The area of the triangle is 100


def q5():
    print('Enter three sides in a row')
    side_a, side_b, side_c = input(), input(), input()
    perimeter = int(side_a) + int(side_b) + int(side_c)
    print('Perimeter is', perimeter)
    # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    # Enter side a: 5
    # Enter side b: 4
    # Enter side c: 3
    # The perimeter of the triangle is 12


def q6():
    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    area = length * width
    perimeter = 2 * (length + width)
    print("Area is",area, ". Perimeter is", perimeter)
    # Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))


def q7():
    radius = int(input("Enter a radius: "))
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    print("Area is", area, "Circumference is", circumference)
    # Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
# Find the length of 'python' and 'jargon' and make a falsy comparison statement.


def q13():
    print('on' in 'python' and 'on' in 'jargon')
    # Use and operator to check if 'on' is found in both 'python' and 'jargon'


def q14():
    print('jargon' in 'I hope this course is not full of jargon.')
    # I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.


# There is no 'on' in both dragon and python


def q16():
    print(str(float(len('python'))))
    # Find the length of the text python and convert the value to float and convert it to string


def q17():
    check = int(input("Input a number: "))
    check_even = check/2 == check//2
    print(check_even)
    # Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?


# The floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to 10
# Check if int('9.8') is equal to 10
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume someone lives up to hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.

def q23():
    print(" 1 1 1 1 1\n 2 1 2 4 8\n 3 1 3 9 27\n 4 1 4 16 64\n 5 1 5 25 125" )
    # Write a python script that displays the following table
    # 1 1 1 1 1
    # 2 1 2 4 8
    # 3 1 3 9 27
    # 4 1 4 16 64
    # 5 1 5 25 125
