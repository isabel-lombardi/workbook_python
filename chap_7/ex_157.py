# Both Letter Grades and Grade Points
grades = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
          "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0}

while True:
    user_input = input("➤ Enter a Letter Grades or Grade Points: ").upper()
    if user_input.strip() == "":
        break
    try:
        user_input = float(user_input)
        for key, value in grades.items():
            if value == user_input:
                if user_input == 4.0:
                    keys_list = list(grades)
                    print("˃  Your Grade Point correspond to {} or {} Letter Grade".format(key, keys_list[1]))
                    print("-" * 55)
                    break
                else:
                    print("˃  Your Grade Point correspond to {} Letter Grade".format(key))
                    print("-" * 55)
        if user_input not in grades.values():
            print(" - Enter a Grade Point between 4.0 and 0 -")
            print("-" * 55)

    except ValueError:
        user_input = str(user_input)
        for key, value in grades.items():
            if key == user_input:
                print("˃ Your Letter Grade correspond to {} Grade Point".format(value))
                print("-" * 55)
        if user_input not in grades.keys():
            print("    - This letter Grade do not exist - ")