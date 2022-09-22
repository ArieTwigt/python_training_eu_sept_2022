# Create list that contains the files in your current working directory
import os

files_folders = os.listdir()

files_folders_str =  " - 📄" + "\n - 📄 ".join(files_folders)

print(files_folders_str)