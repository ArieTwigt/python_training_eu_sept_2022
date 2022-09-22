
age = int(input("What is you age?\n"))

if age < 18:
    print("Hi there")
    print("You cannot have alcohol")
    print("Goodbye!")
else:
    print("🍻 Cheers!")

print("Proceed with the code")

#
brands_list = ['BMW', 'TOYOTA', 'OPEL', 'TESLA']

selected_brand = 'VOLKSWAGEN'

if selected_brand in brands_list and selected_brand != 'AUDI':
    print(f"{selected_brand} is already in the list")
elif selected_brand == 'AUDI':
    print("No AUDI's here")
else:
    print(f"{selected_brand} is not in the list")
    print(f"Adding {selected_brand} to the list")
    brands_list.append(selected_brand)
    print(f"{selected_brand} added to the list.")


print(brands_list)
# indentation
# - officially, 4 spaces