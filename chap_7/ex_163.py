# Names that Reached Number One

def process_file(filename, names):
    with open(filename, "r") as file:
        line = file.readline()
    parts = line.split()
    name = parts[0]
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

    print("Girls’ names that reached #1:")
    for name in girls:
        print(" ", name)
    print()

    print("Boys’ names that reached #1: ")
    for name in boys:
        print(" ", name)


main()

