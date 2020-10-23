# Grade Point to Letter grade
"""Convert the grade point entered by the user in equivalent letter grade"""

gp_u = float(input("Enter the Grade point: "))
gp = ""  # round(gp_u)

# try dictionary
lut = {4.0: "A+" and "A", 3.7: "A-", 3.3: "B+", 3.0: "B", 2.7: "B-",
       2.3: "C+", 2.0: "C", 1.7: "C-", 1.3: "D+", 1.0: "D", 0: "F"}

res = lut.get(gp_u) or lut[min(lut.keys(), key=lambda key: abs(key - gp_u))]

if gp not in lut:
    print("point grade not valid")
else:
    print(gp_u, "equals", str(res))
