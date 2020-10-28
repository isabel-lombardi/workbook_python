# Dog Years

user_n = float(input("Enter the age: "))

dog_age = 10.5
dog_age2 = 4

if user_n <= 2:
    result = int(user_n * dog_age)
    print("The age equal to {} dog years".format(result))
elif user_n >= 2:
    result2 = int(dog_age * 2) + (user_n * dog_age2) - (dog_age2 * 2)
    print("The age equal to {} dog years".format(result2))
elif user_n < 0:
    print("Invalid format. Enter an integer number")
