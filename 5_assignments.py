# Create an if-statement which if your name contains an “A”
#. If it does, print a message that it does. Otherwise, print that is doesn’t.
my_name = input("What is your name?\n")

if 'a' in my_name.lower():
    print("Your name contains an 'A'")
else:
    print("Your name does not contain an 'A'")

print(f"Hello {my_name}")

# your name begins with a vowel, change it into a non-vowel and otherwise: Arie –> Brie or Rose –> Aose
vowels = "aeoui"

if my_name[0].lower() in vowels:
    print("Your name begins with a vowel")
    first_letter = my_name[0]
    new_name = my_name.replace(first_letter, 'B')
    print(f"Changed name {my_name} to {new_name} ")
else:
    print("Your name does not begin with a vowel")
    first_letter = my_name[0]
    new_name = my_name.replace(first_letter, 'A')
    print(f"Changed name {my_name} to {new_name} ")

print(f"Hello {new_name}")