# Check a Password
import re


def check_pas(p):
    if len(p) < 8:
        if bool(re.findall('([A-Z][a-z][1-9])', p)) is False:
            return False
    else:
        return True


def main():
    us_pass = input("Enter your password: ")
    result = check_pas(us_pass)
    if result:
        print(result)
    else:
        print(result)


if __name__ == "__main__":
    main()
