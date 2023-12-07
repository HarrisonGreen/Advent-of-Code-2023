file = open("Data/day4.txt", "r")

cards = {}

for line in file:
    line = line.strip().split("|")

    card_number = int(line[0].split()[1][:-1])
    win = tuple(int(x) for x in line[0].split()[2:])
    card = tuple(int(x) for x in line[1].split())

    cards[card_number] = (win, card)

points = 0
count = {x: 1 for x in range(1, len(cards) + 1)}

for card_number, data in cards.items():
    matches = len(set(data[0]).intersection(set(data[1])))
    points += int(2 ** (matches - 1))

    for i in range(matches):
        count[card_number + i + 1] += count[card_number]

print(f"Part one: {points}")
print(f"Part two: {sum(count.values())}")
