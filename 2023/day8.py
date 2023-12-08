import math
import re

import file_handle


def parse_input(data: str) -> tuple[str, dict]:
    instructions, graph_data = data.split('\n\n')
    graph = {node[0]: {'L': node[1], 'R': node[2]}
             for node in re.findall(r'(\w+) = \((\w+), (\w+)\)', graph_data)}

    return instructions, graph


def chinese_remainder(divisors: list[int], remainders: list[int]) -> int:
    number = remainders[0]
    lcm_ = divisors[0]
    for d, r in zip(divisors, remainders):
        while number % d != r % d:
            number += lcm_
        lcm_ = math.lcm(lcm_, d)

    return number


def puzzle15(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    instructions, graph = parse_input(data)

    step, curr = 0, 'AAA'
    while curr != 'ZZZ':
        rl = instructions[step % len(instructions)]
        curr = graph[curr][rl]
        step += 1

    return step


def puzzle16(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    instructions, graph = parse_input(data)

    end_reach_steps, cycles = [], []
    for curr in [node for node in graph if node.endswith('A')]:
        i, step = 0, 0
        first_visit = {}

        while (i, curr) not in first_visit:
            if curr.endswith('Z'):
                end_reach_steps.append(step)
            first_visit[(i, curr)] = step
            curr = graph[curr][instructions[i]]
            step += 1
            i = step % len(instructions)

        cycles.append(step - first_visit[(i, curr)])
        assert len(cycles) == len(end_reach_steps)

    return chinese_remainder(cycles, end_reach_steps)


if __name__ == '__main__':
    print('Day #8, part one:', puzzle15('./input/day8.txt'))
    print('Day #8, part two:', puzzle16('./input/day8.txt'))
