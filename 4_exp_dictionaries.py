my_dict = dict()
my_dict_2 = {}

# constructing
person = {'name': 'Arie',
          'city': 'Amsterdam'}

# adding/collecting data
person['age'] = 50 
person['hobbies'] = ['cycling', 'running', 'cooking']

print(my_dict)

# return the available keys
person.keys()
person.values()

# creating a dictionary from 2 lists
names_list = ['Arie', 'Mary', 'James']
ages_list = [50, 40, 30]

people_dict = dict(zip(names_list, ages_list))

#
person_2 = {'name': 'Arie', 'age': 50}
person_3 = {'name': 'Jim', 'age': 40}
person_4 = {'name': 'James', 'age': 30, 'hobbies': ['cycling', 'running', 'cooking']}

person_list = [person_2, person_3]
# brackets python
# structures
# - [] = lists
# - {} = dictionaries
# - () = tuple

# operations
# - [] = data selection
# - {} = formatting strings
# - () = applying functions or callings methods