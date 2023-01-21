import collections

import fileHandle, copy, itertools
from collections import deque


def parse_input(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    plot = deque(deque(line) for line in data)
    return plot


class Grove:
    def __init__(self, plot):
        self.plot = plot
        self.elves = set()
        # spread2
        for y in range(len(plot)):
            for x in range(len(plot[0])):
                if self.plot[y][x] == '#':
                    self.elves.add((x, y))
        # spread1
        self.number_of_elves = sum(row.count('#') for row in self.plot)

    turn = 3
    N = [(-1, -1), (0, -1), (1, -1)]
    S = [(-1, 1), (0, 1), (1, 1)]
    W = [(-1, -1), (-1, 0), (-1, 1)]
    E = [(1, -1), (1, 0), (1, 1)]
    directions = [N, S, W, E]

    def draw_plot(self, plot=None):
        if plot is None:
            plot = self.plot
        for row in plot:
            print(*row, sep='')

    def expand_plot(self):
        if '#' in self.plot[0]:
            self.plot.appendleft(deque('.' * len(self.plot[0])), )
        if '#' in self.plot[-1]:
            self.plot.append(deque('.' * len(self.plot[0])), )
        if '#' in [row[0] for row in self.plot]:
            for row in self.plot:
                row.appendleft('.')
        if '#' in [row[-1] for row in self.plot]:
            for row in self.plot:
                row.append('.')

    def isolated(self, x, y):
        for vx, vy in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if (vx, vy) != (0, 0) and self.plot[y + vy][x + vx] == '#':
                return False
        return True

    def aim(self, x, y):
        for dr in [(i + self.turn) % 4 for i in range(4)]:
            for vx, vy in Grove.directions[dr]:
                if self.plot[y + vy][x + vx] == '#':
                    break
            else:
                vx, vy = Grove.directions[dr][1]
                return x + vx, y + vy
        return x, y

    def spread(self):
        self.turn = (self.turn + 1) % 4
        self.expand_plot()
        new_plot = copy.deepcopy(self.plot)
        for y in range(len(self.plot)):
            for x in range(len(self.plot[0])):
                if self.plot[y][x] != '#' or self.isolated(x, y):
                    continue
                ax, ay = self.aim(x, y)
                if (ax, ay) == (x, y):
                    continue
                if new_plot[ay][ax] == '.':
                    new_plot[y][x] = '.'
                    new_plot[ay][ax] = f'{x}-{y}'
                elif new_plot[ay][ax] not in ['.', '#', '!']:
                    xx, yy = new_plot[ay][ax].split('-')
                    new_plot[int(yy)][int(xx)] = '#'
                    new_plot[ay][ax] = '!'
        has_moved = False
        for y in range(len(new_plot)):
            for x in range(len(new_plot[0])):
                if new_plot[y][x] == '!':
                    new_plot[y][x] = '.'
                elif new_plot[y][x] not in ['.', '!', '#']:
                    new_plot[y][x] = '#'
                    has_moved = True
        self.plot = new_plot
        return has_moved

    def isolated2(self, x, y):
        for vx, vy in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if (vx, vy) != (0, 0) and (x + vx, y + vy) in self.elves:
                return False
        return True

    def aim2(self, x, y):
        for i in range(4):
            dr = (i + self.turn) % 4
            for vx, vy in Grove.directions[dr]:
                if (x + vx, y + vy) in self.elves:
                    break
            else:
                vx, vy = Grove.directions[dr][1]
                return x + vx, y + vy
        return x, y

    def spread2(self):
        self.turn = (self.turn + 1) % 4
        positions = collections.defaultdict([1])
        for x, y in self.elves:
            if self.isolated2(x, y) or self.aim2(x, y) == (x, y):
                positions[(x, y)].append((x, y))
                continue
            positions[self.aim2(x, y)].append((x, y))
        print(positions)
        has_moved = False
        self.elves.clear()
        for pos in positions:
            self.elves.add(pos)
            has_moved = True
        return has_moved


def puzzle45b(input_file):
    plot = parse_input(input_file)
    grove = Grove(plot)
    print(grove.elves)
    grove.spread2()
    print(grove.elves)


def puzzle45(input_file):
    plot = parse_input(input_file)
    grove = Grove(plot)
    for _ in range(10):
        grove.spread()
    height = len(grove.plot) - ('#' not in grove.plot[0]) - ('#' not in grove.plot[-1])
    width = len(grove.plot[0]) - ('#' not in [row[0] for row in grove.plot]) \
            - ('#' not in [row[-1] for row in grove.plot])
    area = width * height
    return area - grove.number_of_elves


def puzzle46(input_file):
    plot = parse_input(input_file)
    grove = Grove(plot)
    rnd = 1
    while grove.spread():
        rnd += 1
    return rnd


print('Day #23 Part One:', puzzle45b('input.txt'))
# print('Day #23 Part Two:', puzzle46('day23.txt'))
