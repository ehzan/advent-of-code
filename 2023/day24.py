import itertools
import re

import sympy

import file_handle


def intersection(l1: tuple, l2: tuple) -> tuple[int, int] | None:
    (x1, y1, z1, a1, b1, c1) = l1
    (x2, y2, z2, a2, b2, c2) = l2

    if a2 * b1 == a1 * b2:  # l1 & l2 are parallel
        return None

    x = (a1 * a2 * (y2 - y1) + a2 * b1 * x1 - a1 * b2 * x2) / (a2 * b1 - a1 * b2)
    y = b1 / a1 * (x - x1) + y1
    # l1 & l2 intersect at (x,y)
    return (x, y) if 0 <= (x - x1) * a1 and 0 <= (x - x2) * a2 else None


def puzzle47(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    lines = re.findall(r'(-?\d+), (-?\d+), (-?\d+) @ (-?\d+), (-?\d+), (-?\d+)', data)
    lines = [tuple(map(int, line)) for line in lines]

    area = (200000000000000, 400000000000000)
    crosses = 0
    for l1, l2 in itertools.combinations(lines, 2):
        point = intersection(l1, l2)
        crosses += point is not None and area[0] <= point[0] <= area[1] and area[0] <= point[1] <= area[1]

    return crosses


def puzzle48(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    lines = re.findall(r'(-?\d+), (-?\d+), (-?\d+) @ (-?\d+), (-?\d+), (-?\d+)', data)
    lines = [tuple(map(int, line)) for line in lines]

    x, y, z, a, b, c = sympy.symbols('x y z a b c')
    equations = []
    for l1 in lines[:4]:
        (x1, y1, z1, a1, b1, c1) = l1
        equations.append((b - b1) * (x - x1) - (a - a1) * (y - y1))
        equations.append((c - c1) * (x - x1) - (a - a1) * (z - z1))
    # print(*sympy.solve(equations), sep='\n')

    int_answers = [answer for answer in sympy.solve(equations)
                   if all(var == int(var) for var in answer.values())]

    return int_answers[0][x] + int_answers[0][y] + int_answers[0][z]


if __name__ == '__main__':
    print('Day #24, part one:', puzzle47('./input/day24.txt'))
    print('Day #24, part two:', puzzle48('./input/day24.txt'))
