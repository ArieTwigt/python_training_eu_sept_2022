import math
import datetime
import os

# power function
math.pow(3,3)

# get the current date
date_today = datetime.date.today()
date_later = date_today + datetime.timedelta(days=1000)

# subtract dates
my_birthday = datetime.date(1990, 5, 21)
difference = date_today - my_birthday

# exp strftime
my_birthday.strftime("%Y-%m-%d it was %A")

# create a folder from Python
folder_name = "my_folder"
files_folder = os.listdir()

if folder_name not in files_folder: 
    print(f"Creating folder {folder_name}")
    os.mkdir("my_folder")


None