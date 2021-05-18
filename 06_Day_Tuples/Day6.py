empty_tpl = ()
# Create an empty tuple

bros = ('Terry', 'Larry')
siblings = ('Frank', 'Mary')
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

bros_siblings = bros + siblings
# Join brothers and sisters tuples and assign it to siblings

len(bros_siblings)
# How many siblings do you have?

family_members = siblings + ('Father', 'Mother')
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

print(siblings[0:2])
# Unpack siblings and parents from family_members

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

food_stuff_lt = list(fruits_and_vegetables)
print(food_stuff_lt)
# Change the about food_stuff_tp tuple to a food_stuff_lt list

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')