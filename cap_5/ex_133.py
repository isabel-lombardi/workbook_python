# Does a List Contain a Sublist?

def is_sublist(larger, smaller):
    a = [element for element in larger if element in smaller]
    b = [element for element in smaller if element in larger]
    return a == b


print(is_sublist([1, 2, 3, 4], [1]))
