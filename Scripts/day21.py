import numpy as np
from copy import copy

file = open("Data/day21.txt", "r")

for i, line in enumerate(file):
    line = line.strip()

    if i == 0:
        dim = len(line)
        grid = np.zeros([dim, dim])
    
    for j, char in enumerate(line):
        
        if char == "#":
            grid[i, j] = 1
        
        if char == "S":
            start_pos = (i, j)

def count_individual_grid(grid, start_position, steps):

    grid[start_position] = 2

    for _ in range(steps):
        new_tiles = set()

        for i in range(dim):
            for j in range(dim):

                if grid[i, j] != 0:
                    continue

                if i > 0 and grid[i-1, j] == 2:
                    new_tiles.add((i, j))
                    continue

                if i < dim-1 and grid[i+1, j] == 2:
                    new_tiles.add((i, j))
                    continue

                if j > 0 and grid[i, j-1] == 2:
                    new_tiles.add((i, j))
                    continue

                if j < dim-1 and grid[i, j+1] == 2:
                    new_tiles.add((i, j))
                    continue
        
        for tile in new_tiles:
            grid[tile] = 2

    count = 0

    if (start_position[0]%2 + start_position[1]%2 + steps%2)%2 == 0:

        for i in range(dim):
            for j in range(dim):
                
                if i%2 == j%2 and grid[i, j] == 2:
                    count += 1
    
    else:

        for i in range(dim):
            for j in range(dim):
                
                if i%2 != j%2 and grid[i, j] == 2:
                    count += 1
    
    return count

print(f"Part one: {count_individual_grid(copy(grid), start_pos, 64)}")

steps = 26501365
count = 0

internal_width = 2 * round(steps/dim) - 1

# Full grids
count += (2 * (internal_width//4) + 1)**2 * count_individual_grid(copy(grid), start_pos, dim + dim%2 + steps%2) # Central grids
count += (2 * ((internal_width + 2)//4))**2 * count_individual_grid(copy(grid), start_pos, dim + dim%2 + steps%2 + 1) # Opposite grids

# Corner grids
remaining_steps = steps - (internal_width//2 * dim) - (dim//2 + 1)

count += count_individual_grid(copy(grid), (start_pos[0], 0), remaining_steps)
count += count_individual_grid(copy(grid), (start_pos[0], dim-1), remaining_steps)
count += count_individual_grid(copy(grid), (0, start_pos[1]), remaining_steps)
count += count_individual_grid(copy(grid), (dim-1, start_pos[1]), remaining_steps)

# Large edge grids
remaining_steps = steps - ((internal_width//2 - 1) * dim) - (dim + 1)

count += (internal_width//2) * count_individual_grid(copy(grid), (0, 0), remaining_steps)
count += (internal_width//2) * count_individual_grid(copy(grid), (0, dim-1), remaining_steps)
count += (internal_width//2) * count_individual_grid(copy(grid), (dim-1, 0), remaining_steps)
count += (internal_width//2) * count_individual_grid(copy(grid), (dim-1, dim-1), remaining_steps)

# Small edge grids
remaining_steps = steps - ((internal_width//2) * dim) - (dim + 1)

count += (internal_width//2 + 1) * count_individual_grid(copy(grid), (0, 0), remaining_steps)
count += (internal_width//2 + 1) * count_individual_grid(copy(grid), (0, dim-1), remaining_steps)
count += (internal_width//2 + 1) * count_individual_grid(copy(grid), (dim-1, 0), remaining_steps)
count += (internal_width//2 + 1) * count_individual_grid(copy(grid), (dim-1, dim-1), remaining_steps)

print(f"Part two: {count}")