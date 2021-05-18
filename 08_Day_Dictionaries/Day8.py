dog = {}
# Create an empty dictionary called dog
dog['name'], dog['color'], dog['breed'], dog['legs'], dog['age'] = 'Puppy', 'white', 'akita', 'long', 4
print(dog)
# Add name, color, breed, legs, age to the dog dictionary
student = {'first_name': 'Stephen',
           'last_name': 'Cao',
           'gender': 'Male',
           'age': 25,
           'marital_status': 'unmarried',
           'skills': ['Python', 'Java', 'CSS'],
           'country': 'China',
           'city': 'Shanghai',
           'address': {
               'street': 'Collins St',
               'zipcode': '3008'
           }}
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
print(len(student))
# Get the length of the student dictionary
print(student['skills'], type(student['skills']))
# Get the value of skills and check the data type, it should be a list
student['skills'].append('SQL')
print(student['skills'])
# Modify the skills values by adding one or two skills
print(student.keys())
# Get the dictionary keys as a list
print(student.values())
# Get the dictionary values as a list
print(student.items())
# Change the dictionary to a list of tuples using items() method
del student['first_name']
# Delete one of the items in the dictionary
del student
# Delete one of the dictionaries
