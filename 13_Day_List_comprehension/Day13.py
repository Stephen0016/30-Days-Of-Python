def q1():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    result = [i for i in numbers if i <= 0]
    print(result)


def q2():
    list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    list_of_sublist = [i for lst in list_of_lists for i in lst]
    result = [i for lst in list_of_sublist for i in lst]
    print(result)


def q3():
    result = [(i ** 1, i ** 0, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
    print(result)


def q4():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    tuples_in_lists = [i for lst in countries for i in lst]
    result = [i for tpls in tuples_in_lists for i in tpls]
    print(result)


def q5():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    list_of_tuples = [i for lst in countries for i in lst]
    result = []
    for i in list_of_tuples:
        result.append({'country': i[0].upper(), 'city': i[1].upper()})
    print(result)


def q6():
    names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    result = []
    list_of_tuples = [i for lst in names for i in lst]
    for i in list_of_tuples:
        result.append(i[0]+' '+i[1])
    print(result)


def q7():
    pass    # cant make it, for reference as below
            # https://stackoverflow.com/questions/63867325/is-there-a-way-to-find-the-slope-and-the-y-intercept-of-the-best-fit-line-line