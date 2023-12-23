import numpy as np

file = open("Data/day17.txt", "r")

for i, line in enumerate(file):
    line = line.strip()

    if i == 0:
        dim = len(line)
        grid = np.zeros([dim, dim], dtype = int)
    
    for j, char in enumerate(line):
        grid[i, j] = char

def min_heat_loss(grid, min_line, max_line):

    provisional_states = {(1, 0, 2, 1): grid[1, 0], (0, 1, 1, 1): grid[0, 1]}
    final_states = {}

    while provisional_states:

        lowest_dist = 1e6
        for state, dist in provisional_states.items():
            if dist < lowest_dist:
                lowest_dist = dist
                current = state
        
        provisional_states.pop(current)
        final_states[current] = lowest_dist
        
        if current[3] >= min_line:

            if (current[2]+1) % 4 == 0:
                right_block = (current[0]-1, current[1], 0, 1)
            elif (current[2]+1) % 4 == 1:
                right_block = (current[0], current[1]+1, 1, 1)
            elif (current[2]+1) % 4 == 2:
                right_block = (current[0]+1, current[1], 2, 1)
            elif (current[2]+1) % 4 == 3:
                right_block = (current[0], current[1]-1, 3, 1)
            
            if 0 <= right_block[0] <= dim-1 and 0 <= right_block[1] <= dim-1 and right_block not in final_states.keys():
                provisional_states[right_block] = min(provisional_states.get(right_block, 1e6), lowest_dist + grid[right_block[0:2]])
        
        if current[3] >= min_line:

            if (current[2]-1) % 4 == 0:
                left_block = (current[0]-1, current[1], 0, 1)
            elif (current[2]-1) % 4 == 1:
                left_block = (current[0], current[1]+1, 1, 1)
            elif (current[2]-1) % 4 == 2:
                left_block = (current[0]+1, current[1], 2, 1)
            elif (current[2]-1) % 4 == 3:
                left_block = (current[0], current[1]-1, 3, 1)
            
            if 0 <= left_block[0] <= dim-1 and 0 <= left_block[1] <= dim-1 and left_block not in final_states.keys():
                provisional_states[left_block] = min(provisional_states.get(left_block, 1e6), lowest_dist + grid[left_block[0:2]])
        
        if current[3] < max_line:

            if current[2] % 4 == 0:
                straight_block = (current[0]-1, current[1], 0, current[3]+1)
            elif current[2] % 4 == 1:
                straight_block = (current[0], current[1]+1, 1, current[3]+1)
            elif current[2] % 4 == 2:
                straight_block = (current[0]+1, current[1], 2, current[3]+1)
            elif current[2] % 4 == 3:
                straight_block = (current[0], current[1]-1, 3, current[3]+1)
            
            if 0 <= straight_block[0] <= dim-1 and 0 <= straight_block[1] <= dim-1 and straight_block not in final_states.keys():
                provisional_states[straight_block] = min(provisional_states.get(straight_block, 1e6), lowest_dist + grid[straight_block[0:2]])

    shortest_dist = 1e6

    for state, dist in final_states.items():
        if state[0] == dim-1 and state[1] == dim-1 and current[3] >= min_line:
            shortest_dist = min(shortest_dist, dist)
    
    return shortest_dist

print(f"Part one: {min_heat_loss(grid, 0, 3)}")
print(f"Part one: {min_heat_loss(grid, 4, 10)}")
