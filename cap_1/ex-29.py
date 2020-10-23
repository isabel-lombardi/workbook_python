# Celsius to Kelvin and Fahrenheit

c_degrees = int(input("Enter the degrees in Celsius: "))

# Convert
k_degrees = c_degrees + 273.15
f_degrees = c_degrees * (9 / 5) + 32

print("The temperature equals", k_degrees, "°K and", f_degrees, "°F")
