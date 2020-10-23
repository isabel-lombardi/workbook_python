# Is a List already in Sorted Order?

def is_sorted(x):
    if x == sorted(x):
        return True
    else:
        return False


def main():
    us_list = []
    while True:
        us_value = input("Enter a number (black to quit) : ")
        if us_value == "":
            break
        us_value = float(us_value)
        us_list.append(us_value)

    print(is_sorted(us_list))


main()