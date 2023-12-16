import time
from typing import Iterator

import file_handle

VECTORS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1), }


def exit_dirs(entrance_dir: str, cell: str) -> Iterator[str]:
    match cell:
        case '/':
            # L,R,U,D -> D,U,R,L
            yield 'DURL'['LRUD'.index(entrance_dir)]
        case '\\':
            # L,R,U,D -> U,D,L,R
            yield 'UDLR'['LRUD'.index(entrance_dir)]
        case '-' if entrance_dir in 'UD':
            yield 'L'
            yield 'R'
        case '|' if entrance_dir in 'LR':
            yield 'U'
            yield 'D'
        case _:
            yield entrance_dir


def energized_count(initial_beam: tuple[int, int, str], grid: list[str], ) -> int:
    width, height = len(grid[0]), len(grid)

    visited = set()
    beams = [initial_beam]
    while beams:
        beam = beams.pop()
        (x, y, entrance_dir) = beam
        if not (0 <= x < width and 0 <= y < height) or beam in visited:
            continue

        visited.add(beam)
        for exit_dir in exit_dirs(entrance_dir, grid[y][x]):
            dx, dy = VECTORS[exit_dir]
            beams.append((x + dx, y + dy, exit_dir))

    return len({(x, y) for (x, y, _) in visited})


def puzzle31(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()

    return energized_count((0, 0, 'R'), grid)


def puzzle32(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()

    width, height = len(grid[0]), len(grid)
    energized_counts = []
    for sx in range(width):
        energized_counts.append(energized_count((sx, 0, 'D'), grid))
        energized_counts.append(energized_count((sx, height - 1, 'U'), grid))
    for sy in range(height):
        energized_counts.append(energized_count((0, sy, 'R'), grid))
        energized_counts.append(energized_count((width - 1, sy, 'L'), grid))

    return max(energized_counts)


if __name__ == '__main__':
    print('Day #16, part one:', puzzle31('./input/day16.txt'))
    timestamp = time.time()
    print('Day #16, part two:', puzzle32('./input/day16.txt'), f' (runtime: {round(time.time() - timestamp, 1)}s) ')
