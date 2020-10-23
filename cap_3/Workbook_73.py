# MultipleWord Palindromes

pal = ""
s = input("Enter the word: ")
s1 = s.replace(" ", "")

for l in s1:
    pal += l

if s1 == pal:
    print("True")
else:
    print("False")