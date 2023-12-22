import numpy as np

file = open("Data/day14.txt", "r")

for i, line in enumerate(file):
    line = line.strip()

    if i == 0:
        dim = len(line)
        grid = np.zeros([dim, dim])

    for j, char in enumerate(line):
        if char == "O":
            grid[i, j] = 1
        elif char == "#":
            grid[i, j] = 2

def tilt_grid(grid, direction):
    change = True

    while change:
        change = False

        if direction == 0:

            for i in range(1, dim):
                for j in range(dim):
                    if grid[i, j] == 1 and grid[i-1, j] == 0:
                        change = True
                        grid[i, j] = 0
                        grid[i-1, j] = 1
        
        elif direction == 1:

            for i in range(dim):
                for j in range(1, dim):
                    if grid[i, j] == 1 and grid[i, j-1] == 0:
                        change = True
                        grid[i, j] = 0
                        grid[i, j-1] = 1
        
        elif direction == 2:

            for i in range(dim-1):
                for j in range(dim):
                    if grid[i, j] == 1 and grid[i+1, j] == 0:
                        change = True
                        grid[i, j] = 0
                        grid[i+1, j] = 1
        
        elif direction == 3:

            for i in range(dim):
                for j in range(dim-1):
                    if grid[i, j] == 1 and grid[i, j+1] == 0:
                        change = True
                        grid[i, j] = 0
                        grid[i, j+1] = 1
    
    return grid

def calculate_load(grid):
    total = 0

    for i in range(dim):
        for j in range(dim):
            if grid[i, j] == 1:
                total += dim - i
    
    return total

grid = tilt_grid(grid, 0)
load = calculate_load(grid)

print(f"Part one: {load}")

cycles = 0
history = []

while cycles < 200:
    cycles += 1

    grid = tilt_grid(grid, 0)
    grid = tilt_grid(grid, 1)
    grid = tilt_grid(grid, 2)
    grid = tilt_grid(grid, 3)
    load = calculate_load(grid)

    history.append(load)

for i in range(198, 0, -1):
    if history[i] == history[-1]:
        length = 199 - i
        break

index = 1000000000 - (1 + (1000000000-200)//length) * length - 1
print(f"Part two: {history[index]}")
