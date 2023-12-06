file = open("Data/day2.txt", "r")

games = {}

for line in file:

    line = line.strip("\n").split(":")
    line = [line[0]] + line[1].split(";")

    game_number = int(line[0].split()[1])
    games[game_number] = []

    for i in range(1, len(line)):

        cubes = line[i].replace(",", "").split()
        cubes = {cubes[2*i + 1]: int(cubes[2*i]) for i in range(len(cubes)//2)}
        games[game_number].append(cubes)

total = 0
powersum = 0
red_limit = 12
green_limit = 13
blue_limit = 14

for key, value in games.items():
    possible = True
    red_min = 0
    green_min = 0
    blue_min = 0
    
    for cubes in value:
        if cubes.get("red", 0) > red_limit or cubes.get("green", 0) > green_limit or cubes.get("blue", 0) > blue_limit:
            possible = False
        
        red_min = max(red_min, cubes.get("red", 0))
        green_min = max(green_min, cubes.get("green", 0))
        blue_min = max(blue_min, cubes.get("blue", 0))
    
    if possible:
        total += key
    
    powersum = powersum + red_min * green_min * blue_min

print(f"Part one: {total}")
print(f"Part two: {powersum}")
