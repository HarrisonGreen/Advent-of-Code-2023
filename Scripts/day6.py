from numpy import sqrt

file = open("Data/day6.txt", "r")

for i, line in enumerate(file):

    if i == 0:
        times = [int(x) for x in line.split()[1:]]
    else:
        distances = [int(x) for x in line.split()[1:]]

races = {times[i]: distances[i] for i in range(len(times))}
product = 1

for t, d in races.items():
    lower_limit = t/2 - sqrt(t**2 - 4*d)/2
    upper_limit = t/2 + sqrt(t**2 - 4*d)/2

    product *= int(upper_limit) - int(lower_limit)

print(f"Part one: {product}")

time = ""
distance = ""

for i in range(len(times)):
    time = time + str(times[i])
    distance = distance + str(distances[i])

time = int(time)
distance = int(distance)

print(f"Part two: {int(time/2 + sqrt(time**2 - 4*distance)/2) - int(time/2 - sqrt(time**2 - 4*distance)/2)}")
