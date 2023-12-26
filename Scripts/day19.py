from copy import deepcopy

file = open("Data/day19.txt", "r")

workflows = {}

for line in file:
    
    if line == "\n":
        break

    line = line.strip().split("{")
    line[1] = line[1][:-1].split(",")

    for i in range(len(line[1])):
        
        if line[1][i] == "A":
            line[1][i] = 1

        elif line[1][i] == "R":
            line[1][i] = 0

        elif "<" in line[1][i]:
            line[1][i] = line[1][i].split("<")
            line[1][i][1] = line[1][i][1].split(":")
            line[1][i] = [line[1][i][0], 0, int(line[1][i][1][0]), line[1][i][1][1]]

            if line[1][i][3] == "A":
                line[1][i][3] = 1
            elif line[1][i][3] == "R":
                line[1][i][3] = 0
        
        elif ">" in line[1][i]:
            line[1][i] = line[1][i].split(">")
            line[1][i][1] = line[1][i][1].split(":")
            line[1][i] = [line[1][i][0], 1, int(line[1][i][1][0]), line[1][i][1][1]]

            if line[1][i][3] == "A":
                line[1][i][3] = 1
            elif line[1][i][3] == "R":
                line[1][i][3] = 0
    
    workflows[line[0]] = line[1]

parts = []

for line in file:
    line = line.replace("=", ":").replace("x", "\"x\"").replace("m", "\"m\"").replace("a", "\"a\"").replace("s", "\"s\"")
    line = eval(line)
    parts.append(line)

def process_part(part, workflow):
    
    for i in range(len(workflow)):

        if type(workflow[i]) == int:
            return workflow[i]
        
        elif type(workflow[i]) == str:
            return process_part(part, workflows[workflow[i]])
        
        elif workflow[i][1] == 0:
            if part[workflow[i][0]] < workflow[i][2]:
                if type(workflow[i][3]) == int:
                    return workflow[i][3]
                return process_part(part, workflows[workflow[i][3]])
            continue

        else:
            if part[workflow[i][0]] > workflow[i][2]:
                if type(workflow[i][3]) == int:
                    return workflow[i][3]
                return process_part(part, workflows[workflow[i][3]])
            continue

total = 0

for part in parts:
    if process_part(part, workflows["in"]) == 1:
        total += sum(part.values())

print(f"Part one: {total}")

def process_part_ranges(part, workflow):

    if type(workflow) == int:
        if workflow == 0:
            return 0
        return ((part["x"][1] - part["x"][0] + 1) * (part["m"][1] - part["m"][0] + 1) *
                (part["a"][1] - part["a"][0] + 1) * (part["s"][1] - part["s"][0] + 1))
    
    if type(workflow) == str:
        workflow = workflows[workflow]
    
    for i in range(len(workflow)):

        if type(workflow[i]) == int:
            return process_part_ranges(part, workflow[i])
        
        elif type(workflow[i]) == str:
            return process_part_ranges(part, workflow[i])
        
        elif workflow[i][1] == 0:

            if part[workflow[i][0]][0] >= workflow[i][2]:
                continue
            
            elif part[workflow[i][0]][1] < workflow[i][2]:
                return process_part_ranges(part, workflow[i][3])
            
            else:
                part_a = deepcopy(part)
                part_b = deepcopy(part)

                part_a[workflow[i][0]][1] = workflow[i][2] - 1
                part_b[workflow[i][0]][0] = workflow[i][2]

                return process_part_ranges(part_a, workflow[i][3]) + process_part_ranges(part_b, workflow[i+1:])

        else:
            
            if part[workflow[i][0]][1] <= workflow[i][2]:
                continue
            
            elif part[workflow[i][0]][0] > workflow[i][2]:
                return process_part_ranges(part, workflow[i][3])
            
            else:
                part_a = deepcopy(part)
                part_b = deepcopy(part)

                part_a[workflow[i][0]][0] = workflow[i][2] + 1
                part_b[workflow[i][0]][1] = workflow[i][2]

                return process_part_ranges(part_a, workflow[i][3]) + process_part_ranges(part_b, workflow[i+1:])

print(f"Part two: {process_part_ranges({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in')}")
