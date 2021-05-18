from random import randint, random
import string
import random


def q1():
    lst_letters = list(string.ascii_letters)
    lst_numbers = list(string.digits)[1:]
    random_id = ''
    for i in range(6):
        ran = random()
        if ran > 0.5:
            random_id += str(lst_numbers[randint(0, 8)])
        else:
            random_id += str(lst_letters[randint(0, 51)])
    print(random_id)


def q2():
    lst_letters = list(string.ascii_letters)
    lst_numbers = list(string.digits)[1:]
    random_id = ''
    number_of_id = int(input('Please enter the number of IDs: '))
    number_of_characters = int(input('Please enter the number of characters: '))
    for j in range(number_of_id):
        for i in range(number_of_characters):
            ran = random()
            if ran > 0.5:
                random_id += str(lst_numbers[randint(0, 8)])
            else:
                random_id += str(lst_letters[randint(0, 51)])
        print(random_id)
        random_id = ''


def q3():
    print('rgb(' + str(randint(0, 255)) + ',' + str(randint(0, 255)) + ',' + str(randint(0, 255)) + ')')


def q4():
    pass  # same way as q2


def q5():
    pass  # loop q3


def q6():
    pass  # same way as q5


def q7(lst=None):
    if lst is None:
        lst = ['r', 'a', 'n', 'd', 'o', 'm']
    random.shuffle(lst)
    return lst


def q8():
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    for i in range(7):
        result.append(number.pop(randint(0, len(number) - 1)))
    print(result)



