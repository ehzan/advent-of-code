import math
import re
import time

import file_handle


def parse_input(data: str) -> list[dict]:
    monkeys = []
    regex = (r'Monkey (\d+):\n' +
             r'.* items: ([0-9, ]*)\n' +
             r'.* new = (.*)\n' +
             r'.* divisible by (\d+)\n' +
             r'.* true: .* (\d+)\n' +
             r'.* false: .* (\d+)(?:\n{2}|$)')
    for (id_, items, op, divisor, if_true, if_false) in re.findall(regex, data):
        monkeys.append({'id': int(id_),
                        'activity': 0,
                        'items': list(map(int, items.split(', '))),
                        'operation': op,
                        'test_divisor': int(divisor),
                        'throw': {True: int(if_true), False: int(if_false), }
                        })
    return monkeys


def puzzle21(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    monkeys = parse_input(data)

    for _ in range(20):
        for monkey in monkeys:
            for val in monkey['items']:
                monkey['activity'] += 1
                old = val
                new_val = eval(monkey['operation']) // 3
                receiver = monkey['throw'][new_val % monkey['test_divisor'] == 0]
                monkeys[receiver]['items'].append(new_val)
            monkey['items'].clear()

    activities = sorted([monkey['activity'] for monkey in monkeys], reverse=True)
    return activities[0] * activities[1]


def puzzle22(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    monkeys = parse_input(data)
    lcm = math.lcm(*[monkey['test_divisor'] for monkey in monkeys])

    for _ in range(10000):
        for monkey in monkeys:
            for val in monkey['items']:
                monkey['activity'] += 1
                old = val
                new_val = eval(monkey['operation']) % lcm
                receiver = monkey['throw'][new_val % monkey['test_divisor'] == 0]
                monkeys[receiver]['items'].append(new_val)
            monkey['items'].clear()

    activities = sorted([monkey['activity'] for monkey in monkeys], reverse=True)
    return activities[0] * activities[1]


if __name__ == '__main__':
    print('Day #11, part one:', puzzle21('./input/day11.txt'))
    timestamp = time.time()
    print('Day #11, part two:', puzzle22('./input/day11.txt'), f' (runtime: {round(time.time() - timestamp, 1)}s) ')
