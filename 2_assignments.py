# assignment 1
# define the full_name
full_name = "Erling Haaland"

# possible solution 1: '+' operator
#full_name = "Erling Haaland" + " .Jr"

# possible solution 2: 'f'-string
full_name = f"{full_name} .Jr"

# assignment 2
# possible solution 1: split <string> in <list>
full_name_list = full_name.split(" ")
first_name = full_name_list[0]
last_name = full_name_list[1]
addition = full_name_list[2]

full_name_new = first_name[0] + ". " + last_name + " " + " " + addition


# possible solution 2: Same, but with f-strings
full_name_new = f"{first_name[0]}. {last_name} {addition}"
print(full_name_new)


# assignment 3
# define the variable 
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2

# possible solution 1
# (if you know the exact location)
combined_flower_list[1] = 'daisy'

# possible solution 2 (more dynamic)
# find the location of the 'daisy'
idx_tulip = combined_flower_list.index('tulip')
combined_flower_list[idx_tulip] = 'daisy'

# other solution would be a 'list comprehension' --> we be discussed during 'Loops in Python'