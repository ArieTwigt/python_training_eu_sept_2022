import math

diameter = float(input("Insert the diameter:\n\n"))
print(f"Inserted diameter:{diameter}")

radius = diameter / 2
size = math.pow(radius, 2) * math.pi
size_rounded = round(size, 2)
print(f"The size is {size_rounded}")
