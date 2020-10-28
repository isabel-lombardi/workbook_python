# Recursive Palindrome

def is_palidrome(txt):
    if len(txt) < 1:
        return True
    return txt[0] == txt[len(txt) - 1] and is_palidrome(txt[1: len(txt) - 1])


def main():
    user_txt = input("Enter a string: ")
    if is_palidrome(user_txt):
        print("The entered string is palindrome")
    else:
        print("The entered string is not a palindrome")


main()
