import re

import file_handle


def puzzle7(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    pairs = [re.split(r'[,-]', row) for row in data.splitlines()]

    count_ = 0
    for [a1, a2, b1, b2] in pairs:  # a1-a2,b1-b2
        count_ += int(a1) <= int(b1) <= int(b2) <= int(a2) or \
                  int(b1) <= int(a1) <= int(a2) <= int(b2)

    return count_


def puzzle8(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    pairs = [re.split(r'[,-]', row) for row in data.splitlines()]

    count_ = 0
    for [a1, a2, b1, b2] in pairs:  # a1-a2,b1-b2
        count_ += int(a1) <= int(b1) <= int(a2) or \
                  int(b1) <= int(a1) <= int(b2)

    return count_


if __name__ == '__main__':
    print('Day #4, part one:', puzzle7('./input/day4.txt'))
    print('Day #4, part two:', puzzle8('./input/day4.txt'))
