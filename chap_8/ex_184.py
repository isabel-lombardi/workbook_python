# Flatten a List


def flatten(data):
    if not data:
        return []

    if type(data[0]) == list:
        return flatten(data[0]) + flatten(data[1:])
    else:
        return [data[0]] + flatten(data[1:])


def main():
    print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))

    print(flatten([1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]))
    print(flatten([[[[[[[[[[1], 2], 3], 4], 5], 6], 7], 8], 9], 10]))
    print(flatten([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(flatten([]))


main()
