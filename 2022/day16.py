import functools
import re
import time

import file_handle


def parse_input(data: str) -> list[dict]:
    valve_specs = re.findall(r'^Valve (\w+).*=(\d+).* valves? (.*)$', data, re.MULTILINE)

    _graph = [{'name': spec[0],
               'flow_rate': int(spec[1]),
               'adjacency': spec[2].split(', '), }
              for spec in valve_specs]

    index = {valve['name']: i for i, valve in enumerate(_graph)}
    for node in _graph:
        node['adjacency'] = {index[name] for name in node['adjacency']}

    return _graph


def floyd_warshall(graph: list[dict]) -> list[list[int]]:
    infinity = 30
    n = len(graph)
    _dist = [[infinity] * n for _ in range(n)]

    for v in range(n):
        _dist[v][v] = 0
        for u in graph[v]['adjacency']:
            _dist[v][u] = 1

    for mid in range(n):
        for v in range(n):
            for u in range(n):
                _dist[v][u] = min(_dist[v][u], _dist[v][mid] + _dist[mid][u])

    return _dist


def dfs(v: int, t: int, valves: frozenset[int]) -> int:
    _max_flow = 0
    dfs_stack = [(v, t, 0, valves,)]
    while dfs_stack:
        (v, t, p, remaining) = dfs_stack.pop()
        _max_flow = max(_max_flow, p)
        for u in remaining:
            if (tt := t - dist[v][u] - 1) > 0:
                pp = p + graph[u]['flow_rate'] * tt
                dfs_stack.append((u, tt, pp, remaining - {u},))

    return _max_flow


global graph, dist, v0, t0


@functools.cache
def max_flow1(v: int, t: int, remaining: frozenset[int]) -> int:
    _max_flow = 0
    for u in remaining:
        if (tt := t - dist[u][v] - 1) > 0:
            flow = graph[u]['flow_rate'] * tt + max_flow1(u, tt, remaining - {u}, )
            _max_flow = max(_max_flow, flow)
    return _max_flow


def max_flow2(v: int, t: int, remaining: frozenset[int]) -> int:
    _max_flow = max_flow1(v0, t0, remaining)
    for u in remaining:
        if (tt := t - dist[u][v] - 1) > 0:
            flow = graph[u]['flow_rate'] * tt + max_flow2(u, tt, remaining - {u}, )
            _max_flow = max(_max_flow, flow)
    return _max_flow


def puzzle31(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    global graph, dist, v0, t0
    graph = parse_input(data)
    dist = floyd_warshall(graph)
    v0, t0 = 0, 30
    while graph[v0]['name'] != 'AA':
        v0 += 1

    valves = frozenset(i for i in range(len(graph)) if graph[i]['flow_rate'] > 0)

    return max_flow1(v0, t0, valves, )


def puzzle32(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    global graph, dist, v0, t0
    graph = parse_input(data)
    dist = floyd_warshall(graph)
    v0, t0 = 0, 26
    while graph[v0]['name'] != 'AA':
        v0 += 1

    valves = frozenset(i for i in range(len(graph)) if graph[i]['flow_rate'] > 0)

    return max_flow2(v0, t0, valves, )


if __name__ == '__main__':
    print('Day #16, part one:', puzzle31('./input/day16.txt'))
    timestamp = time.time()
    print('Day #16, part two:', puzzle32('./input/day16.txt'), f' (runtime: {round(time.time() - timestamp, 1)}s) ')
