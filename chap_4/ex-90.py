# Does a String Represent an Integer?
def is_integer(s):
    s = s.strip()
    s = s.replace(' ', '')
    if (s[0] == '+' or s[0] == '-') and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    """if s.isdigit():
        return True"""
    return False


def main():
    s = input('Enter the string: ')
    if is_integer(s):
        print('The string is an integer')
    else:
        print('The string is not an integer')


if __name__ == '__main__':
    main()
