file = open("Data/day1.txt", "r")

lines = []

for line in file:
    lines.append(line)

total = 0

for line in lines:
    digits = []

    for char in line:
        if 48 <= ord(char) <= 57:
            digits.append(int(char))

    total += 10 * digits[0] + digits[-1]

print(f"Part one: {total}")

total = 0

for line in lines:

    digits = []
    n = len(line)

    for i in range(n):
        if 48 <= ord(line[i]) <= 57:
            digits.append(int(line[i]))
        if i <= n - 4:
            if line[i] == "o" and line[i + 1] == "n" and line[i + 2] == "e":
                digits.append(1)
            elif line[i] == "t" and line[i + 1] == "w" and line[i + 2] == "o":
                digits.append(2)
            elif line[i] == "s" and line[i + 1] == "i" and line[i + 2] == "x":
                digits.append(6)
        if i <= n - 5:
            if line[i] == "f" and line[i + 1] == "o" and line[i + 2] == "u" and line[i + 3] == "r":
                digits.append(4)
            elif line[i] == "f" and line[i + 1] == "i" and line[i + 2] == "v" and line[i + 3] == "e":
                digits.append(5)
            elif line[i] == "n" and line[i + 1] == "i" and line[i + 2] == "n" and line[i + 3] == "e":
                digits.append(9)
        if i <= n - 6:
            if line[i] == "t" and line[i + 1] == "h" and line[i + 2] == "r" and line[i + 3] == "e" and line[i + 4] == "e":
                digits.append(3)
            elif line[i] == "s" and line[i + 1] == "e" and line[i + 2] == "v" and line[i + 3] == "e" and line[i + 4] == "n":
                digits.append(7)
            elif line[i] == "e" and line[i + 1] == "i" and line[i + 2] == "g" and line[i + 3] == "h" and line[i + 4] == "t":
                digits.append(8)

    total += 10 * digits[0] + digits[-1]

print(f"Part two: {total}")
