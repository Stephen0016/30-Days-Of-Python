challenge = 'Thirty ' + 'Days ' + 'Of ' + 'Python '
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

company = 'Coding For All'  # Declare a variable named company and assign it to an initial value "Coding For All".


def q4():
    print(company)
    # Print the variable company using print().


def q5():
    print(len(company))
    # Print the length of the company string using len() method and print().


def q6():
    result = challenge.upper()
    # Change all the characters to capital letters using upper() method.


def q7():
    result = challenge.lower()
    # Change all the characters to lowercase letters using lower() method.


def q8():
    print(company.capitalize().title().swapcase())
    # Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.


def q9():
    result = company[7:]
    print(result)
    # Cut(slice) out the first word of Coding For All string.


def q10():
    result = company.index('Coding')
    print(result)
    # Check if Coding For All string contains a word Coding using the method index, find or other methods.


def q11():
    result = company.replace('Coding', 'Python')
    print(result)
    # Replace the word coding in the string 'Coding For All' to Python.    https://docs.python.org/3/library/stdtypes.html#str.split


# Change Python for Everyone to Python for All using the replace method or other methods.

def q13():
    result = company.split()
    print(result)
    # Split the string 'Coding For All' using space as the separator (split()) .


def q14():
    origin = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
    print(origin.split(','))
    # "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.


def q15():
    result = company[0]
    print(result)
    # What is the character at index 0 in the string Coding For All.


def q16():
    result = company[-1]
    print(result)
    # What is the last index of the string Coding For All.


def q17():
    result = company[10]
    print(result)
    # What character is at index 10 in "Coding For All" string.


# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.

def q23():
    sentence = 'You cannot end a sentence with because because because is a conjunction'
    print(sentence.index('because'))
    # Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

def q28():
    result = company.startswith('Coding')
    print(result)
    # Does ''Coding For All' start with a substring Coding?


def q29():
    result = company.endswith('Coding')
    print(result)
    # Does 'Coding For All' end with a substring coding?


def q30():
    result = '   Coding For All      '.strip(' ')
    print(result)
    # '   Coding For All      '  , remove the left and right trailing spaces in the given string.


def q31():
    print('30DaysOfPython'.isidentifier(), 'thirty_days_of_python'.isidentifier())
    # Which one of the following variables return True when we use the method isidentifier():
    # 30DaysOfPython
    # thirty_days_of_python


def q32():
    result = '# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])
    print(result)
    # The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.


def q33():
    print('I am enjoying this challenge.\nI just wonder what is next.')
    # Use the new line escape sequence to separate the following sentences.
    # I am enjoying this challenge.
    # I just wonder what is next.


def q34():
    print('Name\tAge\tCountry\nAsabneneh\t250\tFinland')
    # Use a tab escape sequence to write the following lines.
    # Name      Age     Country
    # Asabeneh  250     Finland


def q35():
    radius = 10
    area = 3.14 * radius ** 2
    print('The area of a circle with radius {} is {} meters square.'.format(radius, int(area)))
    # Use the string formating method to display the following:
    # radius = 10
    # area = 3.14 * radius ** 2
    # The area of a cricle with radius 10 is 314 meters square.


def q36():
    num1 = 8
    num2 = 6
    print('{} + {} = {}'.format(num1, num2, num1 + num2))
    print('{} - {} = {}'.format(num1, num2, num1 - num2))
    print('{} * {} = {}'.format(num1, num2, num1 * num2))
    print('{} / {} = {}'.format(num1, num2, num1 / num2))
    print('{} % {} = {}'.format(num1, num2, num1 % num2))
    print('{} // {} = {}'.format(num1, num2, num1 // num2))
    print('{} ** {} = {}'.format(num1, num2, num1 ** num2))
    # Make the following using string formating methods:
    # 8 + 6 = 14
    # 8 - 6 = 2
    # 8 * 6 = 48
    # 8 / 6 = 1.33
    # 8 % 6 = 2
    # 8 // 6 = 1
    # 8 ** 6 = 262144


q36()
