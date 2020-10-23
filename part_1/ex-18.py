# Volume of a Cylinder
import math

radius = float(input("Enter the number of the radius: "))
height = float(input("Enter the number of the height: "))

# Formulas
area_base = (math.pi * radius ** 2)
volume = (area_base * height)

print("The volume of the cylinder is:",  "%.1f" % volume)
