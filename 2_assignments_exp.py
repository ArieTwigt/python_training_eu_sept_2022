# assignment 1
first_name = "Erling"
last_name  = "Haaland"

# possible solution 1
full_name = first_name + " " + last_name + " .Jr" 

# possible solution 2
full_name = "{} {} .Jr".format(first_name, last_name)

# possible solution 3
full_name = f"{first_name} {last_name} .Jr"

print(full_name)


# assignment 2
# possible solution 1
full_name_new = first_name[0] + ". " + last_name + " .Jr"

# possible solution 2
full_name_new = "{} {} .Jr".format(first_name[0], last_name)

# possible solution 3
full_name_new = f"{first_name[0]}. {last_name} .Jr"

# possible solution 4
full_name_list = full_name.split(" ")
full_name_new = f"{full_name_list[0][0]}. {full_name_list[1]} {full_name_list[2]}"
print(full_name_new)

# assignment 3
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2

# solution 1: replace 'tulip' for 'daisy' --> overwrite the value
#combined_flower_list[1] = 'daisy'

# solution 2 --> more dynamic
idx_tulip = combined_flower_list.index('tulip')
combined_flower_list[idx_tulip] = 'daisy'

print(combined_flower_list)