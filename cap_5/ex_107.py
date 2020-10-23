# Avoiding Duplicates

user_w = []

while True:
    word = input("Enter the words (black to quit): ")
    if word == "":
        break
    if word not in user_w:
        user_w.append(word)

for w in user_w:
    print(w)

