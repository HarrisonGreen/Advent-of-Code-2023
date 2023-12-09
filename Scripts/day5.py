file = open("Data/day5.txt", "r")

ranges = {}
group = 0

for i, line in enumerate(file):
    line = line.strip()

    if i == 0:
        seeds = [int(x) for x in line.split()[1:]]
    elif line == "":
        group += 1
    elif len(line.split()) == 3:
        ranges[group] = ranges.get(group, []) + [[int(x) for x in line.split()]]

def find_destination(number, level):
    for mapping in ranges[level]:
        if mapping[1] <= number < mapping[1] + mapping[2]:
            return number + mapping[0] - mapping[1]
    
    return number

def find_destination_ranges(number, num_range, level):
    
    for mapping in ranges[level]:
        if number >= mapping[1] and number + num_range <= mapping[1] + mapping[2]:
            return [(number + mapping[0] - mapping[1], num_range, level + 1)]
        elif number <= mapping[1] and number + num_range >= mapping[1] + mapping[2]:
            return [(mapping[0], mapping[2], level + 1), (number, mapping[1] - number, level), (mapping[1] + mapping[2], number + num_range - mapping[1] - mapping[2], level)]
        elif number <= mapping[1] and number + num_range > mapping[1]:
            return [(mapping[0], number + num_range - mapping[1], level + 1), (number, mapping[1] - number, level)]
        elif number < mapping[1] + mapping[2] and number + num_range > mapping[1] + mapping[2]:
            return [(number + mapping[0] - mapping[1], mapping[1] + mapping[2] - number, level + 1), (mapping[1] + mapping[2], number + num_range - mapping[1] - mapping[2], level)]
    
    return [(number, num_range, level + 1)]

locations = []
n = len(ranges)

for number in seeds:
    for i in range(1, n + 1):
        number = find_destination(number, i)
    
    locations.append(number)

print(f"Part one: {min(locations)}")

locations = []
to_check = [(seeds[2 * i], seeds[2 * i + 1], 1) for i in range(len(seeds)//2)]

while to_check:
    current_item = to_check.pop(0)
    next_states = find_destination_ranges(current_item[0], current_item[1], current_item[2])

    for state in next_states:
        if state[1] <= 0:
            continue
        elif state[2] == n + 1:
            locations.append(state[0])
        else:
            to_check.append(state)

print(f"Part two: {min(locations)}")
