import re

import file_handle


def token_spent1(Ax: int, Ay: int, Bx: int, By: int, Px: int, Py: int) -> int:
    a_range = range(101) if Ax < 3 * Bx else range(100, -1, -1)
    for a in a_range:
        b = (Px - a * Ax) // Bx
        if 0 <= b <= 100 and Px == a * Ax + b * Bx and Py == a * Ay + b * By:
            return 3 * a + b
    return 0


def token_spent2(Ax: int, Ay: int, Bx: int, By: int, Px: int, Py: int) -> int:
    assert Ax * By != Ay * Bx

    a = (Px * By - Py * Bx) / (Ax * By - Ay * Bx)
    if a >= 0 and a.is_integer():
        b = (Py - a * Ay) / By
        if b >= 0 and b.is_integer():
            return 3 * int(a) + int(b)
    return 0


def puzzle25(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    machin_configs = [part for part in data.split('\n\n')]

    machin_configs = [list(map(int, re.findall(r'[+=](\d+)', prize, flags=re.DOTALL)))
                      for prize in machin_configs]

    return sum(token_spent1(*config) for config in machin_configs)


def puzzle26(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    machin_configs = [part for part in data.split('\n\n')]

    machin_configs = [list(map(int, re.findall(r'[+=](\d+)', prize, flags=re.DOTALL)))
                      for prize in machin_configs]
    d = 10000000000000
    return sum(token_spent2(*config[:4], d + config[4], d + config[5])
               for config in machin_configs)


if __name__ == '__main__':
    print('Day #13, part one:', puzzle25('./input/day13.txt'))
    print('Day #13, part two:', puzzle26('./input/day13.txt'))
