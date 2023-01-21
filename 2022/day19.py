import time

import fileHandle, re


def parse_input(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    data = [re.findall(r'\d+', line) for line in data]
    blueprints = [{'ore': int(d[1]), 'clay': int(d[2]), 'obsidian': (int(d[3]), int(d[4]), 0),
                   'geode': (int(d[5]), 0, int(d[6]),)} for d in data]
    return blueprints


def plus(tuple1, tuple2):
    return (tuple1[0] + tuple2[0],
            tuple1[1] + tuple2[1],
            tuple1[2] + tuple2[2],
            tuple1[3] + tuple2[3])


# ad = Infix(plus)


def calc(states, blueprint):
    next_level = set()
    for state in states:
        t, robots, minerals = state
        ore_robots, clay_robots, obsidian_robots, geode_robots = robots

        max_ore_consumption = max(blueprint['clay'], blueprint['obsidian'][0], blueprint['geode'][0])
        max_ore_needed = max_ore_consumption + (t - 1) * (max_ore_consumption - ore_robots)
        max_clay_needed = blueprint['obsidian'][1] + (t - 1) * (blueprint['obsidian'][1] - clay_robots)
        max_obsidian_needed = blueprint['geode'][2] + (t - 1) * (blueprint['geode'][2] - obsidian_robots)
        minerals = (min(minerals[0], max_ore_needed), min(minerals[1], max_clay_needed),
                    min(minerals[2], max_obsidian_needed), minerals[3])
        ore, clay, obsidian, geode = minerals
        # print(t, ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geode)
        # if geode_robots > 0:
        #     print(state)
        next_level.add((t - 1, robots, plus(minerals, robots, )))
        if ore >= blueprint['ore'] and ore < max_ore_needed:
            next_level.add((t - 1, plus(robots, (1, 0, 0, 0), ),
                            plus(plus(minerals, robots, ), (-blueprint['ore'], 0, 0, 0), )))
        if ore >= blueprint['clay'] and clay < max_clay_needed:
            next_level.add((t - 1, plus(robots, (0, 1, 0, 0), ),
                            plus(plus(minerals, robots, ), (-blueprint['clay'], 0, 0, 0), )))
        if ore >= blueprint['obsidian'][0] and clay >= blueprint['obsidian'][1] and obsidian < max_obsidian_needed:
            next_level.add((t - 1, plus(robots, (0, 0, 1, 0), ),
                            plus(plus(minerals, robots, ),
                                 (-blueprint['obsidian'][0], -blueprint['obsidian'][1], 0, 0), )))
        if ore >= blueprint['geode'][0] and obsidian >= blueprint['geode'][2]:
            next_level.add((t - 1, plus(robots, (0, 0, 0, 1), ),
                            plus(plus(minerals, robots, ),
                                 (-blueprint['geode'][0], 0, -blueprint['geode'][2], 0), )))
    return next_level


def puzzle37(input_file):
    blueprints = parse_input(input_file)
    print(blueprints[1])
    ans = 1
    _time = time.time()
    for n, bp in enumerate(blueprints[:3]):
        bfs = [set()] * 25
        bfs[0] = {(24, (1, 0, 0, 0), (0, 0, 0, 0)), }
        for i in range(24):
            bfs[i + 1] = calc(bfs[i], bp)
            # print(32 - i - 1, len(bfs[i + 1]), )
            # print(bfs[i + 1])
        print(n + 1, max(bfs[i + 1], key=lambda a: a[2][3])[2][3])
        print(time.time() - _time)
        ans *= max(bfs[i + 1], key=lambda a: a[2][3])[2][3]
    return ans


print('Day #19, Part One:', puzzle37('input.txt'))
