# Assessing Employees
us_rating = float(input("Enter the rating: "))

increase = 2400

rating = {0.0: "Unacceptable performance",
          0.4: "Acceptable performance, " + "an increase of:" "$%.f"% (us_rating * increase),
          0.6: "Meritorious performance, " + "an increase of " "$%.f" % (us_rating * increase)}

if us_rating >= 0.6:
    print(rating[0.6])
elif us_rating not in rating:
    print("Invalid evaluation, try again.")
else:
    print(rating[us_rating])
