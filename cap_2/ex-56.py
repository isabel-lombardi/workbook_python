# Cell Phone Bill

minutes = int(input("Enter the number of minutes used in a month: "))
text_mess = int(input("Enter the number of messages used in a month: "))

base_charge = 15.00
every_extra_mess = (text_mess - 50) * 0.15
every_extra_min = (minutes - 50) * 0.25
call_center_charge = 0.44

subtotal = base_charge + every_extra_mess + every_extra_min + call_center_charge

tax = subtotal / 100 * 5
total = subtotal + tax

print()
print("Base charge = ${}".format(round(base_charge, 2)))

if every_extra_min > 0:
    print("Additional minutes charge = ${}".format(round(every_extra_min, 2)))
if every_extra_mess > 0:
    print("Additional messages charge = ${}".format(round(every_extra_mess, 2)))

print("Call center charge = ${}". format(round(call_center_charge, 2)))
print("Tax = ${}". format(round(tax, 2)))
print()
print("Grand Total = ${}". format(round(total, 2)))

