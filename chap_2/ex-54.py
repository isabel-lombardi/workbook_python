# Wavelengths of Visible Light

user_wl = int(input("Enter the Wavelength: "))
color = ""

if user_wl == 380 or user_wl < 450:
    color = "Violet"
elif user_wl == 450 or user_wl < 495:
    color = "Blue"
elif user_wl == 495 or user_wl < 570:
    color = "Green"
elif user_wl == 570 or user_wl < 590:
    color = "Yellow"
elif user_wl == 590 or user_wl < 620:
    color = "Orange"
elif user_wl == 620 or user_wl < 750:
    color = "Red"
elif user_wl > 750:
    color = ""

if color == "":
    print("The wavelength entered is outside the visible spectrum.")
else:
    print("The wavelength {}, correspond to: {}".format(user_wl, color))

