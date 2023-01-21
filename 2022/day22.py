import fileHandle, re


def parse_input(input_file):
    data = fileHandle.readfile(input_file, strip=False).split('\n\n')
    mapp = data[0].splitlines()
    path = re.findall(r'^\d+|[A-Z]\d+', data[1])
    return mapp, path


class Tour:
    def __init__(self, _map, cur, dir):
        self.map = _map
        self.cur = cur
        self.cur1 = cur
        self.dir = dir

    _vector = {'right': (1, 0), 'left': (-1, 0), 'up': (0, -1), 'down': (0, 1)}
    _WIDTH = 50
    _faces = [(1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (0, 3)]

    def _next(self, x=None, y=None):
        Vx, Vy = self._vector[self.dir]
        x = self.cur[0] if x is None else x
        y = self.cur[1] if y is None else y
        return x + Vx, y + Vy

    def _face(self, pos):
        a = pos[0] // self._WIDTH
        b = pos[1] // self._WIDTH
        if (a, b) in self._faces:
            return 'ABCDEF'[self._faces.index((a, b))]  # A,B,C,...
        else:
            return None

    def turn(self, turn_direction):
        turn_right = {'right': 'down', 'left': 'up', 'up': 'right', 'down': 'left'}
        turn_left = {'right': 'up', 'left': 'down', 'up': 'left', 'down': 'right'}
        self.dir = turn_right[self.dir] if turn_direction == 'R' else turn_left[self.dir]

    def walk1(self, turn_direction, length):
        self.turn(turn_direction)
        for _ in range(length):
            x, y = self.cur
            while True:
                x, y = self._next(x, y)
                y = y % len(self.map)
                x = x % len(self.map[0])
                if x < len(self.map[y]) and self.map[y][x] != ' ':
                    break
            assert self.map[y][x] in ['.', '#']
            if self.map[y][x] == '.':
                self.cur = (x, y)
            else:
                break

    @staticmethod
    def turn_over(face, x, y):
        if face == 'A' and y == -1:
            y = x + 100
            x = 0
            new_dir = 'right'
        elif face == 'F' and x == -1:
            x = y - 100
            y = 0
            new_dir = 'down'
        elif face == 'A' and x == 49:
            y = 149 - y
            x = 0
            new_dir = 'right'
        elif face == 'D' and x == -1:
            y = 149 - y
            x = 50
            new_dir = 'right'
        elif face == 'B' and y == -1:
            x = x - 100
            y = 199
            new_dir = 'up'
        elif face == 'F' and y == 200:
            x = x + 100
            y = 0
            new_dir = 'down'
        elif face == 'B' and x == 150:
            y = 149 - y
            x = 99
            new_dir = 'left'
        elif face == 'E' and x == 100:
            y = 149 - y
            x = 149
            new_dir = 'left'
        elif face == 'B' and y == 50:
            y = x - 50
            x = 99
            new_dir = 'left'
        elif face == 'C' and x == 100:
            x = y + 50
            y = 49
            new_dir = 'up'
        elif face == 'C' and x == 49:
            x = y - 50
            y = 100
            new_dir = 'down'
        elif face == 'D' and y == 99:
            y = x + 50
            x = 50
            new_dir = 'right'
        elif face == 'E' and y == 150:
            y = 100 + x
            x = 49
            new_dir = 'left'
        elif face == 'F' and x == 50:
            x = y - 100
            y = 149
            new_dir = 'up'
        return x, y, new_dir

    def walk2(self, turn_direction, length):
        self.turn(turn_direction)
        for _ in range(length):
            x, y = self._next()
            new_dir = self.dir
            if self._face((x, y)) is None:
                x, y, new_dir = self.turn_over(self._face(self.cur), x, y)
            assert self.map[y][x] in ['.', '#']
            if self.map[y][x] == '.':
                self.cur = (x, y)
                self.dir = new_dir
            else:
                break


def puzzle43(input_file):
    mapp, path = parse_input(input_file)
    cur = (mapp[0].index('.'), 0)
    tour = Tour(mapp, cur, 'up')
    path[0] = 'R' + path[0]
    for w in path:
        tour.walk1(w[0], int(w[1:]), )
    password = 1000 * (tour.cur[1] + 1) + 4 * (tour.cur[0] + 1)
    password += 0 if tour.dir == 'right' else 1 if tour.dir == 'down' else 2 if tour.dir == 'left' else 3
    return tour.cur, password


def puzzle44(input_file):
    mapp, path = parse_input(input_file)
    cur = (mapp[0].index('.'), 0)
    tour = Tour(mapp, cur, 'up')
    path[0] = 'R' + path[0]
    for w in path:
        tour.walk2(w[0], int(w[1:]), )
    password = 1000 * (tour.cur[1] + 1) + 4 * (tour.cur[0] + 1)
    password += 0 if tour.dir == 'right' else 1 if tour.dir == 'down' else 2 if tour.dir == 'left' else 3
    return tour.cur, password


print('Day #22 Part One:', puzzle43('day22.txt'))
print('Day #22 Part Two:', puzzle44('day22.txt'))
