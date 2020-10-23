# Word by Word Palindromes
from cap_5.ex_117 import only_words


def word_palindromes(s):
    first_list = only_words(s)
    second_list = [x.lower() for x in first_list]
    if first_list == second_list:
        return True
    return False


def main():
    us_text = input("Enter the text: ").lower()
    print(word_palindromes(us_text))


main()
