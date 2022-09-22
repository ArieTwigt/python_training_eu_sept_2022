# Create dictonary that contains the family of this person. 
# For each person in the family, store the same attributes as with the first person
person = {'name': 'James',
          'age': 30,
          'hobbies': ['football', 'tennis', 'walking']}

person_2 = {'name': 'Mary',
          'age': 40,
          'hobbies': ['hockey', 'running', 'gaming']}

person_3 = {'name': 'Jimmy',
          'age': 16,
          'hobbies': ['gaming', 'cook', 'cycle']}

person_4 = {'name': 'Bobby',
          'age': 3,
          'hobbies': ['pokemon', 'cars', 'eat']}



# create a dictionary for the family
family_dict = {}
family_dict['members'] = [person, person_2, person_3, person_4]
family_dict['name'] = 'Jones'

# what is the age of the third person
family_dict

print(family_dict)

names_list = ['James', 'Mary']
ages_list = [20, 30]

my_dict = dict(zip(names_list, ages_list))
