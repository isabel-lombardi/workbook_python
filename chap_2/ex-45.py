# What Color is that Square?
# It reads the user's location and writes whether it is white or black
gridP_p = input("PEnter a chess board position: ")

color = gridP_p[0].lower()
row = int(gridP_p[1])

if color in "aceg":
    start_black = True
else:
    start_black = False

if start_black:
    if row % 2 == 0:
        white = True
    else:
        white = False
else:
    if row % 2 == 0:
        white = False
    else:
        white = True

if white:
    print("The position is  white.")
else:
    print("The position is black.")
