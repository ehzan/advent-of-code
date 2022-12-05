from fileHandle import readfile
import re


def puzzle9(input_file='day5.txt'):
    data = readfile(input_file).split('\n\n')
    stacks = data[0].split('\n')
    n_stacks = len(stacks[0]) // 4 + 1
    stack = [[] for i in range(0, n_stacks + 1)]
    for line in range(len(stacks) - 2, -1, -1):
        for i in range(1, n_stacks + 1):
            if stacks[line][4 * i - 3] != ' ':
                stack[i].append(stacks[line][4 * i - 3])
    # print(*stack)
    commands = data[1].split('\n')
    for line in range(0, len(commands)):
        cmd = re.split(r'move | from | to ', commands[line])
        number, origin, destination = int(cmd[1]), int(cmd[2]), int(cmd[3])
        for i in range(number):
            stack[destination].append(stack[origin].pop())
    tops = ''
    for i in range(1, n_stacks + 1):
        tops += stack[i][-1]
    return tops


def puzzle10(input_file='day5.txt'):
    data = readfile(input_file).split('\n\n')
    stacks = data[0].split('\n')
    n_stacks = len(stacks[0]) // 4 + 1
    stack = [[] for i in range(0, n_stacks + 1)]
    for line in range(len(stacks) - 2, -1, -1):
        for i in range(1, n_stacks + 1):
            if stacks[line][4 * i - 3] != ' ':
                stack[i].append(stacks[line][4 * i - 3])
    # print(*stack)
    commands = data[1].split('\n')
    for line in range(0, len(commands)):
        cmd = re.split(r'move | from | to ', commands[line])
        number, origin, destination = int(cmd[1]), int(cmd[2]), int(cmd[3])
        stack[destination] += stack[origin][-number:]
        stack[origin] = stack[origin][:-number]
    tops = ''
    for i in range(1, n_stacks + 1):
        tops += stack[i][-1]
    return tops
