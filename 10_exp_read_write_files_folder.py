# import the require libraries
import os

# specify the filename and folder name
my_text = input("Specify your text\n")
file_name = input("To which file?\n")
folder_name = input("To which folder? (texts)\n") or 'texts'
mode = input("Write or append? ('a'/'w') (default is 'a')") or 'a'


# compose the full path
full_path = f"{folder_name}/{file_name}.txt"

# list the current files and folders
files_folders = os.listdir()

# check if the folder already exists
if folder_name not in files_folders:
    os.mkdir(folder_name)


# export the content to the file
with open(full_path, mode) as file:
    print(f"Writing to {full_path}")
    file.write(my_text)

print(f"Succesfully written to {full_path}")
