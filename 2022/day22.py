import enum
import re

import file_handle


def parse_input(data: str) -> tuple[list, list]:
    data = data.split('\n\n')
    mapp = data[0].splitlines()
    path = [(int(segment[:-1]), segment[-1])
            for segment in re.findall(r'\d+[RL\n]?', data[1])]

    return mapp, path


class Dir(enum.Enum):
    RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3


class Tour:
    def __init__(self, mapp: list[str],
                 starting_position: tuple[int, int],
                 direction: Dir):
        self._map = mapp
        self._curr = starting_position
        self._dir = direction

    DIRECTION = {Dir.RIGHT: (1, 0), Dir.LEFT: (-1, 0),
                 Dir.UP: (0, -1), Dir.DOWN: (0, 1), }

    FACE = {(1, 0): 'A', (2, 0): 'B',
            (1, 1): 'C',
            (0, 2): 'D', (1, 2): 'E',
            (0, 3): 'F', }

    @property
    def password(self) -> int:
        return 1000 * (self._curr[1] + 1) + 4 * (self._curr[0] + 1) + self._dir.value

    def turn(self, turn_to: str):
        self._dir = Dir((self._dir.value + (turn_to == 'R') - (turn_to == 'L')) % 4)

    def next1(self) -> tuple[int, int]:
        (x, y) = self._curr
        (dx, dy) = Tour.DIRECTION[self._dir]
        (x, y) = (x + dx, y + dy)

        if 0 <= y < len(self._map) and 0 <= x < len(self._map[y]) \
                and self._map[y][x] != ' ':
            return x, y

        match self._dir:
            case Dir.RIGHT:
                x = self._map[y].rfind(' ') + 1
            case Dir.LEFT:
                x = len(self._map[y]) - 1
            case Dir.DOWN:
                y = next(yi for yi in range(len(self._map)) if self._map[yi][x] != ' ')
            case Dir.UP:
                y = next(yi for yi in range(len(self._map) - 1, -1, -1) if x < len(self._map[yi]))

        return x, y

    def walk1(self, length: int, turn_to: str):
        for _ in range(length):
            (x, y) = self.next1()
            if self._map[y][x] == '#':
                break
            else:
                self._curr = (x, y)
        self.turn(turn_to)

    def next2(self) -> tuple[tuple, Dir]:
        new_dir = self._dir
        (x, y) = self._curr
        current_page = Tour.FACE[(x // 50, y // 50)]
        (dx, dy) = Tour.DIRECTION[self._dir]
        (x, y) = (x + dx, y + dy)

        if (x // 50, y // 50) not in Tour.FACE:
            (x, y), new_dir = self.turn_over(current_page, x, y)

        return (x, y), new_dir

    @staticmethod
    def turn_over(face: str, x: int, y: int) -> tuple[tuple, Dir]:
        match face, x, y:
            case 'A', 49, _:
                return (0, 149 - y), Dir.RIGHT
            case 'A', _, -1:
                return (0, x + 100), Dir.RIGHT
            case 'B', 150, _:
                return (99, 149 - y), Dir.LEFT
            case 'B', _, -1:
                return (x - 100, 199), Dir.UP
            case 'B', _, 50:
                return (99, x - 50), Dir.LEFT
            case 'C', 49, _:
                return (y - 50, 100), Dir.DOWN
            case 'C', 100, _:
                return (y + 50, 49), Dir.UP
            case 'D', -1, _:
                return (50, 149 - y), Dir.RIGHT
            case 'D', _, 99:
                return (50, x + 50), Dir.RIGHT
            case 'E', 100, _:
                return (149, 149 - y), Dir.LEFT
            case 'E', _, 150:
                return (49, 100 + x), Dir.LEFT
            case 'F', -1, _:
                return (y - 100, 0), Dir.DOWN
            case 'F', 50, _:
                return (y - 100, 149), Dir.UP
            case 'F', _, 200:
                return (x + 100, 0), Dir.DOWN

    def walk2(self, length: int, turn_to: str):
        for _ in range(length):
            (x, y), new_dir = self.next2()
            assert self._map[y][x] in ['.', '#']
            if self._map[y][x] == '#':
                break
            else:
                self._curr = (x, y)
                self._dir = new_dir
        self.turn(turn_to)


def puzzle43(input_file: str) -> int:
    data = file_handle.readfile(input_file)
    mapp, path = parse_input(data)

    starting_position = (mapp[0].index('.'), 0)
    tour = Tour(mapp, starting_position, Dir.RIGHT)
    for length, turn_to in path:
        tour.walk1(length, turn_to)

    return tour.password


def puzzle44(input_file: str) -> int:
    data = file_handle.readfile(input_file)
    mapp, path = parse_input(data)

    starting_position = (mapp[0].index('.'), 0)
    tour = Tour(mapp, starting_position, Dir.RIGHT)
    for length, turn_to in path:
        tour.walk2(length, turn_to)

    return tour.password


if __name__ == '__main__':
    print('Day #22, part one:', puzzle43('./input/day22.txt'))
    print('Day #22, part two:', puzzle44('./input/day22.txt'))
