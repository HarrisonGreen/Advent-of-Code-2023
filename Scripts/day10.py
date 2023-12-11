import numpy as np

file = open("Data/day10.txt", "r")

for i, line in enumerate(file):
    line = line.strip()

    if i == 0:
        dim = 2 * len(line)
        grid = np.zeros([dim, dim], dtype = int)

    for j, char in enumerate(line):
        if char == "|":
            grid[2*i, 2*j] = 1
        elif char == "-":
            grid[2*i, 2*j] = 2
        elif char == "L":
            grid[2*i, 2*j] = 3
        elif char == "J":
            grid[2*i, 2*j] = 4
        elif char == "7":
            grid[2*i, 2*j] = 5
        elif char == "F":
            grid[2*i, 2*j] = 6
        elif char == "S":
            grid[2*i, 2*j] = 7
            pos = (2*i, 2*j)

def get_directions(square):
    if square == 1:
        return (0, 2)
    elif square == 2:
        return (1, 3)
    elif square == 3:
        return (0, 1)
    elif square == 4:
        return (0, 3)
    elif square == 5:
        return (2, 3)
    elif square == 6:
        return (1, 2)
    else:
        return ()

if 2 in get_directions(grid[pos[0]-2, pos[1]]):
    direction = 0
elif 3 in get_directions(grid[pos[0], pos[1]+2]):
    direction = 1
else:
    direction = 2

main_loop = [pos]

while True:
    if direction == 0:
        main_loop.append((pos[0]-1, pos[1]))
        pos = (pos[0]-2, pos[1])
    elif direction == 1:
        main_loop.append((pos[0], pos[1]+1))
        pos = (pos[0], pos[1]+2)
    elif direction == 2:
        main_loop.append((pos[0]+1, pos[1]))
        pos = (pos[0]+2, pos[1])
    else:
        main_loop.append((pos[0], pos[1]-1))
        pos = (pos[0], pos[1]-2)

    if grid[pos] == 7:
        break
    
    main_loop.append(pos)
    new_directions = get_directions(grid[pos])

    if abs(new_directions[0] - direction) == 2:
        direction = new_directions[1]
    else:
        direction = new_directions[0]

print(f"Part one: {len(main_loop)//4}")

outside_squares = set()
checked = set()
to_check = set()
for i in range(dim):
    to_check.add((0, i))
    to_check.add((i, 0))
    to_check.add((i, dim-1))
    to_check.add((dim-1, i))

while to_check:
    current = to_check.pop()

    if current in checked or current in main_loop:
        continue

    checked.add(current)
    outside_squares.add(current)
    adjacent = []

    if current[0] > 0:
        adjacent.append((current[0]-1, current[1]))
    if current[0] < dim-1:
        adjacent.append((current[0]+1, current[1]))
    if current[1] > 0:
        adjacent.append((current[0], current[1]-1))
    if current[1] < dim-1:
        adjacent.append((current[0], current[1]+1))
    
    for square in adjacent:
        if square in checked or square in outside_squares or square in main_loop:
            pass
        else:
            outside_squares.add(square)
            to_check.add(square)

outside_count = 0
for square in outside_squares:
    if square[0]%2 == 0 and square[1]%2 == 0:
        outside_count += 1

inside_count = dim*dim//4 - len(main_loop)//2 - outside_count
print(f"Part two: {inside_count}")
