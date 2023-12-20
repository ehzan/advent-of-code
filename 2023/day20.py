import math
import re

import file_handle


def parse_input(data: str) -> dict[str, dict]:
    modules_info = re.findall(r'(^[%&]?)(\w+) -> (.+)$', data, re.MULTILINE)
    modules = {module[1]: {
        'type': module[0],
        'state': 0,
        'inputs': {},
        'outputs': module[2].split(', '),
    }
        for module in modules_info}

    for sender in modules:
        for receiver in modules[sender]['outputs']:
            if receiver in modules and modules[receiver]['type'] == '&':
                modules[receiver]['inputs'][sender] = 0

    return modules


def push_button(modules: dict[str, dict]) -> tuple[dict[int, int], set[str]]:
    pulse_count = {0: 1, 1: 0}
    got_high_modules = set()
    pulse_queue = [('broadcaster', 0)]

    for (sender, pulse) in pulse_queue:
        for receiver in modules[sender]['outputs']:
            pulse_count[pulse] += 1
            next_pulse = apply_pulse(sender, pulse, receiver, modules)
            if next_pulse is not None:
                pulse_queue.append((receiver, next_pulse))
                if next_pulse:
                    got_high_modules.add(receiver)

    return pulse_count, got_high_modules


def apply_pulse(sender: str, pulse: int, receiver: str, modules: dict[str, dict]) -> int | None:
    if receiver not in modules:
        return None

    receiver_module = modules[receiver]
    match receiver_module['type']:
        case '':
            return pulse
        case '%' if not pulse:
            receiver_module['state'] ^= 1
            return receiver_module['state']
        case '&':
            receiver_module['inputs'][sender] = pulse
            return 1 ^ math.prod(receiver_module['inputs'].values())


def chinese_remainder(divisors: list[int], remainders: list[int]) -> int:
    number = remainders[0]
    lcm_ = divisors[0]
    for d, r in zip(divisors, remainders):
        while number % d != r % d:
            number += lcm_
        lcm_ = math.lcm(lcm_, d)

    return number


def puzzle39(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    modules = parse_input(data)

    total_low_pulses = total_high_pulses = 0
    for _ in range(1000):
        pulse_count = push_button(modules)[0]
        total_low_pulses += pulse_count[0]
        total_high_pulses += pulse_count[1]

    return total_low_pulses * total_high_pulses


def puzzle40(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    modules = parse_input(data)

    inputs_of_inputs_of_rx = [module['inputs'] for module in modules.values()
                              if 'rx' in module['outputs']]
    observed_modules = set().union(*inputs_of_inputs_of_rx)

    i, first_high_pulse, module_cycles = 0, {}, {}
    while len(module_cycles) < len(observed_modules):
        i += 1
        got_high_modules = push_button(modules)[1]
        for module in got_high_modules.intersection(observed_modules):
            if module not in first_high_pulse:
                first_high_pulse[module] = i
            else:
                module_cycles[module] = i - first_high_pulse[module]

    key_list = list(observed_modules)
    divisors = [module_cycles[key] for key in key_list]
    remainders = [first_high_pulse[key] for key in key_list]

    return chinese_remainder(divisors, remainders)


if __name__ == '__main__':
    print('Day #20, part one:', puzzle39('./input/day20.txt'))
    print('Day #20, part two:', puzzle40('./input/day20.txt'))
