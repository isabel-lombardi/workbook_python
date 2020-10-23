# Generate All Sublists of a List

def sublist(s):
    def is_sublist(x):
        sub_list = [[]]
        for e in range(1, len(x) + 1):
            for i in range(0, len(x) - e + 1):
                sub_list.append(x[i: i + e])
        return sub_list

    def main():
        print("The sublist of [] is: ")
        print(is_sublist([]))

        print("The sublists of [1] are: ")
        print(is_sublist([1]))

        print("The sublists of [1, 2] are: ")
        print(is_sublist([1, 2]))

        print("The sublists of [1, 2, 3] are: ")
        print(is_sublist([1, 2, 3]))

        print("The sublists of [1, 2, 3, 4] are: ")
        print(is_sublist([1, 2, 3, 4]))

    main()
