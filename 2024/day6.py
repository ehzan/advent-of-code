import re

import file_handle


def initial_state(grid: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    y = 0
    while re.search(r'[\^v<>]', grid[y]) is None:
        y += 1
    x = re.search(r'[\^v<>]', grid[y]).start()
    direction = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    return (x, y), direction[grid[y][x]]


def turn_right(dx: int, dy: int) -> tuple[int, int]:
    # return {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}[(dx,dy)]
    return (dy, dx) if dx else (-dy, -dx)


def visited(grid: list[str], start: tuple[int, int], direction: tuple[int, int]) \
        -> set[tuple[int, int]]:
    x, y = start
    dx, dy = direction
    visited_positions = {(x, y)}

    while 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
        if grid[y + dy][x + dx] == '#':
            dx, dy = turn_right(dx, dy)
        else:
            x, y = x + dx, y + dy
            visited_positions.add((x, y))

    return visited_positions


def stuck_in_loop(grid: list[str], start: tuple[int, int], direction: tuple[int, int],
                  obstacle: tuple[int, int]) -> bool:
    x, y = start
    dx, dy = direction
    visited_positions = set()

    while 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
        if (x, y, dx, dy) in visited_positions:
            return True
        visited_positions.add((x, y, dx, dy))
        if (x + dx, y + dy) == obstacle or grid[y + dy][x + dx] == '#':
            dx, dy = turn_right(dx, dy)
        else:
            x, y = x + dx, y + dy

    return False


def puzzle11(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()
    start, direction = initial_state(grid)

    return len(visited(grid, start, direction))


def puzzle12(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()
    start, direction = initial_state(grid)

    candidates = visited(grid, start, direction) - {start}
    return sum(stuck_in_loop(grid, start, direction, obstacle) for obstacle in candidates)


if __name__ == '__main__':
    print('Day #6, part one:', puzzle11('./input/day6.txt'))
    print('Day #6, part two:', puzzle12('./input/day6.txt'))
