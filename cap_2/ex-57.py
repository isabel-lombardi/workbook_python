# Year is leap?

us_year = int(input("Enter the year: \n"))
year = ""
if us_year % 400 == 0:
    year = "leap year"
if us_year % 100 == 0:
    year = "not a leap year"
if us_year % 4 == 0:
    year = "leap year"
else:
    year = "not a leap year"

print()
print("{} is {}".format(us_year, year))
