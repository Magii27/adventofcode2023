import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(4, splitter)
data = aof.getDayData_str(4, splitter)

print("Data:", data)

# PART ONE
ans = 0

for line in data:
    tmp_line = line[line.find(":") + 2:]
    tmp_line = tmp_line.split(" | ")
    set_1 = list(map(int, list(filter(None, tmp_line[0].split(" ")))))
    set_2 = list(map(int, list(filter(None, tmp_line[1].split(" ")))))

    tmp_ans = 0
    for item in set_1:
        if item in set_2:
            if tmp_ans == 0:
                tmp_ans = 1

            else:
                tmp_ans *= 2

    ans += tmp_ans

aof.answer(ans, 4, 1)

# PART TWO
ans = 0

iteration_data = data.copy()

i = 0
while i <= len(iteration_data) - 1:
    current_game = int(
        iteration_data[i].split(":")[0][iteration_data[i].split(":")[0].find("Card") + 4:].replace(" ", ""))

    tmp_line = iteration_data[i][iteration_data[i].find(":") + 2:]
    tmp_line = tmp_line.split(" | ")
    set_1 = list(map(int, list(filter(None, tmp_line[0].split(" ")))))
    set_2 = list(map(int, list(filter(None, tmp_line[1].split(" ")))))

    tmp_ans = 0
    found = 0
    for item in set_1:
        if item in set_2:
            found += 1

    inserting_on = 1
    for i_found in range(found):
        iteration_data.insert(i + inserting_on, data[current_game + i_found])
        inserting_on += 2

    i += 1

ans = len(iteration_data)
aof.answer(ans, 4, 2)
