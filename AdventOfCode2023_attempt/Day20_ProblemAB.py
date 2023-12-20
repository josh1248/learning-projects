day_number = 20
import collections
import math
def main():
    low_pulse, high_pulse = 0, 1 #treat as binaries
    modules = {}
    for line in read_file():
        name, tmp = line.strip().split(" -> ")
        outputs = tmp.split(", ")
        if name[0] == "%":
            modules[name[1:]] = {"type": "flipflop", "state": low_pulse, "outputs": outputs}
        elif name[0] == "&":
            modules[name[1:]] = {"type": "conjunction", "inputs": {}, "outputs": outputs}
        else:
            modules[name] = {"type": "broadcaster", "outputs": outputs}
    
    #find inputs of conjunction modules
    for key, value in modules.items():
        for output in value["outputs"]:
            try:
                if modules[output]["type"] == "conjunction":
                    modules[output]["inputs"][key] = low_pulse
            except KeyError:
                pass


    #Part 2: works because a single conjunction module, itself linked to conjunction modules only, connects to rx
    rx_conjunction_module = "hj" #i am the input processing
    terminals = {k: [] for k in modules[rx_conjunction_module]["inputs"]}

    def press_button(i):
        low_pulses, high_pulses = 0, 0
        queue = collections.deque([("broadcaster", low_pulse, "button")])
        while queue:
            target_name, pulse_type, origin = queue.popleft()
            if pulse_type == high_pulse: high_pulses += 1
            else: low_pulses += 1

            if target_name not in modules: #target is the rx module
                continue

            target = modules[target_name]
            if target["type"] == "broadcaster":
                pulse_to_send = pulse_type
            elif target["type"] == "flipflop":
                if pulse_type == high_pulse:
                    continue #do not send a pulse, skip last line
                else:
                    target["state"] = not target["state"]
                    pulse_to_send = target["state"]
            else: #conjunction module
                target["inputs"][origin] = pulse_type
                pulse_to_send = low_pulse if all(target["inputs"].values()) else high_pulse
                #Part 2 junk
                if target_name in terminals and pulse_to_send == high_pulse:
                        terminals[target_name].append(i)

            queue.extend([(output, pulse_to_send, target_name) for output in target["outputs"]])
        return (low_pulses, high_pulses)
    
    total_low, total_high = 0, 0
    for i in range(1, 1001):
        l, h = press_button(i)
        total_low += l
        total_high += h

    print("Part 1:", total_low * total_high)

    for i in range(1001, 5001): #enough to find a high pulse from the all modules connecting to terminal conjunction module
        press_button(i)
    print("Part 2:", math.lcm(*(v[0] for v in terminals.values())))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()