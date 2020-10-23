"""It reads the measurement in feet by the user 
   and shows the equivalent in inches, yards and miles."""""

foot = int(input("Enter the distance in feet: "))

# Convert units of measure
inc_in_ft = 12
yar_in_ft = 0.333333
mls_in_ft = 0.000189394

print("The distance in inches is: {}".format(inc_in_ft*foot))
print("The distance in yards is: {}".format(yar_in_ft*foot))
print("The distance in miles is:{}".format(mls_in_ft*foot))
