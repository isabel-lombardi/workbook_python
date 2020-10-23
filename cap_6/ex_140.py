# Postal Codes

pos = {"Newfoundland": "A", "Nova Scotia": "B", "Prince Edward Island": "C", "New Brunswick": "E",
             "Quebec": ["G", "H", "I"], "Ontario": ["K", "L", "M", "N", "P"], "Manitoba": "R", "Saskatchewan": "S",
             "Alberta": "T", "British Columbia": "V", "Nunavut": "X", "or Northwest Territories": "X", "Yukon": "Y"}

postal_code = input("Enter the postal code: ").upper()
result = ""
if postal_code[1] == 0:
    result += "a rural "
else:
    result += "an urban "
for k, v in pos.items():
    if postal_code[0] in v:
        result += "address " + k


print("The postal code {} is for {} ".format(postal_code, result))
