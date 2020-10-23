# Automatic checkout machine

cent_toonie = 200
cent_loonie = 100
cent_quarter = 25
cent_dime = 10
cent_nickle = 5
cent_penny = 1

cents = int(input("Enter the number of cents: "))

print("", cents // cent_toonie, "toonies")
cents = cents % cent_toonie

print("", cents // cent_loonie, "loonies")
cents = cents % cent_loonie

print("", cents // cent_quarter, "quarter")
cents = cents % cent_quarter

print("", cents // cent_dime, "dime")
cents = cents % cent_dime

print("", cents // cent_nickle, "nickle")
cents = cents % cent_nickle

print("", cents // cent_penny, "penny")
