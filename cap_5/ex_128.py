# Count the Elements

def countRange(x, mn, mx):
    count = 0
    for n in x:
        if mn <= n < mx:
            count += 1
    return count


def main():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Counting the elements in [1, 10] between 5 and 7.")
    print("Result: {} Expected: 2".format(countRange(x, 5, 7)))

    print("Counting the elements in [1, 10] between -5 and 77.")
    print("Result: {} Expected: 10".format(countRange(x, -5, 77)))

    print("Counting the elements in [1, 10] between 12 and 17.")
    print("Result: {} Expected: 0".format(countRange(x, 12, 17)))

    print("Counting the elements in [] between 0 and 100.")
    print("Result: {} Expected: 0".format(countRange([], 0, 100)))

    x = [1, 2, 3, 4, 1, 2, 3, 4]
    print("Counting the elements in {} between 2 and 4.")
    print("Result: {} Expected: 4".format(countRange(x, 2, 4)))


main()
