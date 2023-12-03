import re

import file_handle


def adjacent_numbers(x, y, schematic) -> list[int]:
    adj = []
    for row in schematic[y - 1: y + 2]:
        precedent = re.search(r'\d*$', row[:x]).group()
        subsequent = re.search(r'^\d*', row[x + 1:]).group()
        if row[x].isdigit():
            adj.append(int(precedent + row[x] + subsequent))
        else:
            if precedent:
                adj.append(int(precedent))
            if subsequent:
                adj.append(int(subsequent))
    return adj


def puzzle5(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    schematic = data.splitlines()

    sum_ = 0
    for y, row in enumerate(schematic):
        for match in re.finditer(r'\d+', row):
            if any(ch not in '.0123456789'
                   for adj_row in schematic[max(0, y - 1): y + 2]
                   for ch in adj_row[max(0, match.start() - 1): match.end() + 1]):
                sum_ += int(match.group())

    return sum_


def puzzle6(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    schematic = data.splitlines()

    gears = {(x, y) for y, row in enumerate(schematic)
             for x, ch in enumerate(row) if ch == '*'}

    return sum(nums[0] * nums[1] for (x, y) in gears
               if len(nums := adjacent_numbers(x, y, schematic)) == 2)


if __name__ == '__main__':
    print('Day #3, part one:', puzzle5('./input/day3.txt'))
    print('Day #3, part two:', puzzle6('./input/day3.txt'))
