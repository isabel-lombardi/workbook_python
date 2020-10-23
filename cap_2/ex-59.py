# Is a License Plate Valid?
import re

us_plate = input("Enter the plate: ")
number = us_plate
plate_style = ""

number = re.sub('[^0-9]', '', number)
letter = re.findall("[a-zA-Z]", us_plate)

if len(number) == 3 and len(letter) == 3:
    plate_style = "older style"
elif len(number) == 4 and len(letter) == 3:
    plate_style = "newer style"
else:
    plate_style = ""

if plate_style == "":
    print("Is not valid for either style of license plat")
else:
    print("The {} plate equals to {} ".format(us_plate.upper(), plate_style))
