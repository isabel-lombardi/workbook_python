"""Shows if the month and day entered by the user
   are holidays with a fixed date or not"""

day = int(input("Enter the day: "))
month = input("Enter the month: ")

holiday = ""

if day == 1 and month == "January":
    holiday = "New Year's day"
elif day == 1 and month == "July":
    holiday = "Canada day"
elif day == 25 and month == "December":
    holiday = "Christmas day"
else:
    holiday = ""

if holiday == "":
    print("The month and day entered do not correspond to a fixed date holiday \n"
          "or the month entered is not correct")
else:
    print("The date correspond to {}".format(holiday))

