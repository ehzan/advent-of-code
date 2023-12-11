import bisect
import itertools

import file_handle


def parse_input(data: str) -> tuple[set, list, list]:
    grid = [list(row) for row in data.splitlines()]
    width, height = len(grid), len(grid[0])

    galaxies = {(x, y) for x in range(width) for y in range(height) if grid[y][x] == '#'}
    empty_rows = [y for y, row in enumerate(grid) if '#' not in row]
    empty_cols = [x for x, col in enumerate(zip(*grid)) if '#' not in col]

    return galaxies, empty_rows, empty_cols


def distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int],
             empty_rows: list[int], empty_cols: list[int], expansion: int) -> int:
    (x1, y1), (x2, y2) = (galaxy1, galaxy2)
    xd = abs(x2 - x1) + (expansion - 1) * abs(bisect.bisect_left(empty_cols, x2) - bisect.bisect_left(empty_cols, x1))
    yd = abs(y2 - y1) + (expansion - 1) * abs(bisect.bisect_left(empty_rows, y2) - bisect.bisect_left(empty_rows, y1))

    return xd + yd


def puzzle21(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    galaxies, empty_rows, empty_cols = parse_input(data)

    return sum(distance(galaxy1, galaxy2, empty_rows, empty_cols, 2)
               for (galaxy1, galaxy2) in itertools.combinations(galaxies, 2))


def puzzle22(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    galaxies, empty_rows, empty_cols = parse_input(data)

    return sum(distance(galaxy1, galaxy2, empty_rows, empty_cols, 1000000)
               for (galaxy1, galaxy2) in itertools.combinations(galaxies, 2))


if __name__ == '__main__':
    print('Day #11, part one:', puzzle21('./input/day11.txt'))
    print('Day #11, part two:', puzzle22('./input/day11.txt'))
