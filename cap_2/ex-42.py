# Convert the frequency to note name
freq = float(input("Please enter a frequency in Hertz: "))
note = ""

if 261.63 - 1 < freq < 261.63 + 1:
    note = "C"
elif 293.66 - 1 < freq < 293.66 + 1:
    note = "D"
elif 329.63 - 1 < freq < 329.63 + 1:
    note = "E"
elif 349.23 - 1 < freq < 349.23 + 1:
    note = "F"
elif 392.00 - 1 < freq < 392.00 + 1:
    note = "G"
elif 440.00 - 1 < freq < 440.00 + 1:
    note = "A"
elif 493.88 - 1 < freq < 493.88 + 1:
    note = "B"

if note == "":
    print("There is no note that corresponds to that frequency")
else:
    print("That frequency is {}".format(note))
