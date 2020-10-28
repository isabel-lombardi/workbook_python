# Compute the area of a regular polygon
import math

s = float(input("Enter the size of a side of a regular polygon: "))
n = float(input("Enter the number of these sides in the regular polygon: "))

area = (n * (s*s)) / (4 * math.tan(math.pi/n))

print("The area of this polygon is {} units squared.".format(area))