import math

diameters_list = [20, 40, 60, -10 ,300, 6000]

circle_size_list = []

for diameter in diameters_list:
    print(diameter)
    if diameter < 0:
        print("This is a negative value")
        continue


    radius = diameter / 2
    size = math.pow(radius, 2) * math.pi
    print(size)
    circle_size_list.append(size)

print("This is the rest of the code")


# keywords that can be used in loops
# - continue - Stop the current iteration of the loop, proceed ('continue') to the next
# - break
# - pass

for idx, value in enumerate(diameters_list):
    print(f"index is: {idx}")
    print(f"value is: {value}")
    print("="*10)

diameters_list = [20, 40, 60, -10 ,300, 6000]

for i in diameters_list:
    print(i)

print("hello")