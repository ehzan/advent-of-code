import re

import file_handle


def area(polygon_sides: list[tuple[str, int]]) -> int:
    _area = x_distance = 1
    for (direction, length) in polygon_sides:
        match direction:
            case 'R':
                x_distance += length
                _area += length
            case 'L':
                x_distance -= length
            case 'D':
                _area += x_distance * length
            case 'U':
                _area -= (x_distance - 1) * length
    return _area


def puzzle35(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    sides = re.findall(r'^(\w) (\d+) .*$', data, re.MULTILINE)
    sides = [(d, int(l)) for (d, l) in sides]

    return area(sides)


def puzzle36(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    sides = re.findall(r'\(#(\w*)(\d)\)', data, re.MULTILINE)
    sides = [('RDLU'[int(idx)], int(hex_l, base=16)) for (hex_l, idx) in sides]

    return area(sides)


if __name__ == '__main__':
    print('Day #18, part one:', puzzle35('./input/day18.txt'))
    print('Day #18, part two:', puzzle36('./input/day18.txt'))
