# Is a String a Palindrome?

pal = ""
s = input("Enter the word: ")

for i in s:
    pal = i + pal

if s == pal:
    print("True")
else:
    print("False")