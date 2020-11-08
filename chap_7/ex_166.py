# Distinct Names
from string import digits


def process_file(filename, names):
    with open(filename, "r") as file:
        for line in file:
            line = line.translate(str.maketrans('', '', digits))
            for name in line.split():
                if name not in names:
                    names.append(name)


def main():
    girls = []
    boys = []
    for year in range(1900, 2012 + 1):
        girl_fname = "BabyNames/" + str(year) + "_GirlsNames.txt"
        boy_fname = "BabyNames/" + str(year) + "_BoysNames.txt"

        process_file(girl_fname, girls)
        process_file(boy_fname, boys)

    sep_girls = " ◦ ".join(girls)
    print("► The girls' names are: ")
    print(sep_girls)
    print()
    sep_boys = " ◦ ".join(boys)
    print("► The boys' names are: ")
    print(sep_boys)


main()
