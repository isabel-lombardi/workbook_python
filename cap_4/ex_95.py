import string
import random


# old: AAANNN
# new: 0000AAA


def generate_old_plate():
    chars = "".join(random.choices(string.ascii_uppercase, k=3))
    numbers = "".join(random.choices(string.digits, k=3))

    return "{}{}".format(chars, numbers)


def generate_new_plate():
    numbers = "".join(random.choices(string.digits, k=4))
    chars = "".join(random.choices(string.ascii_uppercase, k=3))

    return "{}{}".format(numbers, chars)


def generate_random_plate():
    if random.random() > 0.5:
        return generate_new_plate(), "new format"
    else:
        return generate_old_plate(), "old format"


if __name__ == "__main__":
    plate, plate_format = generate_random_plate()
    print("Generated plate ({}): {}".format(plate_format, plate))
