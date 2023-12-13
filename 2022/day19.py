import functools
import math
import re
import time

import file_handle


class Tuple_(tuple):

    def __add__(self, other):
        return Tuple_(a + b for a, b in zip(self, other))

    def __sub__(self, other):
        return Tuple_(a - b for a, b in zip(self, other))

    def __mul__(self, other: int):
        return Tuple_(a * other for a in self)

    def __matmul__(self, other) -> bool:
        # not efficient: return all(a >= b for a, b in zip(self, other))
        for a, b in zip(self, other):
            if a < b:
                return False
        return True


global blueprint


def parse_input(data: str) -> list[dict]:
    regex = r'Blueprint (\d+):.* (\d+).* (\d+).* (\d+) ore and (\d+) clay.* (\d+) ore and (\d+) obsidian'
    return [{'id': int(match[0]),
             'ore': (int(match[1]), 0, 0),
             'clay': (int(match[2]), 0, 0),
             'obsidian': (int(match[3]), int(match[4]), 0),
             'geode': (int(match[5]), 0, int(match[6])),
             'max': (max(int(match[1]), int(match[2]), int(match[3]), int(match[5]), ),
                     int(match[4]),
                     int(match[6])),
             } for match in re.findall(regex, data)]


@functools.cache
def max_geodes_slow(t: int, minerals: Tuple_, robots: Tuple_, ) -> int:
    if t == 1:
        return 0

    new_minerals, new_robots = check_sufficient(t, minerals, robots)
    if new_minerals != minerals:
        return max_geodes_slow(t, new_minerals, new_robots)

    geodes = [max_geodes_slow(t - 1, minerals + robots, robots)]

    for i, key in enumerate(['ore', 'clay', 'obsidian']):
        if minerals[i] != math.inf and minerals @ blueprint[key]:
            new_minerals = minerals + robots - blueprint[key]
            new_robots = robots + (i == 0, i == 1, i == 2)
            geodes.append(max_geodes_slow(t - 1, new_minerals, new_robots))

    if minerals @ blueprint['geode']:
        new_minerals = minerals + robots - blueprint['geode']
        geodes.append(t - 1 + max_geodes_slow(t - 1, new_minerals, robots))

    return max(geodes)


@functools.cache
def max_geodes(t: int, minerals: Tuple_, robots: Tuple_, ) -> int:
    new_minerals, new_robots = check_sufficient(t, minerals, robots)
    if new_minerals != minerals:
        return max_geodes(t, new_minerals, new_robots)

    geodes = [0]
    for i, robot_type in enumerate(['ore', 'clay', 'obsidian', 'geode']):
        if robot_type == 'geode' or minerals[i] < math.inf:
            rt = required_time(robot_type, minerals, robots)
            if rt < t:
                new_minerals = minerals + robots * rt - blueprint[robot_type]
                new_robots = robots + (i == 0, i == 1, i == 2)
                geodes.append(max_geodes(t - rt, new_minerals, new_robots)
                              + (t - rt if robot_type == 'geode' else 0))

    return max(geodes)


def check_sufficient(t: int, minerals: Tuple_, robots: Tuple_) -> tuple[Tuple_, Tuple_]:
    minerals, robots = list(minerals), list(robots)

    for i in range(len(minerals)):
        if (t - 1) * blueprint['max'][i] <= minerals[i] + (t - 2) * robots[i]:
            minerals[i], robots[i] = math.inf, 0

    return Tuple_(minerals), Tuple_(robots)


def required_time(robot_type: str, minerals: Tuple_, robots: Tuple_) -> int:
    needed_times = [1 if cost <= curr else
                    math.inf if not gain else
                    1 + math.ceil((cost - curr) / gain)
                    for cost, curr, gain in zip(blueprint[robot_type], minerals, robots)]
    return max(needed_times)


def puzzle37(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    blueprints = parse_input(data)

    global blueprint
    ans = 0
    for blueprint in blueprints:
        ans += blueprint['id'] * max_geodes(24, Tuple_((0, 0, 0)), Tuple_((1, 0, 0)), )
        max_geodes.cache_clear()

    return ans


def puzzle38(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    blueprints = parse_input(data)

    global blueprint
    ans = 1
    for blueprint in blueprints[:3]:
        ans *= max_geodes(32, Tuple_((0, 0, 0)), Tuple_((1, 0, 0)), )
        max_geodes.cache_clear()

    return ans


if __name__ == '__main__':
    print('Day #19, part one:', puzzle37('./input/day19.txt'))
    timestamp = time.time()
    print('Day #19, part one:', puzzle38('./input/day19.txt'), f' (runtime: {round(time.time() - timestamp, 1)}s) ')
