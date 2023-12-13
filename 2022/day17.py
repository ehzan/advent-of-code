from itertools import cycle
from typing import Generator

import file_handle


def plot():
    for row in reversed(chamber):
        for cell in row:
            print('#' if cell else '.', end='')
        print()


global chamber, jet_index


def rock_generator() -> Generator:
    rocks = [
        {(0, 0), (1, 0), (2, 0), (3, 0)},  # －
        {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},  # ➕
        {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},  # ᒧ
        {(0, 0), (0, 1), (0, 2), (0, 3)},  # |
        {(0, 0), (1, 0), (0, 1), (1, 1)},  # ◼
    ]
    heights = [1, 3, 3, 4, 2, ]
    for i in cycle(range(len(rocks))):
        yield rocks[i], heights[i]


def jet_generator(jet_pattern: str) -> Generator:
    global jet_index
    jet_index = -1
    dx = {'<': -1, '>': 1}
    for ch in cycle(jet_pattern):
        jet_index = (jet_index + 1) % len(jet_pattern)
        yield dx[ch]


def jet_push(x: int, y: int, rock: set[tuple], dx: int) -> int:
    if all(0 <= x + rx + dx <= 6 and not chamber[y + ry][x + rx + dx]
           for (rx, ry) in rock):
        x += dx
    return x


def fall(top: int, falling_rock: Generator, jet: Generator) -> int:
    global chamber
    chamber += [[0] * 7 for _ in range(len(chamber), top + 8)]
    rock, height = next(falling_rock)

    y = top + 4
    x = jet_push(2, y, rock, next(jet), )
    while all(not chamber[y + ry - 1][x + rx] for (rx, ry) in rock):
        y -= 1
        x = jet_push(x, y, rock, next(jet), )

    for (rx, ry) in rock:
        chamber[y + ry][x + rx] = 1

    return max(top, y + height - 1)


def column_tops(top: int) -> list[int]:
    global chamber
    col_tops = [0] * len(chamber[0])
    for x in range(len(col_tops)):
        y = top
        while not chamber[y][x]:
            y -= 1
        col_tops[x] = top - y

    return col_tops


def puzzle33(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    global chamber
    chamber = [[1] * 7]
    falling_rock = rock_generator()
    jet = jet_generator(data)

    top = 0
    for _ in range(2022):
        top = fall(top, falling_rock, jet)

    return top


def puzzle34(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    global chamber, jet_index
    chamber = [[1] * 7]
    falling_rock = rock_generator()
    jet = jet_generator(data)

    steps, top = 1000000000000, 0
    patterns, saved_tops = [], []

    for i in range(steps):
        if i % 5 == 0:
            pattern = (jet_index, *column_tops(top))
            if pattern in patterns:
                index = patterns.index(pattern)
                period = i - index * 5
                offset = top - saved_tops[index]
                return (steps // period) * offset + saved_tops[(steps % period) // 5]

            patterns.append(pattern)
            saved_tops.append(top)

        top = fall(top, falling_rock, jet)


if __name__ == '__main__':
    print('Day #17, part one:', puzzle33('./input/day17.txt'))
    print('Day #17, part two:', puzzle34('./input/day17.txt'))
