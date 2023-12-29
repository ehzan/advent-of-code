import timeit

answers = {'day1': (54634, 53855),
           'day2': (2776, 68638),
           'day3': (540212, 87605697),
           'day4': (18619, 8063216),
           'day5': (621354867, 15880236),
           'day6': (393120, 36872656),
           'day7': (249204891, 249666369),
           'day8': (15517, 14935034899483),
           'day9': (1939607039, 1041),
           'day10': (6682, 353),
           'day11': (9974721, 702770569197),
           'day12': (7674, 4443895258186),
           'day13': (33122, 32312),
           'day14': (109654, 94876),
           'day15': (517551, 286097),
           'day16': (7242, 7572),
           'day17': (797, 914),
           'day18': (34329, 42617947302920),
           'day19': (532551, 134343280273968),
           'day20': (743871576, 244151741342687),
           'day21': (3605, 596734624269210),
           'day22': (471, 68525),
           'day23': (2282, 6646),
           'day24': (13754, 711031616315001),
           'day25': (527790,),
           }

if __name__ == '__main__':
    for i in range(1, 26):
        t = timeit.timeit(stmt=f"ans = day{i}.puzzle{2 * i - 1}('./input/day{i}.txt');" +
                               f"print('Day #{i}, part one:', ans, end='  \t', );" +
                               f"assert ans == answers['day{i}'][0];",
                          setup=f"import day{i}",
                          globals={'answers': answers},
                          number=1)
        print(f"{'✅' if t < 5 else '⚠️ '}(runtime: {round(t, 2)}s)")

        if i == 25:
            break

        t = timeit.timeit(stmt=f"ans = day{i}.puzzle{2 * i}('./input/day{i}.txt');" +
                               f"print('Day #{i}, part two:', ans, end='  \t', );" +
                               f"assert ans == answers['day{i}'][1];",
                          setup=f"import day{i}",
                          globals={'answers': answers},
                          number=1)
        print(f"{'✅' if t < 5 else '⚠️ '}(runtime: {round(t, 2)}s)")
        print()
