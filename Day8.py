import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(8, splitter)
data = aof.getDayData_str(8, splitter)

# PART ONE
instructions = data[0]
ins_dict = {"L": 0, "R": 1}
data_dict = {line.split(" = ")[0]: [val.replace("(", "").replace(")", "") for val in line.split(" = ")[1].split(", ")]
             for line in data[2:]}

print("Data:", data_dict)
ans = 0

pos = "AAA"
i = 0
c = 1
while True:
    if i == len(instructions):
        i = 0

    tmp_item = data_dict.get(pos)[ins_dict.get(instructions[i])]
    if tmp_item == "ZZZ":
        break

    else:
        pos = tmp_item
        c += 1

    i += 1

ans = c
aof.answer(ans, 8, 1)

# PART TWO
i = 0
c = []
start = []
for key in data_dict.keys():
    if key[2] == "A":
        start.append(key)

for pos in start:
    c_tmp = 1
    i = 0
    while True:
        if i == len(instructions):
            i = 0

        tmp_item = data_dict.get(pos)[ins_dict.get(instructions[i])]
        if tmp_item[2] == "Z":
            break

        else:
            pos = tmp_item
            c_tmp += 1

        i += 1

    c.append(c_tmp)

from functools import reduce
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def find_lcm(lst):
    return reduce(lcm, lst)


ans = find_lcm(c)

aof.answer(ans, 8, 2)
