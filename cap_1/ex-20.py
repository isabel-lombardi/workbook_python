# Ideal Gas Law

pascal_p = float(input("Please enter a pressure in Pascals: "))
volume_l = float(input("Please enter a volume in liters: "))
temperature_c = float(input("Please enter a temperature in Kelvin: "))

r = 8.314

n = (pascal_p * volume_l) / (r * temperature_c)

print("The amount of gas in moles for these conditions is {:.3f}.".format(n))
