file = open("Data/day15.txt", "r")

for line in file:
    line = line.split(",")

def get_hash(string):
    current = 0

    for char in string:
        current = (17 * (current + ord(char))) % 256
    
    return current

total = 0

for string in line:
    
    total += get_hash(string)

print(f"Part one: {total}")

lenses = {i: [] for i in range(256)}

for string in line:

    if string[-1] == "-":
        label = string[:-1]
        action = "remove"

    else:
        string = string.split("=")
        label = string[0]
        lens = int(string[1])
        action = "add"
    
    box = get_hash(label)
    found = False

    for i in range(len(lenses[box])):

        if lenses[box][i][0] == label:
            found = True
            break
    
    if found:
        if action == "remove":
            lenses[box] = lenses[box][:i] + lenses[box][i+1:]

        else:
            lenses[box] = lenses[box][:i] + [(label, lens)] + lenses[box][i+1:]
    
    elif action == "add":
        lenses[box] = lenses[box] + [(label, lens)]

total = 0

for box in range(256):
    for i in range(len(lenses[box])):
        total += (box + 1) * (i + 1) * lenses[box][i][1]

print(f"Part two: {total}")
