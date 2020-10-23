# Reverse Lookup

def reverseLookup(dic, v):
    keys = []
    for key in dic:
        if dic[key] == v:
            keys.append(key)
    return keys


def main():
    vg_companies = {"Activision": "COD", "Tencent": "COD", "Ubisoft": "Assasin's Creed", "Epic Games": "Fortnite"}
    print("The developers of 'COD' are: {}".format(reverseLookup(vg_companies, "COD")))

    print("The developer of 'Assasin's Creed' is: {}".format(reverseLookup(vg_companies, "Assasin's Creed")))

    print("The developer of 'The Last of Us II' is: {}".format(reverseLookup(vg_companies, "The Last of Us II")))

main()


