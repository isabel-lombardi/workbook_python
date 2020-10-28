# Unique Characters
user_str = input("Enter a string: ")

characters = {}

for ch in user_str:
    characters[ch] = 0
print("That string contained", len(characters), "unique characters")