import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(1, splitter)
data = aof.getDayData_str(1, splitter)

print("Data:", data)

# PART ONE

results = []
for line in data:
    tmp = ""
    for letter in line:
        if letter.isnumeric():
            tmp += letter

    if len(tmp) > 2:
        tmp = tmp[0] + tmp[-1]

    elif len(tmp) == 1:
        tmp += tmp

    results.append(tmp)

ans = 0
for number in results:
    ans += int(number)

aof.answer(ans, 1, 1)

# PART TWO

numbersText = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

results = []
for line in data:
    indexList = []
    numberList = []
    for numberText in numbersText:
        if numberText in line:
            if line.count(numberText) > 1:

                tmp_line = line
                lost = 0
                while tmp_line.find(numberText) >= 0:
                    indexList.append(tmp_line.find(numberText) + lost)
                    numberList.append(int(numbersText.index(numberText)) + 1)

                    lost += tmp_line.find(numberText) + len(numberText)
                    tmp_line = tmp_line[tmp_line.find(numberText) + len(numberText):]


            else:
                indexList.append(line.find(numberText))
                numberList.append(int(numbersText.index(numberText)) + 1)

    for i, letter in enumerate(line):
        if letter.isnumeric():
           indexList.append(i)
           numberList.append(int(letter))

    index_min = 100000
    index_max = 0

    first_num = -1
    second_num = -1

    for index_num, index in enumerate(indexList):
        if index < index_min:
            index_min = index
            first_num = numberList[index_num]

        if index > index_max:
            index_max = index
            second_num = numberList[index_num]

    if second_num == -1:
        second_num = first_num

    if first_num == -1:
        first_num = second_num

    results.append(str(first_num) + str(second_num))

ans = 0
for number in results:
    ans += int(number)

aof.answer(ans, 1, 2)
