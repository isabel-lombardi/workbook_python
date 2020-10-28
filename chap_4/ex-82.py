# Taxi Fare
b_rate = 4.00
plus = 0.25

t_distance = int(input("Enter the total distance travelled in kilometers: "))


def t_rate(n):
    t_in_m = t_distance * 1000
    total = (t_in_m / 140) * plus + b_rate
    print("${}".format(total))


print("The total rate of the route will be:")
t_rate(t_distance)
