def q1():
    age = int(input('Enter your age: '))
    if age >= 18:
        print('You are old enough to learn to drive.')
    else:
        year = str(18 - age)
        print('You need ' + year + ' more years to learn to drive.')


def q2():
    my_age = 25
    your_age = int(input('Enter your age: '))
    if your_age == my_age:
        print('We are the same age.')
    elif your_age >= my_age:
        year = your_age - my_age
        if year == 1:
            print("You are 1 year older than me.")
        else:
            print('You are ' + str(year) + ' years older than me.')
    else:
        year = my_age - your_age
        if year == 1:
            print("You are 1 year younger than me.")
        else:
            print('You are ' + str(year) + ' years younger than me.')


def q3():
    a = int(input('Enter number one: '))
    b = int(input('Enter number two: '))
    if a > b:
        print(str(a) + ' is greater than ' + str(b))
    elif a < b:
        print(str(a) + ' is smaller than ' + str(b))
    else:
        print(str(a) + ' is equal to ' + str(b))


def q4():
    score = int(input('Enter the score: '))
    if 80 <= score <= 100:
        print("A")
    elif 70 <= score <= 89:
        print("B")
    elif 60 <= score <= 69:
        print("C")
    elif 50 <= score <= 59:
        print("D")
    else:
        print('F')


def q6():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruit = input('Please enter a fruit: ')
    if fruit in fruits:
        print('That fruit already exist in the list.')
    else:
        fruits.append(fruit)
        print(fruits)


def q7():
    person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    if 'skills' in person:
        print(person['skills'][len(person['skills'])//2])
    if 'skills' in person:
        has_skill =  'Python' in person['skills']
        print(has_skill)
    if person['skills'] == ['JavaScript', 'React']:
        print('He is a front end developer')
    elif person['skills'] == ['Node', 'Python', 'MongoDB']:
        print('He is a backend developer')
    elif person['skills'] == ['React', 'Node ', 'MongoDB']:
        print('He is a fullstack developer')
    else:
        print('unknown title')


def q8():
    person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    if person['is_marred'] == True and person['country'] == 'Finland':
        print(person['first_name'] + ' ' + person['last_name'] + " lives in " + person['country'] + ". He is married.")

q8()
