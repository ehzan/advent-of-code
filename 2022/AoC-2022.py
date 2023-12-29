import timeit

answers = {'day1': (70698, 206643),
           'day2': (10816, 11657),
           'day3': (8139, 2668),
           'day4': (588, 911),
           'day5': ('QMBMJDFTD', 'NBTVTJNFJ'),
           'day6': (1855, 3256),
           'day7': (1443806, 942298),
           'day8': (1669, 331344),
           'day9': (5878, 2405),
           'day10': (13860, 'RZHFGJCB'),
           'day11': (50616, 11309046332),
           'day12': (447, 446),
           'day13': (6395, 24921),
           'day14': (774, 22499),
           'day15': (4985193, 11583882601918),
           'day16': (2250, 3015),
           'day17': (3200, 1584927536247),
           'day18': (3396, 2044),
           'day19': (1349, 21840),
           'day20': (988, 7768531372516),
           'day21': (194058098264286, 3592056845086),
           'day22': (27436, 15426),
           'day23': (3940, 990),
           'day24': (290, 842),
           'day25': ('2-02===-21---2002==0',),
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
