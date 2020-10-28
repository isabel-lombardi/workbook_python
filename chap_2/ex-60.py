# Display the bets that play out in a roulette simulation
from random import randrange

# simulate spinnig the weel, using 37 to represent 00
value = randrange(0, 38)
if value == 37:
    print("The spin resulted in 00...")
else:
    print("The spin resulted in %d..." % value)

# Display the payout for a single number
if value == 37:
    print("Pay 00")
else:
    print("Pay", value)

if value % 2 == 1 and 1 <= value <= 9 or \
        value % 2 == 0 and 12 <= value <= 18 or \
        value % 2 == 1 and 19 <= value <= 27 or \
        value % 2 == 0 and 30 <= value <= 36:
    print("Pay Red")
elif value == 0 or value == 37:
    pass
else:
    print("Pay Black")
# Display the odd vs even payout
if 1 <= value <= 36:
    if value % 2 == 1:
        print("Pay Odd")
else:
    print("Pay Even")

# Display the lower number vs the upper number
if 1 <= value <= 18:
    print("Pat 1 to 18")
elif 19 <= value <= 36:
    print("Pay 19 to 36")
