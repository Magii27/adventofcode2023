def getDayData_int(day, splitter):
    with open("DayData\\Day" + str(day) + "Data.txt", 'r') as f:
        data = f.read().split(splitter)
        f.close()

    data = list(map(int, data))
    return data


def getDayData_str(day, splitter):
    with open("DayData\\Day" + str(day) + "Data.txt", 'r') as f:
        data = f.read().split(splitter)
        f.close()

    return data


def answer(ans, day, part):
    if int(part) == 1:
        print("┌" + "—" * 69 + "┐")
        print("│" + "<│ AdventOfCode 2022 │>".center(69) + "│")
        print("│" + ("<│ DAY " + str(day) + " │>").center(69) + "│")
        print("└ " + "˅" * 67 + " ┘")
    print(("< PART " + str(part) + " >").center(71, "—"), end="\n")
    print("┌" + "—" * 2 + " ANSWER " + "—" * 59 + "┐")
    print("│" + " " * 5 + str(ans) + " " * (64 - len(str(ans))) + "│")
    print("└" + "—" * 69 + "┘")

