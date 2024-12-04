import itertools

import file_handle


def get_diagonals(rows: list[str]) -> list[str]:
    n = len(rows)
    diagonals = []
    for x in range(n):
        dld, dlu, drd, dru = '', '', '', ''
        for xi in range(x, -1, -1):
            dld += rows[x - xi][xi]
            dlu += rows[n - 1 - x + xi][xi]
        for xi in range(x, n):
            drd += rows[xi - x][xi]
            dru += rows[n - 1 + x - xi][xi]

        diagonals.extend([dld, drd])
        if x != n - 1:
            diagonals.append(dlu)
        if x != 0:
            diagonals.append(dru)

    return diagonals


def puzzle7(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rows = data.splitlines()

    # ny, nx = len(rows), len(rows[0])
    # xmas_count = 0
    # for y in range(ny):
    #     for x in range(nx):
    #         for (dx, dy) in set(itertools.product((-1, 0, 1), repeat=2)) - {(0, 0)}:
    #             if 0 <= x + 3 * dx < nx and 0 <= y + 3 * dy < ny:
    #                 xmas_count += 'XMAS' == rows[y][x] + rows[y + dy][x + dx] + rows[y + 2 * dy][x + 2 * dx] + \
    #                               rows[y + 3 * dy][x + 3 * dx]

    cols = [''.join(col) for col in zip(*rows)]
    diagonals = get_diagonals(rows)
    return sum(line.count('XMAS') + line.count('SAMX') for line in rows + cols + diagonals)


def puzzle8(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()

    ny, nx = len(grid), len(grid[0])
    x_mas_count = 0
    for y in range(ny):
        for x in range(nx):
            found = 0
            for dx, dy in itertools.product((-1, 1), repeat=2):
                if 0 <= x - dx < nx and 0 <= x + dx < nx and 0 <= y - dy < ny and 0 <= y + dy < ny:
                    found += 'MAS' == grid[y - dy][x - dx] + grid[y][x] + grid[y + dy][x + dx]
            x_mas_count += found == 2

    return x_mas_count


if __name__ == '__main__':
    print('Day #4, part one:', puzzle7('./input/day4.txt'))
    print('Day #4, part two:', puzzle8('./input/day4.txt'))
