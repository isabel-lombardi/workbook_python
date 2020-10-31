coins = [0.25, 0.10, 0.05, 0.01]


def combinations_with_replacement(iterable, num):
    comb = tuple(iterable)
    n = len(comb)
    if not n and num:
        return
    indices = [0] * num
    yield tuple(comb[i] for i in indices)
    while True:
        for i in reversed(range(num)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (num - i)
        yield tuple(comb[i] for i in indices)


def num_coins(amount, n, i=0):
    comb = list(combinations_with_replacement(coins, n))
    if amount != round(sum(comb[i]), 4):
        i += 1
        if i >= len(list(comb)):
            return False
        else:
            return num_coins(amount, n, i)
    else:
        print(comb[i])
        return True


us_amount = float(input("Enter the dollar amount: "))
us_num_coins = int(input("Enter the number of coins: "))
print()
print(num_coins(us_amount, us_num_coins))