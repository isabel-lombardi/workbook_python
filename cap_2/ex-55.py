# Frequency to name
freq = float(input("Enter a frequency: "))

name = ""

if freq < 3e9:
    name = "radio waves"
elif 3e9 <= freq < 3e12:
    name = "microwaves"
elif 3e12 <= freq < 4.3e14:
    name = "infrared light"
elif 4.3e14 <= freq < 7.5e14:
    name = "visible light"
elif 7.5e14 <= freq < 3e17:
    name = "ultraviolet light"
elif 3e17 <= freq < 3e19:
    name = "x-rays"
elif freq >= 3e19:
    name = "gamma rays"

if name != "":
    print("This frequency is in the '{}' category.".format(name))
else:
    print("Invalid frequency entered.")