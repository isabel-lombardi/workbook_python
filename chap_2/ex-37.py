# Program determines the name of a shape by its number of sides

sides_u = int(input("Enter the number of sides: "))

name = ""

if sides_u == 3:
    name = "triangle"
elif sides_u == 4:
    name = "square, rectangle, parallelogram, rhombus or trapezoid"
elif sides_u == 5:
    name = "pentagon"
elif sides_u == 6:
    name = "hexagon"
elif sides_u == 7:
    name = "heptagon"
elif sides_u == 8:
    name = "octagon"
elif sides_u == 9:
    name = "ennagon"
elif sides_u == 10:
    name = "decagon"


if name == "":
    print("Invalid Number. Enter a number of sides between 3 and 10")
else:
    print("The shape is: {}".format(name))