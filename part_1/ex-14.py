# Feet and inches in cm
feet = float(input("Enter the number of feet: "))
inches = float(input("Enter the number of inches: "))

OneFoot = 38.48
OneInch = 2.54

cm = (feet*OneFoot) + (inches*OneInch)

print("{} feet and {} inches correspond to {} cm".format(feet, inches, cm))

