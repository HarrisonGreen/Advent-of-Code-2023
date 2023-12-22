file = open("Data/day13.txt", "r")

notes = []
note = []

for line in file:

    if line == "\n":
        notes.append(note)
        note = []
    else:
        row = []
        for char in line.strip():
            if char == ".":
                row.append(0)
            else:
                row.append(1)

        note.append(row)

notes.append(note)

def find_mirror(note):
    output = []

    for i in range(len(note) - 1):
        passed = True

        for j in range(min(i+1, len(note) - (i+1))):

            if tuple(note[i-j]) != tuple(note[i+j+1]):
                passed = False
                break
        
        if passed:
            output.append(100 * (i+1))
    
    cols = []

    for i in range(len(note[0])):
        cols.append([note[j][i] for j in range(len(note))])
    
    for i in range(len(cols) - 1):
        passed = True

        for j in range(min(i+1, len(cols) - (i+1))):

            if tuple(cols[i-j]) != tuple(cols[i+j+1]):
                passed = False
                break
        
        if passed:
            output.append(i+1)
    
    return output

total = 0
scores = {}

for i, note in enumerate(notes):
    score = find_mirror(note)
    total += score[0]
    scores[i] = score[0]

print(f"Part one: {total}")

total = 0

for i, note in enumerate(notes):
    positions = [(j, k) for j in range(len(note)) for k in range(len(note[0]))]

    for position in positions:
        note[position[0]][position[1]] = 1 - note[position[0]][position[1]]
        score = find_mirror(note)

        if len(score) == 1:
            if score[0] == scores[i]:
                note[position[0]][position[1]] = 1 - note[position[0]][position[1]]
                continue
            else:
                total += score[0]
                break
        elif len(score) == 0:
            note[position[0]][position[1]] = 1 - note[position[0]][position[1]]
            continue
        else:
            score.remove(scores[i])
            total += score[0]
            break

print(f"Part two: {total}")
