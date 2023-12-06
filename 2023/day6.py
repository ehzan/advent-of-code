import re
from math import sqrt, prod, ceil, floor

import file_handle


def puzzle11(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    times, distances = [map(int, row.split()[1:]) for row in data.splitlines()]

    ways2win = [sum(x * (t - x) > d for x in range(t))
                for t, d in zip(times, distances)]
    return int(prod(ways2win))


def puzzle12(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    t, d = [int(re.sub(r'\D', '', row)) for row in data.splitlines()]

    delta = sqrt(t ** 2 - 4 * d)
    r1, r2 = (t + delta) / 2, (t - delta) / 2
    return ceil(r1) - floor(r2) - 1


if __name__ == '__main__':
    print('Day #6, part one:', puzzle11('./input/day6.txt'))
    print('Day #6, part two:', puzzle12('./input/day6.txt'))
