from string import digits


def process_file(filename, names):
    with open(filename, "r") as file:
        for line in file:
            line = line.translate(str.maketrans('', '', digits))
            for name in line.split():
                if name not in names:
                    names.append(name)


def main():
    user_year = input("Enter the year to find out if there were neutral names: ")
    try:
        print("═" * 60)
        girls = []
        boys = []

        girl_fname = "BabyNames/" + user_year + "_GirlsNames.txt"
        boy_fname = "BabyNames/" + user_year + "_BoysNames.txt"

        process_file(girl_fname, girls)
        process_file(boy_fname, boys)
        neutral = [x for x in girls if x in boys]
        if not neutral:
            print("In {} there were no neutral names".format(user_year))
        elif len(neutral) == 1:
            print("The neutral name of {} is:".format(user_year), str(neutral)[1:-1])
        elif len(neutral) > 1:
            sep_neutral = " - ".join(neutral)
            print("The neutral names in {} are: {}".format(user_year, sep_neutral))

    except FileNotFoundError:
        print("The program does not have the data of {}".format(user_year))


main()