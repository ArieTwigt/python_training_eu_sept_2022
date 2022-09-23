

def remove_vowels_from_list(names_list: list) -> list:
    '''
    This function removes the vowels from every value in the list

    Parameters:
    * names_list

    Returns
    * list with names in which the vowels are removed
    
    '''

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
    
    return new_names_list