# Run-Length Decoding

def decode(text):
    if not text:
        return ""
    else:
        char = text[0]
        quantity = text[1]
        return char * int(quantity) + decode(text[2:])


def main():
    code = ['A', 12, 'B', 4, 'A', 6, 'B', 3]
    print("The compressed list is: {}".format(code))
    print()
    deco = []
    for e in decode(code):
        deco.append(e)
    print("The decompressed list is: \n"
          "{}".format(deco))


if __name__ == "__main__":
    main()
