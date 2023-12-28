file = open("Data/day20.txt", "r")

modules = {}

# Read modules and connections from file
for line in file:
    line = line.replace(",", "").split()
    
    # Broadcast module
    if line[0] == "broadcaster":
        modules[line[0]] = {"type": "broadcast", "dest": line[2:]}
    
    # Flip flop modules
    elif line[0].startswith("%"):
        modules[line[0][1:]] = {"type": "flipflop", "state": 0, "dest": line[2:]}
    
    # Conjunction modules
    elif line[0].startswith("&"):
        modules[line[0][1:]] = {"type": "conj", "dest": line[2:], "state": {}}

# Add output modules and find conjunction input modules
output_modules = []

for module, data in modules.items():
    for dest in data["dest"]:

        if dest not in modules.keys():
            output_modules.append(dest)

        elif modules[dest]["type"] == "conj":
            modules[dest]["state"][module] = 0

for module in output_modules:
    modules[module] = {"type": "output"}

def process_pulse(current_pulse):
    from_module = current_pulse[0]
    to_module = current_pulse[1]
    pulse = current_pulse[2]

    # Broadcast module
    if modules[to_module]["type"] == "broadcast":
        return [(to_module, dest, pulse) for dest in modules[to_module]["dest"]]

    # Flip flop module
    if modules[to_module]["type"] == "flipflop":
        if pulse == 1:
            return []
        modules[to_module]["state"] = 1 - modules[to_module]["state"]
        return [(to_module, dest, modules[to_module]["state"]) for dest in modules[to_module]["dest"]]
    
    # Conjunction module
    if modules[to_module]["type"] == "conj":
        modules[to_module]["state"][from_module] = pulse
        if 0 in modules[to_module]["state"].values():
            return [(to_module, dest, 1) for dest in modules[to_module]["dest"]]
        return [(to_module, dest, 0) for dest in modules[to_module]["dest"]]
    
    # Output module
    return []

# Get input modules for final conjunction module before output "rx"
for module in modules:
    if "rx" in modules[module]["dest"]:
        break

min_presses = {}

for input_module in modules[module]["state"].keys():
    min_presses[input_module] = 1e6

# Run simulation
pulse_count = [0, 0]
button_presses = 0

while True:
    button_presses += 1
    to_process = [("button", "broadcaster", 0)]

    while to_process:
        current_pulse = to_process.pop(0)

        if current_pulse[0] in min_presses.keys() and current_pulse[2] == 1:
            min_presses[current_pulse[0]] = min(button_presses, min_presses[current_pulse[0]])

        if button_presses <= 1000:
            pulse_count[current_pulse[2]] += 1

        to_process += process_pulse(current_pulse)
    
    if max(min_presses.values()) < 1e6:
        break

print(f"Part one: {pulse_count[0] * pulse_count[1]}")

press_prod = 1
for value in min_presses.values():
    press_prod *= value

print(f"Part two: {press_prod}")
