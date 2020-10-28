# Scrabble™ Score

table_points = {1: ["A", "E", "I", "L", "N", "O", "R", "S", "T", "V"],
                2: ["D", "G"],
                3: ["B", "C", "M", "P"],
                4: ["F", "H", "V", "W", "Y"],
                5: ["K"],
                8: ["J", "X"],
                10: ["Q", "Z"]}
points = 0
word = input("Enter a word for calculated point: ").upper()
for ch in word:
    for k, v in table_points.items():
        if ch in v:
            points += k
print(points)