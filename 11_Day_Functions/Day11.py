def q1(num1, num2):
    return num1 + num2


def q2(r=2):
    area = 3.14 * r * r
    return 'Area of the circle with a radius of ' + str(r) + ' is ' + str(area)


def q3(*num):
    summary = 0
    for i in num:
        if type(i) == int:
            summary += i
        else:
            return 'Please enter valid numbers.'
    return summary


def q4(temp_c=26):
    temp_f = (temp_c * 9 / 5) + 32
    print(str(temp_c), 'Celcius degree -->', str(temp_f), 'Fahrenheit degree')


def q5(month=1):
    if month in range(1, 4):
        print('Spring')
    elif month in range(4, 7):
        print('Summer')
    elif month in range(7, 10):
        print('Autumn')
    else:
        print('Winter')


def q8(lst=['Asabeneh', 'Brook', 'David', 'Eyob']):
    for i in lst:
        print(i)


def q10(lst=['asabeneh', 'brook', 'david', 'eyob']):
    lst_cap = []
    for i in lst:
        lst_cap.append(i.capitalize())
    print(lst_cap)


def q16(number=100):
    number_of_even = 0
    number_of_odd = 0
    for i in range(number + 1):
        if i % 2 == 0:
            number_of_even += 1
        else:
            number_of_odd += 1
    print('# The number of odds are', str(number_of_odd))
    print('# The number of evens are', str(number_of_even))


def q18(variable):
    # empty variable
    var = ""

    # check if variable is empty
    if variable is var:
        print("Yes it is!")
    else:
        print('No it\'s not')


def q20(num=7):
    result = True
    for i in range(2,num):
        if num%i == 0:
            result = False
            break
    print('It\'s a prime number.') if result == True else print('It\'s not a prime number.')


def q21(lst):
    check = list(set(lst))
    if check == lst:
        print('All items are unique in the list.')
    else:
        print('There are some repetitive items.')


# 23.Write a function which check if provided variable is a valid python variable
# What is a valid python variable? A valid variable name? if yes use ''.isidentifier()

