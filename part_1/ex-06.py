"""Cost of a meal at the restaurant ordered by the user.
   Show tax, tip and total"""
price_meal = float(input("Enter the price of the meal:"))
tax_percent = 24
tip_percent = 18

tax = (price_meal * tax_percent) / 100
tip = (price_meal * tip_percent) / 100

total = price_meal + tip + tax

print("Tax: ${}".format(tax))
print("Tip: ${}".format(tip))
print("-------------")
print("Total ${:.2f}".format(total))
