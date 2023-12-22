import numpy as np

file = open("Data/day16.txt", "r")

for i, line in enumerate(file):
    line = line.strip()

    if i == 0:
        dim = len(line)
        grid = np.zeros([dim, dim], dtype = int)
    
    for j, char in enumerate(line):

        if char == "|":
            grid[i, j] = 1
        elif char == "-":
            grid[i, j] = 2
        elif char == "/":
            grid[i, j] = 3
        elif char == "\\":
            grid[i, j] = 4

def count_energised_tiles(grid, entry):

    energised = np.zeros([dim, dim], dtype = int)
    checked = set()
    beams = [entry]

    while beams:
        beam = beams.pop(0)
        
        if beam in checked:
            continue

        checked.add(beam)

        if beam[0] < 0 or beam[1] < 0 or beam[0] >= dim or beam[1] >= dim:
            continue

        energised[beam[0], beam[1]] = 1

        if grid[beam[0], beam[1]] == 0:
            if beam[2] == 0:
                beams.append((beam[0] - 1, beam[1], 0))
            elif beam[2] == 1:
                beams.append((beam[0], beam[1] + 1, 1))
            elif beam[2] == 2:
                beams.append((beam[0] + 1, beam[1], 2))
            elif beam[2] == 3:
                beams.append((beam[0], beam[1] - 1, 3))
            continue

        if grid[beam[0], beam[1]] == 1:
            if beam[2] == 0:
                beams.append((beam[0] - 1, beam[1], 0))
            elif beam[2] == 2:
                beams.append((beam[0] + 1, beam[1], 2))
            else:
                beams.append((beam[0] - 1, beam[1], 0))
                beams.append((beam[0] + 1, beam[1], 2))
            continue

        if grid[beam[0], beam[1]] == 2:
            if beam[2] == 1:
                beams.append((beam[0], beam[1] + 1, 1))
            elif beam[2] == 3:
                beams.append((beam[0], beam[1] - 1, 3))
            else:
                beams.append((beam[0], beam[1] + 1, 1))
                beams.append((beam[0], beam[1] - 1, 3))
            continue

        if grid[beam[0], beam[1]] == 3:
            if beam[2] == 0:
                beams.append((beam[0], beam[1] + 1, 1))
            elif beam[2] == 1:
                beams.append((beam[0] - 1, beam[1], 0))
            elif beam[2] == 2:
                beams.append((beam[0], beam[1] - 1, 3))
            elif beam[2] == 3:
                beams.append((beam[0] + 1, beam[1], 2))
            continue

        if grid[beam[0], beam[1]] == 4:
            if beam[2] == 0:
                beams.append((beam[0], beam[1] - 1, 3))
            elif beam[2] == 1:
                beams.append((beam[0] + 1, beam[1], 2))
            elif beam[2] == 2:
                beams.append((beam[0], beam[1] + 1, 1))
            elif beam[2] == 3:
                beams.append((beam[0] - 1, beam[1], 0))
            continue
    
    return sum(sum(energised))

print(f"Part one: {count_energised_tiles(grid, (0, 0, 1))}")

maximum = 0

for i in range(dim):
    maximum = max(maximum, count_energised_tiles(grid, (0, i, 2)))
    maximum = max(maximum, count_energised_tiles(grid, (dim-1, i, 0)))
    maximum = max(maximum, count_energised_tiles(grid, (i, 0, 1)))
    maximum = max(maximum, count_energised_tiles(grid, (i, dim-1, 3)))

print(f"Part two: {maximum}")
