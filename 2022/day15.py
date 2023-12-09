import itertools
import re

import file_handle


def parse_input(data: str) -> list[tuple]:
    sensor_beacons = [map(int, re.findall(r'-?\d+', row))
                      for row in data.splitlines()]
    sensors = [(Sx, Sy, abs(Sx - Bx) + abs(Sy - By))
               for Sx, Sy, Bx, By in sensor_beacons]
    return sensors


def join_segments(segments: list[tuple]) -> list[tuple]:
    segments.sort()
    joined_segments = segments[:1]

    for (b1, b2) in segments[1:]:
        (a1, a2) = joined_segments[-1]
        if b1 <= a2:
            joined_segments[-1] = (a1, max(a2, b2))
        else:
            joined_segments.append((b1, b2))

    return joined_segments


def puzzle29(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    sensors = parse_input(data)

    row_y = 2000000
    segments = []
    for (x, y, d) in sensors:
        if abs(row_y - y) <= d:
            dx = d - abs(row_y - y)
            segments.append((x - dx, x + dx))

    joined_segments = join_segments(segments)
    segment_lengths = [x2 - x1 for (x1, x2) in joined_segments]

    return sum(segment_lengths)


def puzzle30(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    sensors = parse_input(data)

    b, c = 0, 0
    for (x1, y1, d1), (x2, y2, d2) in itertools.product(sensors, repeat=2):
        # y=x+b
        b1 = y1 - x1 - d1
        b2 = y2 - x2 + d2
        if b1 == b2 + 2:
            b = b2 + 1
        # y=-x+c
        c1 = y1 + x1 - d1
        c2 = y2 + x2 + d2
        if c1 == c2 + 2:
            c = c2 + 1

    y = (b + c) // 2
    x = (c - b) // 2

    return x * 4000000 + y


if __name__ == '__main__':
    print('Day #15, part one:', puzzle29('./input/day15.txt'))
    print('Day #15, part two:', puzzle30('./input/day15.txt'))
