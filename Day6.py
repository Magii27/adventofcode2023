import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(6, splitter)
data = aof.getDayData_str(6, splitter)

print("Data:", data)
times = [int(num) for num in data[0].split(" ") if num.isnumeric()]
distances = [int(num) for num in data[1].split(" ") if num.isnumeric()]


# PART ONE
def getNumsHigh(time, tmp_time, distance):
    if not (time - tmp_time) * tmp_time > distance:
        return getNumsHigh(time, tmp_time + 1, distance)

    else:
        return tmp_time


def getNumsLow(time, tmp_time, distance):
    if not (time - tmp_time) * tmp_time > distance:
        return getNumsLow(time, tmp_time - 1, distance)

    else:
        return tmp_time


ans = 1

for i in range(len(times)):
    low = getNumsHigh(times[i], 1, distances[i])
    high = getNumsLow(times[i], times[i] - 1, distances[i])
    ans *= high - low + 1

aof.answer(ans, 6, 1)

# PART TWO
ans = 0

time = int(data[0].split(":")[1].replace(" ", ""))
distance = int(data[1].split(":")[1].replace(" ", ""))

blow = False
bhigh = True

nlow = 0
nhigh = 0
for i in range(1, time + 1):
    if i * (time - i) >= distance and not blow:
        blow = True
        bhigh = False
        nlow = i

    if i * (time - i) < distance and bhigh is False:
        bHigh = True
        nhigh = i
        break

ans = nhigh - nlow

aof.answer(ans, 6, 2)
