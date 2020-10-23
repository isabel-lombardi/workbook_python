# Convert MPG in L/100Km

miles = float(input("Enter the number of miles traveled: "))
gallons = float(input("Enter the number of gallons used: "))
mpg = float(miles / gallons)
l100Km = float(235.214583 / mpg)

print("{} mpg, equivalent to {:.2f} L/100Km".format(mpg, l100Km))

