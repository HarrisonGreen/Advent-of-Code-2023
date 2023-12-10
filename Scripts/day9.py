file = open("Data/day9.txt", "r")

sequences = []

for line in file:
    line = [int(x) for x in line.split()]
    sequences.append(line)

def get_differences(sequence):
    return [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]

def next_value(sequence):
    differences = get_differences(sequence)
    rows = [differences]

    while len(set(differences)) > 1:
        differences = get_differences(differences)
        rows.append(differences)
    
    for i in range(len(rows)-2, -1, -1):
        rows[i].append(rows[i][-1] + rows[i+1][-1])
    
    return sequence[-1] + rows[0][-1]

total = 0

for sequence in sequences:
    total += next_value(sequence)

print(f"Part one: {total}")

def previous_value(sequence):
    differences = get_differences(sequence)
    rows = [differences]

    while len(set(differences)) > 1:
        differences = get_differences(differences)
        rows.append(differences)
    
    for i in range(len(rows)-2, -1, -1):
        rows[i] = [rows[i][0] - rows[i+1][0]] + rows[i]
    
    return sequence[0] - rows[0][0]

total = 0

for sequence in sequences:
    total += previous_value(sequence)

print(f"Part two: {total}")
