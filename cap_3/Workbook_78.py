# Decimal to Binary
base = 2
us_num = int(input("Enter the decimal number to convert to binary number: "))
result = ""
q = us_num

remainder = q % base
result = str(remainder) + result
q = q // base

while q > 0:
    remainder = q % base
    result = str(remainder) + result
    q = q // base

print("The decimal number {} corresponds to the binary number: {}".format(us_num, result))
