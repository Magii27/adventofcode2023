import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(3, splitter)
tmp_data = aof.getDayData_str(3, splitter)

data = []
for line in tmp_data:
    data.append(" ".join(line).split(" "))

print("Data:", data)


def checkVal(field):
    if not field.isnumeric() and field != ".":
        print(field)
        return True

    return False


def haveNeighbor(coordinates, data):
    y = coordinates[1]
    for x in range(coordinates[0][0], coordinates[0][1] + 1):
        if y == 0:
            if x == 0:
                if checkVal(data[y][x + 1]):
                    return True

                if checkVal(data[y + 1][x]):
                    return True

                if checkVal(data[y + 1][x + 1]):
                    return True

            elif x == len(data[y]) - 1:
                if checkVal(data[y][x - 1]):
                    return True

                if checkVal(data[y + 1][x]):
                    return True

                if checkVal(data[y + 1][x - 1]):
                    return True

            else:
                if checkVal(data[y][x + 1]):
                    return True

                if checkVal(data[y][x - 1]):
                    return True

                if checkVal(data[y + 1][x]):
                    return True

                if checkVal(data[y + 1][x + 1]):
                    return True

                if checkVal(data[y + 1][x - 1]):
                    return True

        elif y == len(data) - 1:
            if x == 0:
                if checkVal(data[y][x + 1]):
                    return True

                if checkVal(data[y - 1][x]):
                    return True

                if checkVal(data[y - 1][x + 1]):
                    return True

            elif x == len(data[y]) - 1:
                if checkVal(data[y][x - 1]):
                    return True

                if checkVal(data[y - 1][x]):
                    return True

                if checkVal(data[y - 1][x - 1]):
                    return True

            else:
                if checkVal(data[y][x + 1]):
                    return True

                if checkVal(data[y][x - 1]):
                    return True

                if checkVal(data[y - 1][x]):
                    return True

                if checkVal(data[y - 1][x + 1]):
                    return True

                if checkVal(data[y - 1][x - 1]):
                    return True

        else:
            if x == 0:
                if checkVal(data[y][x + 1]):
                    return True

                if checkVal(data[y + 1][x]):
                    return True

                if checkVal(data[y + 1][x + 1]):
                    return True

                if checkVal(data[y - 1][x]):
                    return True

                if checkVal(data[y - 1][x + 1]):
                    return True

            elif x == len(data[y]) - 1:
                if checkVal(data[y][x - 1]):
                    return True

                if checkVal(data[y + 1][x]):
                    return True

                if checkVal(data[y + 1][x - 1]):
                    return True

                if checkVal(data[y - 1][x]):
                    return True

                if checkVal(data[y - 1][x - 1]):
                    return True

            else:
                if checkVal(data[y][x + 1]):
                    return True

                if checkVal(data[y][x - 1]):
                    return True

                if checkVal(data[y + 1][x]):
                    return True

                if checkVal(data[y + 1][x + 1]):
                    return True

                if checkVal(data[y + 1][x - 1]):
                    return True

                if checkVal(data[y - 1][x - 1]):
                    return True

                if checkVal(data[y - 1][x]):
                    return True

                if checkVal(data[y - 1][x + 1]):
                    return True

    return False


def getLenOfLine(line):
    length = 0
    for item in line:
        length += len(item) if not item else 1

    return length


# PART ONE
ans = 0
liste = []
for y_line, line in enumerate(data):
    number = ""
    numberfound = False

    for x_line, item in enumerate(line):
        if item.isnumeric() and numberfound:
            number += item

        elif item.isnumeric():
            number = item
            numberfound = True

        elif not item.isnumeric() and numberfound:
            coordinates = ((x_line - len(number), x_line - 1), y_line)
            number = ""
            numberfound = False

            if haveNeighbor(coordinates, data):
                print("number:", int("".join([line[cor] for cor in range(coordinates[0][0], coordinates[0][1] + 1)])))
                liste.append(int("".join([line[cor] for cor in range(coordinates[0][0], coordinates[0][1] + 1)])))
                ans += int("".join([line[cor] for cor in range(coordinates[0][0], coordinates[0][1] + 1)]))

    else:
        if numberfound:
            coordinates = ((x_line - len(number) + 1, x_line), y_line)
            if haveNeighbor(coordinates, data):
                print("number:", int("".join([line[cor] for cor in range(coordinates[0][0], coordinates[0][1] + 1)])))
                liste.append(int("".join([line[cor] for cor in range(coordinates[0][0], coordinates[0][1] + 1)])))
                ans += int("".join([line[cor] for cor in range(coordinates[0][0], coordinates[0][1] + 1)]))
aof.answer(ans, 3, 1)

# PART TWO


ans = 0

# aof.answer(ans, 3, 2)
