# center  string of characters within a certain width
width = 140


def center(s, w):
    if w < len(s):
        return s

    spaces = (w - len(s)) // 2
    result = " " * spaces + s
    return result


def main():
    print(center("If", width))
    print(center("you stayed", width))
    print(center("with", width))
    print(center("Harry Potter", width))
    print(center("to the", width))
    print(center("very", width))
    print(center("end", width))


main()

