# Create a loop that removes the vowels from the following 
# # names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] . Add the results to a new list.

names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

vowels = 'aeouiy'

new_names_list = []

for name in names_list:
    print(name)
    for letter in name:
        if letter.lower() in vowels:
            name = name.replace(letter, "")
    print(name)
    new_names_list.append(name)

print("The new names are:\n")

for new_name in new_names_list:
    print(f"{new_name}")