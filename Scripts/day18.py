file = open("Data/day18.txt", "r")

dig_plan = []
second_plan = []

for line in file:
    line = line.split()
    line = [line[0], int(line[1]), int(line[2][2:7], 16), int(line[2][7], 16)]

    if line[0] == "R":
        line[0] = 0
    elif line[0] == "D":
        line[0] = 1
    elif line[0] == "L":
        line[0] = 2
    elif line[0] == "U":
        line[0] = 3
    
    dig_plan.append((line[0], line[1]))
    second_plan.append((line[3], line[2]))

def find_area(plan):
    pos = [0, 0]

    # List of main vertices
    corners = [tuple(pos)]

    for instr in plan:

        if instr[0] == 0:
            pos[1] += instr[1]
        elif instr[0] == 1:
            pos[0] += instr[1]
        elif instr[0] == 2:
            pos[1] -= instr[1]
        elif instr[0] == 3:
            pos[0] -= instr[1]
        
        corners.append(tuple(pos))
    
    x_points = {corners[i][1] for i in range(len(corners))}
    y_points = {corners[i][0] for i in range(len(corners))}

    x_points.add(min(x_points)-1)
    y_points.add(min(y_points)-1)
    x_points.add(max(x_points)+1)
    y_points.add(max(y_points)+1)

    # Lists of x and y values to divide grid into blocks
    x_points = sorted(list(x_points))
    y_points = sorted(list(y_points))

    prev_x = {x_points[i]: x_points[i-1] for i in range(1, len(x_points))}
    next_x = {x_points[i]: x_points[i+1] for i in range(len(x_points) - 1)}
    prev_y = {y_points[i]: y_points[i-1] for i in range(1, len(y_points))}
    next_y = {y_points[i]: y_points[i+1] for i in range(len(y_points) - 1)}

    # Extended list of vertices with edges divided by block grid
    full_corners = [(0, 0)]

    for i in range(1, len(corners)):

        if corners[i][0] == full_corners[-1][0]: # Moving horizontally
            while corners[i][1] > full_corners[-1][1]: # Moving right
                full_corners.append((full_corners[-1][0], next_x[full_corners[-1][1]]))
            while corners[i][1] < full_corners[-1][1]: # Moving left
                full_corners.append((full_corners[-1][0], prev_x[full_corners[-1][1]]))
        
        else: # Moving vertically
            while corners[i][0] > full_corners[-1][0]: # Moving down
                full_corners.append((next_y[full_corners[-1][0]], full_corners[-1][1]))
            while corners[i][0] < full_corners[-1][0]: # Moving up
                full_corners.append((prev_y[full_corners[-1][0]], full_corners[-1][1]))
    
    next_corner = {full_corners[i]: full_corners[i+1] for i in range(len(full_corners) - 1)}
    prev_corner = {full_corners[i+1]: full_corners[i] for i in range(len(full_corners) - 1)}

    to_check = {(y_points[0], x_points[0], y_points[1], x_points[1])}
    outside_blocks = {(y_points[0], x_points[0], y_points[1], x_points[1])}
    checked = set()

    while to_check:
        current = to_check.pop()
        checked.add(current)

        top_left = (current[0], current[1])
        top_right = (current[0], current[3])
        bottom_left = (current[2], current[1])
        bottom_right = (current[2], current[3])

        if current[0] != y_points[0]:
            if not (top_left in full_corners and (next_corner[top_left] == top_right or prev_corner[top_left] == top_right)):
                to_top = (prev_y[current[0]], current[1], current[0], current[3])
                if to_top not in checked:
                    to_check.add(to_top)
                    outside_blocks.add(to_top)
        
        if current[2] != y_points[-1]:
            if not (bottom_left in full_corners and (next_corner[bottom_left] == bottom_right or prev_corner[bottom_left] == bottom_right)):
                to_bottom = (current[2], current[1], next_y[current[2]], current[3])
                if to_bottom not in checked:
                    to_check.add(to_bottom)
                    outside_blocks.add(to_bottom)
        
        if current[1] != x_points[0]:
            if not (top_left in full_corners and (next_corner[top_left] == bottom_left or prev_corner[top_left] == bottom_left)):
                to_left = (current[0], prev_x[current[1]], current[2], current[1])
                if to_left not in checked:
                    to_check.add(to_left)
                    outside_blocks.add(to_left)
        
        if current[3] != x_points[-1]:
            if not (top_right in full_corners and (next_corner[top_right] == bottom_right or prev_corner[top_right] == bottom_right)):
                to_right = (current[0], current[3], current[2], next_x[current[3]])
                if to_right not in checked:
                    to_check.add(to_right)
                    outside_blocks.add(to_right)
    
    edge_set = set()
    corner_set = set()
    outside_area = 0

    for block in outside_blocks:
        outside_area += (block[2] - block[0] - 1) * (block[3] - block[1] - 1) # Add interior area

        if block[0] == y_points[0] or (prev_y[block[0]], block[1], block[0], block[3]) in outside_blocks: # Add top edge
            edge_set.add((block[0], block[1], block[0], block[3]))
        
        if block[2] == y_points[-1] or (block[2], block[1], next_y[block[2]], block[3]) in outside_blocks: # Add bottom edge
            edge_set.add((block[2], block[1], block[2], block[3]))
        
        if block[1] == x_points[0] or (block[0], prev_x[block[1]], block[2], block[1]) in outside_blocks: # Add left edge
            edge_set.add((block[0], block[1], block[2], block[1]))
        
        if block[3] == x_points[-1] or (block[0], block[3], block[2], next_x[block[3]]) in outside_blocks: # Add right edge
            edge_set.add((block[0], block[3], block[2], block[3]))
        
        if block[0] == y_points[0] or block[3] == x_points[-1] or ((prev_y[block[0]], block[1], block[0], block[3]) in outside_blocks and
                                                                   (block[0], block[3], block[2], next_x[block[3]]) in outside_blocks and
                                                                   (prev_y[block[0]], block[3], block[0], next_x[block[3]]) in outside_blocks):
            corner_set.add((block[0], block[3])) # Add top right corner
        
        if block[2] == y_points[-1] or block[3] == x_points[-1] or ((block[2], block[1], next_y[block[2]], block[3]) in outside_blocks and
                                                                    (block[0], block[3], block[2], next_x[block[3]]) in outside_blocks and
                                                                    (block[2], block[3], next_y[block[2]], next_x[block[3]]) in outside_blocks):
            corner_set.add((block[2], block[3])) # Add bottom right corner
        
        if block[2] == y_points[-1] or block[1] == x_points[0] or ((block[2], block[1], next_y[block[2]], block[3]) in outside_blocks and
                                                                   (block[0], prev_x[block[1]], block[2], block[1]) in outside_blocks and
                                                                   (block[2], prev_x[block[1]], next_y[block[2]], block[1]) in outside_blocks):
            corner_set.add((block[2], block[1])) # Add bottom left corner
        
        if block[0] == y_points[0] or block[1] == x_points[0] or ((prev_y[block[0]], block[1], block[0], block[3]) in outside_blocks and
                                                                   (block[0], prev_x[block[1]], block[2], block[1]) in outside_blocks and
                                                                   (prev_y[block[0]], prev_x[block[1]], block[0], block[1]) in outside_blocks):
            corner_set.add((block[0], block[1])) # Add top left corner
    
    total_area = (y_points[-1] - y_points[0] + 1) * (x_points[-1] - x_points[0] + 1)

    for edge in edge_set:
        if edge[0] == edge[2]:
            outside_area += edge[3] - edge[1] - 1
        else:
            outside_area += edge[2] - edge[0] - 1

    outside_area += len(corner_set)

    return total_area - outside_area

print(f"Part one: {find_area(dig_plan)}")
print(f"Part one: {find_area(second_plan)}")
