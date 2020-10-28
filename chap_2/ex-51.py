# Read a letter grade from the user and write the relative grade points

letter = input("Enter the Letter Grade: ")
letter = letter.upper()
gp = 0

# Convert Letter Grade to Grade Points
if letter == "A+" or letter == "A":
    gp = 4.0
elif letter == "A-":
    gp = 3.7
elif letter == "B+":
    gp = 3.3
elif letter == "B":
    gp = 3.0
elif letter == "B-":
    gp = 2.7
elif letter == "C+":
    gp = 2.3
elif letter == "C":
    gp = 2.0
elif letter == "C-":
    gp = 1.7
elif letter == "D+":
    gp = 1.3
elif letter == "D":
    gp = 1.0
elif letter == "F":
    gp = 0
else:
    gp = "difference"

if gp == "difference":
    print("The grade of letter is not valid")
else:
    print("{} correspond to {}".format(letter, gp))




