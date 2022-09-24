import os

# Create Python script that creates a file with a few lines consisting of a story made up by yourself, use your emagination.
file_name = "my_file.txt"\

file_content = "This is a story\nThis is the second line\n"

with open(file_name, "w") as file:
    file.write(file_content)
    file.write(file_content)
    file.write(file_content)

# Read the same file in Python and store the seperate lines in a list.
with open(file_name, "r") as file:
    content_list = file.readlines()

# Combine the list to a single string, make all the words in the string uppercase and finally export this file to a new text file.
content_str = "".join(content_list)

# uppercase the content of the file
content_str_upper = content_str.upper()

# specify the file name
new_file_name = "my_text_upper.txt"

# export the file
with open(new_file_name, "w") as file:
    file.write(content_str_upper)

# Save the file in a directory that is created dynamically like in the example of this chapter
folder_name = "my_stories"

files_folders = os.listdir()

if folder_name not in files_folders:
    os.mkdir(folder_name)

file_path = f"{folder_name}/{new_file_name}"

with open(file_path, "w") as file:
    file.write(content_str_upper)

pass

