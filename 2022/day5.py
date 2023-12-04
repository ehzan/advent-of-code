import re

import file_handle


def parse_input(data: str) -> tuple[list, list]:
    stacks_data, instructions_data = data.split('\n\n')

    instructions = instructions_data.strip().splitlines()

    rows = stacks_data.splitlines()
    last_line = rows.pop()
    stacks_count = len(re.findall(r'\d+', last_line))
    stacks = [[] for _ in range(stacks_count + 1)]

    rows.reverse()
    for row in rows:
        matches = re.findall(r'[ \[](\w+| )[ \]]\s?', row)
        for key, item in enumerate(matches):
            if item != ' ':
                stacks[key + 1].append(item)

    return instructions, stacks


def puzzle9(input_file: str) -> str:
    data = file_handle.readfile(input_file)
    instructions, stacks = parse_input(data)

    for instruct in instructions:
        parts = re.split(r'move | from | to ', instruct)
        number, origin, destination = int(parts[1]), int(parts[2]), int(parts[3])
        for _ in range(number):
            stacks[destination].append(stacks[origin].pop())

    return ''.join(stack[-1] for stack in stacks[1:])


def puzzle10(input_file: str) -> str:
    data = file_handle.readfile(input_file)
    instructions, stacks = parse_input(data)

    for instruct in instructions:
        parts = re.split(r'move | from | to ', instruct)
        number, origin, destination = int(parts[1]), int(parts[2]), int(parts[3])
        stacks[destination] += stacks[origin][-number:]
        stacks[origin] = stacks[origin][:-number]

    return ''.join(stack[-1] for stack in stacks[1:])


if __name__ == '__main__':
    print('Day #5, part one:', puzzle9('./input/day5.txt'))
    print('Day #5, part two:', puzzle10('./input/day5.txt'))
