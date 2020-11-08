def process_file(filename, names):
    with open(filename, "r") as file:
        line = file.readline()
        parts = line.split()
        name = parts[0]
        if name not in names:
            names.append(name)


def main():
    first_year = int(input("Enter the year from which to start analyzing: "))
    second_year = int(input("Enter the year to end:"))
    try:
        print("═" * 60)
        girls = []
        boys = []
        for year in range(first_year, second_year + 1):
            girl_fname = "BabyNames/" + str(year) + "_GirlsNames.txt"
            boy_fname = "BabyNames/" + str(year) + "_BoysNames.txt"

            process_file(girl_fname, girls)
            process_file(boy_fname, boys)
        print("The most used names are")
        print("► Girls")
        for name in girls:
            print(" ▹", name)
        print()
        print("► Boy")
        for name in boys:
            print(" ▹", name)

    except FileNotFoundError:
        print("Enter two years between 1800 and 2012")


main()
