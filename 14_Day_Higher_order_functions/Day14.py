import functools
import string

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def q1():
    pass
    # map every items in iterable, filter the satisfied items, reduce until there is only 1 item


def q2():
    pass
    # higher order function     take functions as parameters
    # closure
    # decorator    add new functionality without modifying the function itself


def upper_list(x):
    return x.upper()


def square(x):
    return x**2


def has_land(country):
    if 'land' in country:
        return True
    return False


def six_characters(word):
    if len(word) == 6:
        return True
    return False


def starts_with_e(word):
    if word.startswith('E'):
        return True
    return False


def add_two_nums(x, y):
    return int(x) + int(y)


def combine_list(x,y):
    return x+', '+y


def q456():
    for name in names:
        print(name, end=' ')
    print()
    for country in countries:
        print(country, end=' ')
    print()
    for number in numbers:
        print(number, end=' ')
    print()


def q7():
    result = list(map(upper_list, countries))   # tips: not upper_list()
    print(result)


def q8():
    result = list(map(square, numbers))
    print(result)


def q9():
    pass    # same as q7


def q10():
    result = list(filter(has_land, countries))
    print(result)


def q11():
    result = list(filter(six_characters, countries))
    print(result)


def q12():
    pass    # same as q11


def q13():
    result = list(filter(starts_with_e, countries))
    print(result)


def q14():
    pass    # dont understand


def q15(lst):
    result = []
    for i in lst:
        if type(i) == str:
            result.append(i)
    print(result)


def q16():
    result = functools.reduce(add_two_nums, numbers)   # remember to import
    print(result)


def q17():
    result = functools.reduce(combine_list, countries)
    print(result)


def q18():
    pass  # same as q10


def q19(country_list):
    result = {}
    content = []
    for i in string.ascii_letters[26:52]:
        for country in countries:
            if country.startswith(i):
                content.append(country_list)
        result[i] = content
        content = []
    print(result)


def q20(country_list):
    result = []
    for i in range(10):
        result.append(country_list[i])
    print(result)


def q21(country_list):
    result = []
    for i in range(10):
        result.append(country_list.pop())
    print(result)


