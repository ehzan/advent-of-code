import re

import file_handle


def puzzle1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    return sum(int((digits := re.findall(r'\d', line))[0] + digits[-1])
               for line in data.splitlines())


def puzzle2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    to_int = {digit: i + 1 for i, digit
              in enumerate('one|two|three|four|five|six|seven|eight|nine'.split('|'))}
    to_int.update({str(i): i for i in range(10)})

    sum_ = 0
    for line in data.splitlines():
        digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        sum_ += 10 * to_int[digits[0]] + to_int[digits[-1]]

    return sum_


if __name__ == '__main__':
    print('Day #1, part one:', puzzle1('./input/day1.txt'))
    print('Day #1, part two:', puzzle2('./input/day1.txt'))
