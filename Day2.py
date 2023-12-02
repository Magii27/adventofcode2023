import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(2, splitter)
data = aof.getDayData_str(2, splitter)

print("Data:", data)

# PART ONE
ans = 0

colors = {"blue": 14, "green": 13, "red": 12}

for index, game in enumerate(data):
    count = True

    tmp_game = game[game.find(":") + 2:]
    for playset in tmp_game.split("; "):
        for item in playset.split(", "):
            if int(item.split(" ")[0]) > colors[item.split(" ")[1]]:
                count = False
                break

        if not count:
            break

    if count:
        ans += index + 1

aof.answer(ans, 2, 1)

# PART TWO
ans = 0

for index, game in enumerate(data):
    count = True

    tmp_game = game[game.find(":") + 2:]
    colors_min = {"red": 0, "green": 0, "blue": 0}
    for playset in tmp_game.split("; "):
        for item in playset.split(", "):
            split_items = item.split(" ")
            if int(split_items[0]) > colors_min[split_items[1]]:
                colors_min[split_items[1]] = int(split_items[0])

    ans += colors_min["red"] * colors_min["green"] * colors_min["blue"]

aof.answer(ans, 2, 2)
