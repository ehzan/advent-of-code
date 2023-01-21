import fileHandle, re


def floyd_warshall(adjacents):
    n = len(adjacents)
    MAX_PATH_LENGTH = 30
    _dist = [[MAX_PATH_LENGTH] * n for _ in range(n)]
    for v1 in range(n):
        for v2 in adjacents[v1]:
            _dist[v1][v2] = 1
    for mid in range(n):
        for v1 in range(n):
            for v2 in range(n):
                _dist[v1][v2] = min(_dist[v1][v2], _dist[v1][mid] + _dist[mid][v2])
    return _dist


def parse_input(input_file):
    data = fileHandle.readfile(input_file)
    valves_spec = [re.findall(r'[A-Z]{2}|\d+', line) for line in data.splitlines()]
    valves = [spec[0] for spec in valves_spec]
    _flow_rates = [int(spec[1]) for spec in valves_spec]
    adjacents = [{valves.index(v) for v in spec[2:]} for spec in valves_spec]
    _dist = floyd_warshall(adjacents)
    return valves, _flow_rates, _dist


def max_flow(v1, t1, closed_valves):
    _max = 0
    for v in closed_valves:
        if t1 > dist[v1][v] + 1:
            closed2 = closed_valves.copy()
            closed2.remove(v)
            t = t1 - dist[v1][v] - 1
            p = flow_rates[v] * t + max_flow(v, t, closed2)
            _max = max(_max, p)
    return _max


def dfs(cur, t1, closed_valves):
    v1 = cur[-1]
    if len(closed_valves - set(cur)) == 0:
        dfs.i = dfs.i + 1 if hasattr(dfs, 'i') else 1

        print(dfs.i, cur)

    for v in closed_valves - set(cur):
        print(cur, 'v=', v)
        if t1 > dist[v1][v] + 1:
            t = t1 - dist[v1][v] - 1
            dfs(cur + (v,), t, closed_valves)


def puzzle31(input_file):
    global dist, flow_rates
    valves, flow_rates, dist = parse_input(input_file)
    closed_valves = {i for i in range(len(valves)) if flow_rates[i] > 0}

    print(closed_valves)
    # ans = max_flow(valves.index('AA'), 30, closed_valves)
    dfs((valves.index('AA'),), 30, closed_valves)
    return


# print('Day #16, Part One:', puzzle31('day16.txt'))
print('Day #16, Part One:', puzzle31('input.txt'))
