# Ideal Gas Law

# Calculates the amount of moles

# Read input from the user
p_p = float(input("Enter the pressure in Pascal: "))
v = int(input("Enter the volume in litres: "))
t_c = int(input("Enter the temperature in Celsius: "))

r = 0.0821   # Ideal gas constant (8.314 J / mol K)

t_k = t_c + 273
p = 0.00000986923 * p_p

n1 = (p * v) / (r * t_k)


print("pressione", p)
print("volume", v)
print("temperatura", t_k)

print(float(n1))


