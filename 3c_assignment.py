# Create list that contains the files in your current working directory
import os

files_folders = os.listdir()

files_folders_str =  " - 📄" + "\n - 📄 ".join(files_folders)

print(files_folders_str)

# if you would like to check if a an element in the list is a file or folder
# - os.path.isfile("my_script.py")
# - os.path.isdir("my_folder")