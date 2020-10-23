# Determines the type of triangle from the entered data lengths

side1 = int(input("-Enter the length of the first side: "))
side2 = int(input("-Enter the length of the second side: "))
side3 = int(input("-Enter the length of the third side: "))

name = ""

if side1 == side2 and side2 == side3:
    name = "equilateral"
elif side1 == side2 or side2 == side3 or side3 == side1:
    name = "isosceles"
else:
    name = "scalene"

print("The triangle is: {}".format(name))


