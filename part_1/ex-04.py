# Area of a field
areas_acres_feet = 43560

length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

acres = length * width / areas_acres_feet
print("The area of the field in acres is: {:.3f}".format(acres))
