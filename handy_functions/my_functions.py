# define the function
def calculate_content(length: float, width: float , height: float) -> float:
    '''
    This function returns the content

    Params:
    * length: length of the box
    * width: width of the box
    * height: height of the box

    Returns:
    - content: the content of the box
    '''

    content = length * width * height
    return content


# define the function
def capitalize_names(names_list):
    '''
    Description
    '''

    new_names_list = []

    for name in names_list:
        new_name = name.capitalize()
        new_names_list.append(new_name)

    return new_names_list