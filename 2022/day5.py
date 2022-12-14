import fileHandle, re


def get_stack(stacks_data):
    lines = stacks_data.splitlines()
    n_stacks = len(lines[0]) // 4 + 1
    stacks = [[] for i in range(n_stacks + 1)]
    for l in range(len(lines) - 2, -1, -1):
        for i in range(1, n_stacks + 1):
            if lines[l][4 * i - 3] != ' ':
                stacks[i].append(lines[l][4 * i - 3])
    return stacks


def puzzle9(input_file):
    data = fileHandle.readfile(input_file, strip=False).split('\n\n')
    stacks = get_stack(data[0])
    commands = data[1].splitlines()
    for i in range(len(commands)):
        cmd = re.split(r'move | from | to ', commands[i])
        number, origin, destination = int(cmd[1]), int(cmd[2]), int(cmd[3])
        for j in range(number):
            stacks[destination].append(stacks[origin].pop())
    tops = ''
    for i in range(1, len(stacks)):
        tops += stacks[i][-1]
    return tops


def puzzle10(input_file):
    data = fileHandle.readfile(input_file, strip=False).split('\n\n')
    stacks = get_stack(data[0])
    commands = data[1].splitlines()
    for i in range(len(commands)):
        cmd = re.split(r'move | from | to ', commands[i])
        number, origin, destination = int(cmd[1]), int(cmd[2]), int(cmd[3])
        stacks[destination] += stacks[origin][-number:]
        stacks[origin] = stacks[origin][:-number]
    tops = ''
    for i in range(1, len(stacks)):
        tops += stacks[i][-1]
    return tops


print('Day #5, Part One:', puzzle9('day5.txt'))
print('Day #5, Part Two:', puzzle10('day5.txt'))
