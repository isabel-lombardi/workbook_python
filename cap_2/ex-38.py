# Program that read a name of month from the user and show number of days in that

month = input("Enter the name of month: ").lower()
days = 31

if month == "november" or month == "april" or month == "june" or month == "september":
    days = 30
elif month == "february":
    days = "28 or 29"

print("{} is composed by {} days".format(month, days))