from copy import copy
import functools

file = open("Data/day12.txt", "r")

springs = []

for line in file:
    line = line.split()
    line = [tuple(x for x in line[0]), tuple(int(x) for x in line[1].split(","))]
    springs.append(line)

@functools.cache
def check_valid(row, counts, current):
    row = list(row)
    counts = list(counts)

    # Reached end of row
    if not row:
        if not counts and current == 0:
            return 1
        
        if len(counts) == 1 and counts[0] == current:
            return 1
        
        return 0
    
    state = row.pop(0)
    
    # No more damaged springs
    if not counts:
        if current > 0 or state == "#":
            return 0
        
        return check_valid(tuple(row), tuple(counts), 0)
    
    # Next spring undamaged
    if state == ".":
        if current == 0:
            return check_valid(tuple(row), tuple(counts), 0)
        
        count = counts.pop(0)
        if current == count:
            return check_valid(tuple(row), tuple(counts), 0)
        
        return 0
    
    # Next spring damaged
    if state == "#":
        current += 1
        if current > counts[0]:
            return 0
        
        return check_valid(tuple(row), tuple(counts), copy(current))
    
    # Next spring unknown
    if current > 0:
        if current < counts[0]:
            return check_valid(tuple(row), tuple(counts), copy(current) + 1)
        
        counts.pop(0)
        return check_valid(tuple(row), tuple(counts), 0)
    
    return check_valid(tuple(row), tuple(counts), 0) + check_valid(tuple(row), tuple(counts), 1)

total = 0

for item in springs:
    row = item[0]
    counts = item[1]

    total += check_valid(row, counts, 0)

print(f"Part one: {total}")

total = 0

for item in springs:
    row = item[0]
    counts = item[1]

    row = row + ("?",) + row + ("?",) + row + ("?",) + row + ("?",) + row
    counts = counts + counts + counts + counts + counts

    total += check_valid(row, counts, 0)

print(f"Part two: {total}")
