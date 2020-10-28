# Line of Best Fit

def line_best_fit(x, y):
    avg_x = sum(x) / len(x)
    avg_y = sum(y) / len(y)

    x_avg_x = [n - avg_x for n in x]  # xi - X(avg)
    y_avg_y = [n - avg_y for n in y]  # yi - Y(avg)

    x_y = [x_avg_x[i] * y_avg_y[i] for i in range(len(x_avg_x))]  # (xi - X(avg)) * (yi - Y(avg))
    x_y_sum = [sum(x_y)]

    x2 = [n ** 2 for n in x_avg_x]  # (xi - X(avg)) ** 2
    x2_sum = [sum(x2)]

    x_y_sum = float(x_y_sum[0])
    x2_sum = float(x2_sum[0])

    m = x_y_sum / x2_sum
    b = avg_y - (m * avg_x)

    print("The formula for the line of best fit is: ")
    print("y = {}x + {:.1f}".format(m, b))


def main():
    x = []  # coordinate
    y = []  # coordinate
    while True:
        us_x = input("Enter the coordinate for x: ")
        us_y = input("Enter the coordinate for y: ")
        if us_x == "":
            break
        us_x = float(us_x)
        us_y = float(us_y)
        x.append(us_x)
        y.append(us_y)
    line_best_fit(x, y)


main()

