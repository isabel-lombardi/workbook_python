name = input("Enter the two character note name, such as C4: ")

note = name[0].upper()
octave = int(name[1])

frequency = -1

if note == "C":
    frequency = 261.63
elif note == "D":
    frequency = 293.66
elif note == "E":
    frequency = 329.63
elif note == "F":
    frequency = 349.23
elif note == "G":
    frequency = 392.00
elif note == "A":
    frequency = 440.00
elif note == "B":
    frequency = 493.88

frequency /= 2 ** (4 - octave)  # Adjust the frequency to bring it into the correct octave

print("The note's frequency is {}Hz".format(frequency))