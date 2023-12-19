import math
import re

import file_handle


def parse_input(data: str) -> tuple[dict, list]:
    workflows, parts = data.split('\n\n')

    workflows = re.findall(r'^(\w+)\{(.*)\}$', workflows, re.MULTILINE)
    rules = {workflow[0]: re.findall(r'(?:([^:]+):)?([^,]+)(?:,|$)', workflow[1])
             for workflow in workflows}

    parts = re.findall(r'\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}', parts)
    parts = [tuple(map(int, part)) for part in parts]

    return rules, parts


def is_accepted(part: tuple, work_flow: str, rules: dict[str, list]) -> bool:
    if work_flow in 'AR':
        return work_flow == 'A'

    for condition, next_workflow in rules[work_flow]:
        x, m, a, s = part
        if not condition or eval(condition):
            return is_accepted(part, next_workflow, rules)


def find_accepted_scopes(scope: dict[str, tuple], workflow: str, rules: dict[str, list],
                         ) -> list[dict[str, tuple]]:
    if workflow == 'A':
        return [scope]
    if workflow == 'R':
        return []

    accepted_scopes = []
    for condition, next_workflow in rules[workflow][:-1]:
        scope2 = scope.copy()
        parameter, op, value = condition[0], condition[1], int(condition[2:])

        satisfied_interval = (1, value) if op == '<' else (value + 1, 4001)
        scope2[parameter] = intersection(scope2[parameter], satisfied_interval)
        accepted_scopes += find_accepted_scopes(scope2, next_workflow, rules)

        unsatisfied_interval = (value, 4001) if op == '<' else (1, value + 1)
        scope[parameter] = intersection(scope[parameter], unsatisfied_interval)

    next_workflow = rules[workflow][-1][1]
    accepted_scopes += find_accepted_scopes(scope, next_workflow, rules)

    return accepted_scopes


def intersection(interval1: tuple, interval2: tuple) -> tuple:
    return max(interval1[0], interval2[0]), min(interval1[1], interval2[1])


def combination_count(scope: dict[str, tuple]) -> int:
    return math.prod(max(0, interval[1] - interval[0])
                     for interval in scope.values())


def puzzle37(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rules, parts = parse_input(data)

    accepted_parts = [part for part in parts if is_accepted(part, 'in', rules)]
    return sum(sum(map(int, part)) for part in accepted_parts)


def puzzle38(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rules, parts = parse_input(data)

    full_scope = {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001), }
    accepted_scopes = find_accepted_scopes(full_scope, 'in', rules)

    return sum(combination_count(scope) for scope in accepted_scopes)


if __name__ == '__main__':
    print('Day #19, part one:', puzzle37('./input/day19.txt'))
    print('Day #19, part two:', puzzle38('./input/day19.txt'))
