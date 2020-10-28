# Below and Above Average

num = []
while True:
    us_num = input("Enter a number (blank to quit): ")
    if us_num == "":
        break
    us_num = int(us_num)
    num.append(us_num)

avg = sum(num) / len(num)
num.sort()

below = [n for n in num if n < avg]
above = [n for n in num if n > avg]

print("The lower than average values are: {}".format(below))
print("The mean value of the inserted values is: {}".format(avg))
print("Values above average are: {}".format(above))