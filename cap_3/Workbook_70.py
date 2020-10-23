# Caesar Cipher

w = input("Enter the phrase or word: ")
p = int(input("Enter the number of position: "))


def rotate_word(s, n):
    s_c = ""
    i = 0
    for c in s:
        if ord('A') <= ord(c) <= ord('Z'):
            i = (ord(c) - ord('A') + n) % 26 + ord('A')
        elif ord('a') <= ord(c) <= ord('z'):
            i = (ord(c) - ord('a') + n) % 26 + ord('a')
        else:
            i = ord(c)
        s_c += chr(i)
    return s_c


print(rotate_word(w, p))
