from our_functions.import_functions import import_cars, export_cars_to_file

selected_brand = input("Select a brand:\n")
selected_color = input("Select a color:\n")

# use the functions
cars_list = import_cars(selected_brand, selected_color)
export_cars_to_file(cars_list, f"export_{selected_brand}.csv", selected_brand)

