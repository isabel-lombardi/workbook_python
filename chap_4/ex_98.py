# Hexadecimal and Decimal Digits

def hex2int(h):
    d = int(h, 16)
    print("Value in decimal: {}".format(d))


def int2hex(i):
    convert = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    result = ''
    while i != 0:
        r = i % 16
        r = str(r)
        if r in convert:
            r = str(convert.get(r))
        elif "0" <= r <= "9":
            r = r
        else:
            print("Error. Try Again")
            break
        result += r
        i = i // 16
    c = len(result)
    counter = -1
    res_new = ''
    for x in result:
        counter += 1
        d = c - counter
        e = c - counter - 1
        f = result[e:d]
        res_new = res_new + f
        print("Value in hex: {}".format(x))


hex2int("A")
int2hex(10)
