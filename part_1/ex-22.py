# Area of a triangle with 3 side
import math

side1 = int(input("Enter the first side of a triangle: "))
side2 = int(input("Enter the second side of a triangle: "))
side3 = int(input("Enter the third side of a triangle: "))

s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print("The area of the triangle is: {:.4f}".format(area))
