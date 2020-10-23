# Random Good Password

from cap_4.ex_94 import r_pass
from cap_4.ex_96 import check_pas


def main():
    n = 0
    new_pass = ""
    while not check_pas(new_pass):
        new_pass = r_pass()
        n += 1
    print("Attempts: {}".format(n))
    print("Password: {}".format(new_pass))


main()



