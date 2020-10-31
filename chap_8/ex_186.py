# Run-Length Encoding
def encode(text):
    if not text:
        return ""
    else:
        last_char = text[0]
        max_index = len(text)
        i = 1
        while i < max_index and last_char == text[i]:
            i += 1
        return last_char + str(i) + encode(text[i:])


def main():
    s = input("Enter some characters: ")
    print("When those characters are run-length encoded the result is:", encode(s))


main()
