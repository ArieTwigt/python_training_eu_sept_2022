# Calculate the surface of a circle with a diameter of 10 (radius^2 * pi)
import math

diameter = float(input("Provide the diameter of the circle:\n"))
rouding = int(input("How do you want to round the result?\n"))

radius = diameter / 2

size = math.pow(radius, 2) * math.pi
size_rounded = round(size, rouding)

print(size_rounded)