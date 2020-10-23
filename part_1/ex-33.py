# Day old Bread

b = 3.49
old_b = 60  # 60% discount

num_old_b = int(input("Enter the number of old bread: "))

pr_old_b = (b * old_b) / 100
tot_old_b = num_old_b * pr_old_b

print("Price Bread    ${:.2f}".format(b))
print("Discount       {:.2%}".format(old_b / 100))
print("Total Price    ${:.2f}".format(tot_old_b))


