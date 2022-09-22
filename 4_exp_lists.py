# multiple ways to define a list
my_list = list()
my_list_2 = []

# add an element to 'my_list'
my_list.append(4)
my_list.append("Enschede") # elements of a list do no have to be of the same type

numbers_list = [1,2,3,4,5]
my_list.append(numbers_list)

numbers_list.sort() # sort, is a method of a list
sorted(numbers_list, reverse=False) # is a global function

# get the unique values, apply the set, and list
list(set(my_list))

#
names_list = ['Jim', 'Arie', 'Zeno', 'Marc']

# the 'list()' function can be used to convert to a list
name = "Arie"
name_letter_list = list(name)

a= 10