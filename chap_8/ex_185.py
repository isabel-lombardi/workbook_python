# Run-Length decoding
from chap_8.ex_184 import flatten


def decode(text):
    if not text:
        return []
    else:
        char = text[0]
        quantity = text[1]
        return [char] * quantity + flatten(decode(text[2:]))


def main():
    code = ['A', 12, 'B', 4, 'A', 6, 'B', 3]
    print("The compressed list is: {}".format(code))
    print("The decompressed list is: \n"
          "{}".format(decode(code)))


if __name__ == "__main__":
    main()
