import fileHandle
import itertools


def derive_plot(dots):
    max_x, max_y = 0, 0
    for dot in dots:
        max_x = max(max_x, int(dot[0]))
        max_y = max(max_y, int(dot[1]))
    plot = [[0] * (max_y + 1) for i in range(max_x + 1)]
    for dot in dots:
        plot[int(dot[0])][int(dot[1])] = 1
    return plot


def fold(command, plot):
    axis = command[0]
    offset = int(command[2:])
    if axis == 'x':
        for x in range(offset + 1, len(plot)):
            for y in range(len(plot[0])):
                plot[offset - (x - offset)][y] += plot[x][y]
        plot = plot[:offset]
    elif axis == 'y':
        for x in range(len(plot)):
            for y in range(offset + 1, len(plot[x])):
                plot[x][offset - (y - offset)] += plot[x][y]
            plot[x] = plot[x][:offset]
    return plot


def draw(plot):
    for y in range(len(plot[0])):
        for x in range(len(plot)):
            ch = '##' if plot[x][y] > 0 else '  '
            print(ch, end='')
        print()


def puzzle25(input_file='day13.txt'):
    data = fileHandle.readfile(input_file).split('\n\n')
    dots = [line.split(',') for line in data[0].split('\n')]
    plot = derive_plot(dots)
    command1 = data[1].split('\n')[0].split(' ')[2]
    plot = fold(command1, plot)
    cnt = 0
    for x, y in itertools.product(range(len(plot)), range(len(plot[0])), ):
        cnt += plot[x][y] > 0
    return cnt


def puzzle26(input_file='day13.txt'):
    data = fileHandle.readfile(input_file).split('\n\n')
    dots = [line.split(',') for line in data[0].split('\n')]
    plot = derive_plot(dots)
    for line in data[1].split('\n'):
        command = line.split(' ')[2]
        plot = fold(command, plot)
    draw(plot)
    return 'PGHRKLKL'
