import math
import re
import time

import file_handle


def parse_input(data: str) -> tuple[dict, tuple, tuple]:
    mapp = data.splitlines()
    s = (mapp[0].index('.'), 0)
    e = (mapp[-1].index('.'), len(mapp) - 1)

    graph: dict[tuple, set[tuple[tuple, int]]] = {}
    stack = [s]
    while stack:
        node = stack.pop()
        if node in graph:
            continue

        graph[node] = set()
        for neighbor in adjacency(node, mapp):
            dist = 1
            pre, curr = node, neighbor
            while len(adjacency(curr, mapp) - {pre}) == 1:
                dist += 1
                pre, curr = curr, (adjacency(curr, mapp) - {pre}).pop()

            graph[node].add((curr, dist))
            stack.append(curr)

    return graph, s, e


SLOPES = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1), }


def adjacency(node: tuple, mapp: list[str]) -> set[tuple]:
    (x, y) = node
    if mapp[y][x] in SLOPES:
        (dx, dy) = SLOPES[mapp[y][x]]
        (nx, ny) = (x + dx, y + dy)
        return {(nx, ny)} if mapp[ny][nx] != '#' else set()

    rows, cols = len(mapp), len(mapp[0])
    return {(nx, ny)
            for (nx, ny) in {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
            if 0 <= nx < cols and 0 <= ny < rows and mapp[ny][nx] != '#'}


def longest_path(s: tuple, e: tuple, path: set[tuple], graph: dict[tuple, set]) -> int:
    if s == e:
        return 0

    path.add(s)
    max_dist = -math.inf
    for (neighbor, dist) in graph[s]:
        if neighbor not in path:
            max_dist = max(max_dist, dist + longest_path(neighbor, e, path, graph))
    path.remove(s)

    return max_dist


def puzzle45(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    graph, s, e = parse_input(data)

    return longest_path(s, e, set(), graph)


def puzzle46(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    data = re.sub(r'[><^v]', '.', data)
    graph, s, e = parse_input(data)

    return longest_path(s, e, set(), graph)


if __name__ == '__main__':
    print('Day #23, part one:', puzzle45('./input/day23.txt'))
    timestamp = time.time()
    print('Day #23, part two:', puzzle46('./input/day23.txt'), f' (runtime={round(time.time() - timestamp, 1)}s) ')
