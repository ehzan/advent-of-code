import fileHandle, bisect


def parse_input(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    weather_map = [row[1:-1] for row in data[1:-1]]
    return weather_map


class Plat:
    def __init__(self, weather_map):
        self.blizzards = Plat.extract_blizzards(weather_map)
        self.width = len(weather_map[0])
        self.length = len(weather_map)
        self.entrance = (0, -1)
        self.exit = (self.width - 1, self.length)

    @staticmethod
    def extract_blizzards(weather_map):
        vectors = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}
        blizzards = {(1, 0): [], (-1, 0): [], (0, 1): [], (0, -1): []}
        for y in range(len(weather_map)):
            for x in range(len(weather_map[0])):
                if weather_map[y][x] != '.':
                    v = vectors[weather_map[y][x]]
                    blizzards[v].append([x, y])
        return blizzards

    @property
    def blizzards_list(self):
        l = [coord for lst in self.blizzards.values() for coord in lst]
        l.sort()
        return l

    @staticmethod
    def has(list, item):
        # _has=item in list
        _has = bisect.bisect_left(list, item) != bisect.bisect_right(list, item)
        return _has

    def draw_map(self):
        wmap = [['#'] * (self.width + 2)]
        wmap += [['#'] + ['.'] * self.width + ['#'] for _ in range(self.length)]
        wmap += [['#'] * (self.width + 2)]
        wmap[self.entrance[1] + 1][self.entrance[0] + 1] = '.'
        wmap[self.exit[1] + 1][self.exit[0] + 1] = '.'
        for b in self.blizzards[(1, 0)]:
            wmap[b[1] + 1][b[0] + 1] = '>'
        for b in self.blizzards[(-1, 0)]:
            wmap[b[1] + 1][b[0] + 1] = '<'
        for b in self.blizzards[(0, 1)]:
            wmap[b[1] + 1][b[0] + 1] = 'v'
        for b in self.blizzards[(0, -1)]:
            wmap[b[1] + 1][b[0] + 1] = '^'
        for row in wmap:
            print(*row, sep='')
        print()

    def blow(self):
        for vector, coordinates_list in self.blizzards.items():
            for coord in coordinates_list:
                coord[0] = (coord[0] + vector[0]) % self.width
                coord[1] = (coord[1] + vector[1]) % self.length

    def shortest_time(self, start, goal):
        pos = [{start}]
        for step in range(1, 1000):
            self.blow()
            blz = self.blizzards_list
            pos.append(set())
            for x, y in pos[step - 1]:
                if (x, y + 1) == goal or (x, y - 1) == goal:
                    return step
                if not self.has(blz, [x, y]):
                    pos[step].add((x, y))
                if y < self.length - 1 and not self.has(blz, [x, y + 1]):
                    pos[step].add((x, y + 1))
                if y > 0 and not self.has(blz, [x, y - 1]):
                    pos[step].add((x, y - 1))
                if y == -1 or y == self.length:
                    continue
                if x < self.width - 1 and not self.has(blz, [x + 1, y]):
                    pos[step].add((x + 1, y))
                if x > 0 and not self.has(blz, [x - 1, y]):
                    pos[step].add((x - 1, y))


def puzzle47(input_file):
    weather_map = parse_input(input_file)
    valley = Plat(weather_map)
    steps = valley.shortest_time(valley.entrance, valley.exit)
    return steps


def puzzle48(input_file):
    weather_map = parse_input(input_file)
    valley = Plat(weather_map)
    steps1 = valley.shortest_time(valley.entrance, valley.exit)
    steps2 = valley.shortest_time(valley.exit, valley.entrance)
    steps3 = valley.shortest_time(valley.entrance, valley.exit)
    return steps1 + steps2 + steps3


import timeit

code = "print('Day #24 Part One:', puzzle47('day24.txt'))"
t = timeit.timeit(stmt=code, globals=globals(), number=1)
print(t)
code = "print('Day #24 Part Two:', puzzle48('day24.txt'))"
t = timeit.timeit(stmt=code, globals=globals(), number=1)
print(t)
