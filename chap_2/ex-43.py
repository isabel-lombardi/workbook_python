"""The program reads the denomination of a banknote by the user
   and displays the name of the person who appears on it"""

banknote = int(input("Enter the banknote denomination: "))

# Determine the face on the banknote by the denomination
person = ""

if banknote == 1:
    person = "George Washington"
elif banknote == 2:
    person = "Thomas Jefferson"
elif banknote == 5:
    person = "Abraham Lincoln"
elif banknote == 10:
    person = "Alexander Hamilton"
elif banknote == 20:
    person = "Andrew Jackson"
elif banknote == 50:
    person = "Ulysses S. Grant"
elif banknote == 100:
    person = "Benjamin Franklin"
else:
    person = ""

if person == "":
    print("This banknote does not exist or is not calculated in the program")
else:
    print("On the ${} banknote, appears the face of {}".format(banknote, person))


