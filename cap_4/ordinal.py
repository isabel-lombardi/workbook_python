
d = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth",
     7: "Seventh", 8: "Eigth", 9: "Nineth", 10: "Tenth", 11: "Eleventh", 12: "Twelfth"}


def ordinal(n):
    if n > len(d):
        print("")
    else:
        return d[n]
