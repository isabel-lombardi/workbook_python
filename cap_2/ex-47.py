# Birth Date to Astrological Sign
# Calculates the zodiac sign from the date of birth entered by the user

month = input("Enter your month of birth: ").lower()
day = int(input("Enter your day of birth: "))

z_sign = ""

if month == "december":
    z_sign = "Sagittarius" if (day < 22) else "Capricorn"
elif month == "january":
    z_sign = "Capricorn" if (day < 19) else "Aquarius"
elif month == "february":
    z_sign = "Aquarius" if (day < 18) else "Pisces"
elif month == "march":
    z_sign = "Pisces" if (day < 20) else "Aries"
elif month == "april":
    z_sign = "Aries" if (day < 19) else "Taurus"
elif month == "may":
    z_sign = "Taurus" if (day < 20) else "Gemini"
elif month == "june":
    z_sign = "Gemini" if (day < 20) else "Cancer"
elif month == "july":
    z_sign = "Cancer" if (day < 22) else "Leo"
elif month == "august":
    z_sign = "Leo" if (day < 22) else "Virgo"
elif month == "september":
    z_sign = "Virgo" if (day < 22) else "Libra"
elif month == "october":
    z_sign = "Libra" if (day < 22) else "Scorpio"
elif month == "november":
    z_sign = "Scorpio" if (day < 21) else "Sagittarius"

print("Your zodiac sign is {}".format(z_sign))