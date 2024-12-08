import itertools
from collections import defaultdict

import file_handle


def extract_antennas(grid: list[str]) -> dict[str, set[tuple[int, int]]]:
    antennas = defaultdict(lambda: set())
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                antennas[grid[y][x]].add((x, y))

    return antennas


def puzzle15(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()
    n = len(grid)
    assert n == len(grid[0])

    antinode_locations = set()
    for cords in extract_antennas(grid).values():
        for (x1, y1), (x2, y2) in itertools.permutations(cords, r=2):
            x = 2 * x1 - x2
            y = 2 * y1 - y2
            if 0 <= x < n and 0 <= y < n:
                antinode_locations.add((x, y))

    return len(antinode_locations)


def puzzle16(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()
    n = len(grid)
    assert n == len(grid[0])

    antinode_locations = set()
    for cords in extract_antennas(grid).values():
        for (x1, y1), (x2, y2) in itertools.permutations(cords, r=2):
            if x1 == x2:
                antinode_locations.update((x1, y) for y in range(n))
            else:
                antinode_locations.update((x, y) for x in range(n)
                                          if (y2 - y1) * (x - x1) % (x2 - x1) == 0 and
                                          0 <= (y := y1 + (y2 - y1) * (x - x1) // (x2 - x1)) < n)

    return len(antinode_locations)


if __name__ == '__main__':
    print('Day #8, part one:', puzzle15('./input/day8.txt'))
    print('Day #8, part two:', puzzle16('./input/day8.txt'))
