# Convert an Integer to its Ordinal Number
choose = int(input("Enter the number: "))

d = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth",
     7: "Seventh", 8: "Eigth", 9: "Nineth", 10: "Tenth", 11: "Eleventh", 12: "Twelfth"}


def ordinal(n):
    if n > len(d):
        print("")
    else:
        print("The order of {} is: {}".format(n, d[n]))


ordinal(choose)
print("-" * 25)
for k, v in d.items():
    print("{} - {}".format(k, v))
