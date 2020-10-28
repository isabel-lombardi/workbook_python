# Multiplication Table

num = 10
l = list(list(range(1 * i, (num + 1) * i, i)) for i in range(1, num + 1))

width = len(str(l[-1][-1])) + 1
for n in l:
    n = [str(j).rjust(width) for j in n]
    print(''.join(n))
