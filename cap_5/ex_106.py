# Remove Outliers

def remove_outliers(l, n):
    new_list = sorted(l)
    for num in range(n):
        new_list.pop()  # remove the largest
        new_list.pop(0)  # remove the smallest
    return new_list


def main():
    values = []
    while True:
        num = int(input("Enter a number (0 to quit): "))
        if num == 0:
            break
        values.append(num)

    if len(values) < 4:
        print("Error. Enter at least 4 values")
    else:
        print("With the outliers removed: {}".format(remove_outliers(values, 2)))
        print("The original list: {}".format(values))


main()
