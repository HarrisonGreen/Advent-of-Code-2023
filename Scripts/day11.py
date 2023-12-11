file = open("Data/day11.txt", "r")

galaxies = []

for i, line in enumerate(file):
    for j, char in enumerate(line):

        if char == "#":
            galaxies.append((i, j))

empty_rows = [x for x in range(i+1)]
empty_cols = [x for x in range(i+1)]

for galaxy in galaxies:
    if galaxy[0] in empty_rows:
        empty_rows.remove(galaxy[0])
    if galaxy[1] in empty_cols:
        empty_cols.remove(galaxy[1])

def get_distance(galaxy_one, galaxy_two, expansion):
    min_x = min(galaxy_one[1], galaxy_two[1])
    max_x = max(galaxy_one[1], galaxy_two[1])
    min_y = min(galaxy_one[0], galaxy_two[0])
    max_y = max(galaxy_one[0], galaxy_two[0])

    rows = [y for y in empty_rows if y > min_y and y < max_y]
    cols = [x for x in empty_cols if x > min_x and x < max_x]

    return (max_x - min_x) + (max_y - min_y) + (expansion-1) * (len(rows) + len(cols))

total = 0

for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        total += get_distance(galaxies[i], galaxies[j], 2)

print(f"Part one: {total}")

total = 0

for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        total += get_distance(galaxies[i], galaxies[j], 1000000)

print(f"Part two: {total}")
