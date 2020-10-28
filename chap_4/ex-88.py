# Is it a Valid Triangle?

l1 = int(input("Enter the first length: "))
l2 = int(input("Enter the second length: "))
l3 = int(input("Enter the third length: "))


def is_triangle(a, b, c):
    lenghts = [a, b, c]
    lenghts.sort()
    if lenghts[2] < (lenghts[1] + lenghts[0]):
        return True
    else:
        return False


print(is_triangle(l1, l2, l3))



""" se una qualsiasi lunghezza è maggiore o uguale alla somma degli altri due, 
    le lunghezze non possono essere utilizzate per formare un triangolo"""