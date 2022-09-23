# Define a function that returns the contents (e.g. in m3) of a box. It takes 3 parameters: (1) Length, (2) width and (3) heigth
from handy_functions.my_functions import calculate_content, capitalize_names


# use the function
calculate_content(10, 3, 5)


# Define a function that accepts a lists, capitalizes every name in the list, and retuns this capitalized list. You can use: ['Jim', 'John', 'Marc', 'Danny', 'Peter']
my_list = ['jim', 'john', 'marc', 'danny', 'peter']

my_new_list = capitalize_names(my_list)


# normal loop to update a list
for idx, name in enumerate(my_new_list):
    my_new_list[idx] = name.upper()

# list comprehension to update a list
[name.lower() for name in my_new_list]

# 
numbers_list = [10, 20, 30, 40, 50]

numbers_list = [number for number in numbers_list if number < 30]

pass
