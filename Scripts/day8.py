from sympy import factorint

file = open("Data/day8.txt", "r")

nodes = {}

for i, line in enumerate(file):
    line = line.strip()

    if i == 0:
        directions = line
    elif i >= 2:
        line = line.split()
        line = (line[0], line[2][1:-1], line[3][:-1])
        nodes[line[0]] = {"L": line[1], "R": line[2]}

location = "AAA"
steps = 0
n = len(directions)

while location != "ZZZ":
    direction = directions[steps%n]
    location = nodes[location][direction]
    steps += 1

print(f"Part one: {steps}")

start_nodes = []

for node in nodes:
    if node[2] == "A":
        start_nodes.append(node)

cycle_lengths = []

for node in start_nodes:
    location = node
    steps = 0

    while location[2] != "Z":
        direction = directions[steps%n]
        location = nodes[location][direction]
        steps += 1
    
    cycle_lengths.append(steps)

factors = {}

for length in cycle_lengths:
    factorisation = factorint(length)
    
    for prime, power in factorisation.items():
        factors[prime] = max(factors.get(prime, 0), power)

product = 1

for prime, power in factors.items():
    product *= prime ** power

print(f"Part two: {product}")
