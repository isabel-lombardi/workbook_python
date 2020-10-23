# Season from Month and Day
# Read day and month from the user and print the associated season

day = int(input("Enter the day: "))
month = input("Enter the month: ")

season = ""

if month == "January" or month == "February":
    season = "Winter"
elif month == "March":
    if day < 20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "April" or month == "May":
    season = "Spring"
elif month == "August" or month == "July":
    season = "Summer"
elif month == "June":
    if day < 21:
        season = "Spring"
    else:
        season = "Summer"
elif month == "October" or month == "November":
    season = "Fall"
elif month == "September":
    if day < 22:
        season = "Summer"
    else:
        season = "Fall"
elif month == "December":
    if day < 21:
        season = "Fall"
    else:
        season = "Winter"


print("The entered date correspond to {}".format(season))


