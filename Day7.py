import Default.adventofcode as aof

# IMPORT DATA
splitter = "\n"

# data = aof.getDayData_int(7, splitter)
data = aof.getDayData_str(7, splitter)
cards = []
bids = []
for line in data:
    cards.append(line.split(" ")[0])
    bids.append(int(line.split(" ")[1]))

# print("Data:", data)
print(cards)
print(bids)

# PART ONE
ans = 0


def getType(card):
    set_of_cards = set(card)
    if len(set_of_cards) == 1:
        # return 6 -> 5 of Kind
        return 6

    elif len(set_of_cards) == 2:
        if card.count(list(set_of_cards)[0]) == 4 or card.count(list(set_of_cards)[1]) == 4:
            # return 5 -> 4 of Kind
            return 5

        else:
            # return 4 -> Full house (3 and 2 Same)
            return 4

    elif len(set_of_cards) == 3:
        for s_card in set_of_cards:
            if card.count(s_card) == 3:
                # return 3 -> 3 of Kind
                return 3

        else:
            # return 2 -> 2 pairs
            return 2

    elif len(set_of_cards) == 4:
        # return 1 -> 1 pair
        return 1
    else:
        # return 0 -> for everyone different
        return 0


info = {6: "five of kind", 5: "four of kind", 4: "Full house", 3: "three of kind", 2: "two pairs", 1: "one pair",
        0: "all different"}

order = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7, "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0}
five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pairs = []
one_pair = []
all_diff = []

res = [all_diff, one_pair, two_pairs, three_of_kind, full_house, four_of_kind, five_of_kind]
for card in cards:
    r = getType(card)
    res[r].append(card)

ans_array = []
for arr in res:
    ans_array += sorted(arr, key=lambda x: [order[y] for y in x])

for i in range(len(ans_array)):
    ans += (i + 1) * bids[cards.index(ans_array[i])]
aof.answer(ans, 7, 1)

# PART TWO
ans = 0


def getType2(card):
    global order

    rp = ""
    rp_c = 0
    for place in card:
        if place != "J" and card.count(place) >= rp_c:
            rp_c = card.count(place)
            rp = place

    if rp != "":
        card = card.replace("J", rp)

    set_of_cards = set(card)
    if len(set_of_cards) == 1:
        # return 6 -> 5 of Kind
        return 6

    elif len(set_of_cards) == 2:
        if card.count(list(set_of_cards)[0]) == 4 or card.count(list(set_of_cards)[1]) == 4:
            # return 5 -> 4 of Kind
            return 5

        else:
            # return 4 -> Full house (3 and 2 Same)
            return 4

    elif len(set_of_cards) == 3:
        for s_card in set_of_cards:
            if card.count(s_card) == 3:
                # return 3 -> 3 of Kind
                return 3

        else:
            # return 2 -> 2 pairs
            return 2

    elif len(set_of_cards) == 4:
        # return 1 -> 1 pair
        return 1
    else:
        # return 0 -> for everyone different
        return 0


order = {"A": 12, "K": 11, "Q": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "J": 0}

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pairs = []
one_pair = []
all_diff = []

res = [all_diff, one_pair, two_pairs, three_of_kind, full_house, four_of_kind, five_of_kind]
for card in cards:
    r = getType2(card)
    res[r].append(card)

ans_array = []
for arr in res:
    ans_array += sorted(arr, key=lambda x: [order[y] for y in x])

for i in range(len(ans_array)):
    ans += (i + 1) * bids[cards.index(ans_array[i])]

aof.answer(ans, 7, 2)
