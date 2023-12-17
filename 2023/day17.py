import heapq
import math
import time
from collections import namedtuple, defaultdict
from typing import Iterator

import file_handle

State = namedtuple('state', ('x', 'y', 'rx', 'ry'))


def next_states(curr: State, min_run: int, max_run: int) -> Iterator[State]:
    (x, y, rx, ry) = curr
    if rx == ry == 0:
        yield State(1, 0, 1, 0)
        yield State(0, 1, 0, 1)

    if 0 < abs(rx) < max_run:
        d = 1 if rx > 0 else -1
        yield State(x + d, y, rx + d, 0)
    if 0 < abs(ry) < max_run:
        d = 1 if ry > 0 else -1
        yield State(x, y + d, 0, ry + d)

    if min_run <= abs(rx):
        yield State(x, y - 1, 0, -1)
        yield State(x, y + 1, 0, 1)
    if min_run <= abs(ry):
        yield State(x - 1, y, -1, 0)
        yield State(x + 1, y, 1, 0)


def dijkstra(start: tuple[int, int], end: tuple[int, int], min_run: int, max_run: int,
             weights: list[list[int]], ) -> int | None:
    width, height = len(weights[0]), len(weights)
    starting_state = State(*start, 0, 0)
    dist = defaultdict(lambda: math.inf, {starting_state: 0})

    queue = [(0., starting_state)]
    while queue:
        (_, curr) = heapq.heappop(queue)
        if (curr.x, curr.y) == end:
            return int(dist[curr])
        for next_state in next_states(curr, min_run, max_run):
            if 0 <= next_state.x < width and 0 <= next_state.y < height and \
                    dist[next_state] > dist[curr] + weights[next_state.y][next_state.x]:
                dist[next_state] = dist[curr] + weights[next_state.y][next_state.x]
                heapq.heappush(queue, (dist[next_state], next_state))

    return None


def puzzle33(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    weights = [[int(cost) for cost in row] for row in data.splitlines()]

    end = (len(weights[0]) - 1, len(weights) - 1)
    min_cost = dijkstra((0, 0), end, 1, 3, weights)

    return min_cost


def puzzle34(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    weights = [[int(cost) for cost in row] for row in data.splitlines()]

    end = (len(weights[0]) - 1, len(weights) - 1)
    min_cost = dijkstra((0, 0), end, 4, 10, weights)

    return min_cost


if __name__ == '__main__':
    print('Day #17, part one:', puzzle33('./input/day17.txt'))
    timestamp = time.time()
    print('Day #17, part two:', puzzle34('./input/day17.txt'), f' (runtime: {round(time.time() - timestamp, 1)}s) ')
