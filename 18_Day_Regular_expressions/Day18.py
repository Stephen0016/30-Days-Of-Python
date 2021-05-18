import re
from collections import Counter


def q1_counter(paragraph=None):
    if paragraph is None:
        paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
    lst = paragraph.replace('.', '').split(' ')
    count = Counter(lst)
    most_occur = count.most_common()
    print(most_occur)


def q1(paragraph=None):
    if paragraph is None:
        paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
    lst = paragraph.replace('.', '').split(' ')
    result = []
    new_result = []
    found = False
    for word in lst:
        for sublist in result:
            if word == sublist[1]:
                found = True
                sublist[0] += 1
                break
        if not found:
            result.append([1, word])
        found = False
    result.sort(reverse=True)
    for sublist in result:
        sublist = tuple(sublist)
        new_result.append(sublist)
    # print(new_result)
    return new_result


def q2():
    points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
    int_points = []
    for i in points:
        int_points.append(int(i))
    int_points.sort()
    distance = int_points[-1] - int_points[0]
    print(distance)


def q3(str=None):
    if str is None:
        str = input('Please enter an identifier: ')
    regex = r'^[a-zA-Z_]\w*$'
    if re.search(regex, str):
        print('Valid identifier')
    else:
        print('Invalid identifier')


def q4():
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
    clean_text = re.sub(r'[-()#/@;:<>%$&!{}=~|.?,]', '', sentence)
    print(clean_text)
    print(q1(clean_text)[0:3])


