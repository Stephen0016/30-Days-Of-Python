def q1():
    j = 0
    for i in range(11):
        print(i, end=' ')
    print()
    while j < 11:
        print(j, end=' ')
        j += 1


def q2():
    j = 10
    for i in range(10, -1, -1):
        print(i, end=' ')
    print()
    while j >= 0:
        print(j, end=' ')
        j -= 1


def q3():
    for i in range(7):
        print('#' * i)


def q4():
    for i in range(8):
        for j in range(8):
            print('# ', end='')
        print()


def q5():
    for i in range(11):
        print(str(i) + ' * ' + str(i) + ' = ' + str(i * i))


def q6():
    for i in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
        print(i)


def q7():
    for i in range(0, 101):
        if i % 2 == 0:
            print(i)


def q8():
    for i in range(0, 101):
        if i % 2 == 1:
            print(i)


def q9():
    summary = 0
    for i in range(101):
        summary += i
    print(summary)


def q10():
    summary_even, summary_odd = 0,0
    for i in range(101):
        if i%2 ==0:
            summary_even += i
        else:
            summary_odd += i
    print('The sum of all even is '+ str(summary_even) + '. And the sum of all odds is '+ str(summary_odd))


def q12():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits_reverse = []
    for i in range(len(fruits)):
        fruits_reverse.append(fruits.pop())
    print(fruits_reverse)

