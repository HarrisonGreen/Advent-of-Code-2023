file = open("Data/day3.txt", "r")

part_numbers = {}
gears = {}
symbols = []

for j, line in enumerate(file):
    finish = 0
    line = line.strip("\n")

    for i in range(len(line)):

        if i < finish:
            continue

        if line[i] == ".":
            pass

        elif 48 <= ord(line[i]) <= 57:
            digits = line[i]
            k = 1

            while i+k < len(line) and 48 <= ord(line[i+k]) <= 57:
                digits = digits + line[i+k]
                k += 1
                finish = i+k
            
            part_numbers[(j, i)] = int(digits)
        
        elif line[i] == "*":
            gears[(j, i)] = []
        
        else:
            symbols.append((j, i))

total = 0

for pos, number in part_numbers.items():
    left = pos[1] - 1
    right = pos[1] + len(str(number))
    top = pos[0] - 1
    bottom = pos[0] + 1

    adjacent = False

    for x in range(left, right + 1):
        for y in range(top, bottom + 1):

            if (y, x) in gears:
                adjacent = True
                gears[(y,x)].append(number)

            elif (y, x) in symbols:
                adjacent = True
        
    if adjacent:
        total += number

print(f"Part one: {total}")

gear_sum = 0

for key, value in gears.items():
    if len(value) == 2:
        gear_sum += value[0] * value[1]

print(f"Part two: {gear_sum}")
