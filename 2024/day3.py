import re

import file_handle


def puzzle5(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    operand_pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
    return sum(int(operands[0]) * int(operands[1]) for operands in operand_pairs)


def puzzle6(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    enabled_parts = re.findall(r'(?:^|do\(\)).*?(?:don\'t\(\)|$)', data, flags=re.DOTALL)
    operand_pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', '-'.join(enabled_parts))

    return sum(int(operands[0]) * int(operands[1]) for operands in operand_pairs)


if __name__ == '__main__':
    print('Day #3, part one:', puzzle5('./input/day3.txt'))
    print('Day #3, part two:', puzzle6('./input/day3.txt'))
