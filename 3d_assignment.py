# Add a directory with the name our_functions
import os

files_folders = os.listdir()

folder_name = input("Name of the new folder: \n")

if folder_name not in files_folders:
    print(f"Creating {folder_name}")
    os.mkdir(folder_name)
    print(f"✅ Folder {folder_name} created")
else:
    print(f"❌ The folder {folder_name} already exists")

# If you would like to create folders and sub-folders, can also be used with the 'exist_ok' param
# - os.makedirs()