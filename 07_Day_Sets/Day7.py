# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
len(it_companies)
# Find the length of the set it_companies
it_companies.add('Twitter')
# Add 'Twitter' to it_companies
it_companies.update('a', 'b')
# Insert multiple IT companies at once to the set it_companies
it_companies.remove('Google')
# Remove one of the companies from the set it_companies

# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors,
# so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
# What is the difference between remove and discard

# A.update(B)
# Join A and B
A.intersection(B)
# Find A intersection B
A.issubset(B)
# Is A subset of B
A.isdisjoint(B)
# Are A and B disjoint sets

# Join A with B and B with A
A.symmetric_difference(B)
# What is the symmetric difference between A and B

del A
del B
# Delete the sets completely

age_set = set(age)
print(len(age_set), len(age))
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Explain the difference between the following data types: string, list, tuple and set

lst = 'I am a teacher and I love to inspire and teach people'.split(' ')
word_set = set(lst)
print(lst, len(word_set))
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? You did not learn loops yet you can do it manually.