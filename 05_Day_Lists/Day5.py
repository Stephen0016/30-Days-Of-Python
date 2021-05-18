# Exercises: Level 1

empty_lst = []
# Declare an empty list
lst1 = [1, 2, 3, 4, 5, 6]
# Declare a list with more than 5 items
len(lst1)


# Find the length of your list
def q4():
    print(lst1[0], lst1[len(lst1) // 2 - 1], lst1[-1])
    # Get the first item, the middle item and the last item of the list


mixed_data_types = ["Stephen", 25, 175, "single", "Shanghai"]
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
#
# Print the list using print()
#
# Print the number of companies in the list
#
# Print the first, middle and last company
#
# Print the list after modifying one of the companies

it_companies.append("ByteDance")
# Add an IT company to it_companies


it_companies.insert(len(it_companies) // 2 - 1, "Tencent")
# Insert an IT company in the middle of the companies list


it_companies[0] = it_companies[0].upper()
# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies2 = '#; '.join(it_companies)
# Join the it_companies with a string '#;  '

it_companies.index('Google')
# Check if a certain company exists in the it_companies list.

it_companies.sort()
# Sort the list using sort() method

it_companies.reverse()
# Reverse the list in descending order using reverse() method

it_companies_start = it_companies[0:3]
# Slice out the first 3 companies from the list

it_companies_end = it_companies[-3:]
# Slice out the last 3 companies from the list

it_companies_mid = it_companies[len(it_companies) // 2 - 1]
# Slice out the middle IT company or companies from the list

del it_companies[0]
# Remove the first IT company from the list

del it_companies[len(it_companies) // 2 - 1]
# Remove the middle IT company or companies from the list

del it_companies[-1]
# Remove the last IT company from the list

it_companies.clear()
# Remove all IT companies from the list

del it_companies
# Destroy the IT companies list

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
# Join the following lists:
#
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
#
# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
