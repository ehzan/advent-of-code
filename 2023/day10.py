import file_handle

pipes = {'F': [(1, 0), (0, 1)],
         'J': [(-1, 0), (0, -1)],
         '-': [(-1, 0), (1, 0)],
         '|': [(0, -1), (0, 1)],
         '7': [(-1, 0), (0, 1)],
         'L': [(1, 0), (0, -1)],
         '.': [],
         'S': [], }


def start_position(grid: list[str]) -> tuple[int, int]:
    (Sx, Sy) = next((row.index('S'), y) for y, row in enumerate(grid) if 'S' in row)

    for (dx, dy) in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        if (-dx, -dy) in pipes[grid[Sy + dy][Sx + dx]]:
            pipes['S'].append((dx, dy))

    return Sx, Sy


def next_position(curr: tuple[int, int], grid: list[str], visited: set[tuple]) \
        -> tuple[int, int] | None:
    (x, y) = curr
    return next(((x + dx, y + dy) for (dx, dy) in pipes[grid[y][x]]
                 if (x + dx, y + dy) not in visited), None)


def puzzle19(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()

    visited = set()
    curr = start_position(grid)
    while curr:
        visited.add(curr)
        curr = next_position(curr, grid, visited)

    return len(visited) // 2


def puzzle20(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()

    visited = set()
    curr = start_position(grid)
    while curr:
        visited.add(curr)
        curr = next_position(curr, grid, visited)

    enclosed_tiles = 0
    for y in range(len(grid)):
        ray_conjunction = 0
        for x in range(len(grid[y])):
            if (x, y) in visited:
                ray_conjunction += grid[y][x] in '|F7'
            else:
                enclosed_tiles += ray_conjunction % 2

    return enclosed_tiles


if __name__ == '__main__':
    print('Day #10, part one:', puzzle19('./input/day10.txt'))
    print('Day #10, part two:', puzzle20('./input/day10.txt'))
