# Approximate π
for i in range(1, 16):
    pi = 3
    if i >= 1:
        pi += 4 / (2 * 3 * 4)
    if i >= 2:
        pi -= 4 / (4 * 5 * 6)
    if i >= 3:
        pi += 4 / (6 * 7 * 8)
    if i >= 4:
        pi -= 4 / (8 * 9 * 10)
    if i >= 5:
        pi += 4 / (10 * 11 * 12)
    if i >= 6:
        pi -= 4 / (12 * 13 * 14)
    if i >= 7:
        pi += 4 / (14 * 15 * 16)
    if i >= 8:
        pi -= 4 / (16 * 17 * 18)
    if i >= 9:
        pi += 4 / (18 * 19 * 20)
    if i >= 10:
        pi -= 4 / (20 * 21 * 22)
    if i >= 11:
        pi -= 4 / (22 * 23 * 24)
    if i >= 12:
        pi += 4 / (24 * 25 * 26)
    if i >= 13:
        pi -= 4 / (26 * 27 * 28)
    if i >= 14:
        pi += 4 / (28 * 29 * 30)
    if i >= 15:
        pi -= 4 / (30 * 31 * 32)

    print("Approximation {} is  {}".format(i, pi))