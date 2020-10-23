# Coin Flip Simulation
import random


def coin_flipper():
    options = ['H', 'T']
    launch = ''

    while True:
        flip = random.choice(options)
        launch += flip

        if len(launch) >= 3:
            if launch[-3] == launch[-2] == launch[-1]:
                break
            else:
                continue
    return launch


results = []
sm = 0

for i in range(10):
    results.append(coin_flipper())
    sm += len(results[i])
    print(results[i], "(%d)" % len(results[i]))
avg = sm / 10

print("On average %d flips" % avg)