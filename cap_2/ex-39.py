# Sound Levels
decibel = int(input("Enter a number of decibel: "))

# Calculates the noise corresponding to the number of decibels
noise = ""

if decibel == 130:
    noise = "Jackhammer"
elif decibel == 106:
    noise = "Gas lawnower"
elif decibel == 70:
    noise = "Alarm clock"
elif decibel == 40:
    noise = "Quiet room"


if 130 > decibel > 106:
    noise = "Jackhammer and Gas Lawnower"
elif 106 > decibel > 70:
    noise = "Gas Lawnower and Alarm clock"
elif 70 > decibel > 40:
    noise = "Alarm clock and Quiet room"

if decibel > 130:
    noise = "more than a Jackhammer"
elif decibel < 40:
    noise = "less than a Quiet room"

print("{} decibel correspond to {}".format(decibel, noise))