# basic way of writing to a file
file = open("my_story.txt", 'a')
file.write("\nThis comes from Python")
file.close()

# better, most used way --> with-clause --> context manager
# automatically closes the file

with open("my_story.txt", 'a') as file:
    file.write("\nThis also comes from Python")

print("proceed with the code")

# read from a file
with open("my_story.txt", "r") as file:
    content = file.read()

with open("my_story.txt", "r") as file:
    content_list = file.readlines()

content_list_filtered = []

for line in content_list:
    line_filtered = line.replace("\n", "")
    content_list_filtered.append(line_filtered)

pass

# [line.replace("\n", "") for line in content_list]


