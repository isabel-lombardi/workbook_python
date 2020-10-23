# Compute interest

savings_account = float(input("Enter the amount of money for the savings account: "))
print("-" * 55)
interest = 0.04
print("With this saving account you can earn the 0.4% for year.")
print("-" * 55)


earn_y = savings_account * interest
total_SA_1 = (earn_y+savings_account)
total_SA_2 = (total_SA_1+earn_y)
total_SA_3 = (total_SA_2+earn_y)

print("In one year, your saving account amount will be: ${:.2f}".format(total_SA_1))
print("In two years, your saving account amount will be: ${:.2f}".format(total_SA_2))
print("In three years, your saving account amount will be: ${:.2f}".format(total_SA_3))