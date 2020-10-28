# Only the Words
import re


def only_words(s):
    s = re.split('[:;!?., ]', s)
    return s


def main():
    us_str = input("Enter the text: ")
    print(only_words(us_str))


if __name__ == "__main__":
    main()
