name = input("Insert the name:\n")

selected_letter = input("Insert the letter:\n")
indices_letter = []

for idx, letter in enumerate(name):
    if letter.lower() == selected_letter:
        indices_letter.append(idx + 1)

if len(indices_letter) == 0:
    print(f"No letter {selected_letter} in {name}")
else:
    print(f"The letter {selected_letter} is in positions {indices_letter}")