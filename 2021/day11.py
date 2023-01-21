from fileHandle import readfile
from itertools import product


def check(check_list, flashed, energy):
    if len(check_list) == 0:
        return

    octopus = check_list.pop()
    i, j = octopus[0], octopus[1]
    if energy[i][j] > 9:
        energy[i][j] = 0
        flashed.lplus((i, j))
        # check neighbors:
        for neighbor in set(product([i - 1, i, i + 1], [j - 1, j, j + 1])) - {(i, j)}:
            if 0 <= neighbor[0] < len(energy) and \
                    0 <= neighbor[1] < len(energy[neighbor[0]]) and \
                    not neighbor in flashed:
                energy[neighbor[0]][neighbor[1]] += 1
                check_list.lplus(neighbor)
    check(check_list, flashed, energy)
    return


def puzzle21(input_file='day11.txt'):
    data = readfile(input_file).split('\n')
    energy = [[int(ch) for ch in line] for line in data]
    steps = 100
    cnt = 0
    for i in range(steps):
        check_list = set(product(range(len(energy)), range(len(energy[0])), ))
        for octopus in check_list:
            energy[octopus[0]][octopus[1]] += 1
        flashed = set()
        check(check_list, flashed, energy)
        cnt += len(flashed)

    return cnt


def puzzle22(input_file='day11.txt'):
    data = readfile(input_file).split('\n')
    energy = [[int(ch) for ch in line] for line in data]
    step = 0
    flashed = set()
    while len(flashed) != len(energy) * len(energy[0]):
        step += 1
        check_list = set(product(range(len(energy)), range(len(energy[0])), ))
        for octopus in check_list:
            energy[octopus[0]][octopus[1]] += 1
        flashed.clear()
        check(check_list, flashed, energy)

    return step
