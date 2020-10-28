# The program asks the user to enter a letter and prints if it is a vowel or a consonant

letter = input("Enter the letter: ").lower()

if letter in "aeiou":
    print("The letter is a vowel")
elif letter == "y":
    print("The letter can be a vowel or a consonant")
else:
    print("The letter is a consonant")



