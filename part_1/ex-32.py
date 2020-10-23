# Sort 3 Integers

first_int = int(input("Enter the first integer number: "))
second_int = int(input("Enter the second integer number: "))
third_int = int(input("Enter the third integer number: "))

int_min = min(first_int, second_int, third_int)
int_max = max(first_int, second_int, third_int)
middle = (first_int + second_int + third_int) - int_min - int_max

print("The number in sorted order are:{}, {}, {}.".format(int_min, middle, int_max))
