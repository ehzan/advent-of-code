from fileHandle import *


def puzzle3(input_file='day2.txt'):
    command = readfile(input_file).split('\n')
    position = [0, 0]
    for i in range(len(command)):
        cmd = command[i].split(' ')
        if cmd[0] == 'forward':
            position[0] += int(cmd[1])
        elif cmd[0] == 'up':
            position[1] -= int(cmd[1])
        elif cmd[0] == 'down':
            position[1] += int(cmd[1])
    return position, position[0] * position[1]


def puzzle4(input_file='day2.txt'):
    command = readfile(input_file).split('\n')
    position = [0, 0]
    aim = 0
    for i in range(len(command)):
        cmd = command[i].split(' ')
        if cmd[0] == 'forward':
            position[0] += int(cmd[1])
            position[1] += aim * int(cmd[1])
        elif cmd[0] == 'up':
            aim -= int(cmd[1])
        elif cmd[0] == 'down':
            aim += int(cmd[1])
    return position, position[0] * position[1]
