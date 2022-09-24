import argparse
from car_functions.import_functions import import_car_by_brand

# initiate the argument parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument("--brand", type=str, required=True)
parser.add_argument("--color", type=str, required=True)
parser.add_argument("--cilinders", type=int, required=False, default=0)

# parse the arguments
args = parser.parse_args()

# double underscores are called 'dunders'
if __name__ == '__main__':
   # get the brand from the parser
   selected_brand = args.brand
   selected_color = args.color
   selected_cilinders = args.cilinders
   
   # execute the function
   cars_list = import_car_by_brand(selected_brand, selected_color, selected_cilinders)
   
   print(cars_list[0]['merk'])
   print(cars_list[0]['handelsbenaming'])
   print(cars_list[0]['eerste_kleur'])
   print(cars_list[0]['aantal_cilinders'])


##
# 1. Build your code, or logic
# 2. Wrap your logic/code into functions
# 3. Organize your functions into folders (own libraries) e.g. custom_functions
# 4. In the folders, organize your functions into seperate scripts
# 5. Import and call the functions from your run/main scrips
# 6. Add a argument parser to your script


