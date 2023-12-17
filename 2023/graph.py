import heapq
import math
import re
import time

import file_handle


def refine_file(input_file: str, directed=False):
    import random
    with open(input_file, 'r') as f:
        data = f.read().strip()

    edges = {tuple(map(int, row.split())) for row in data.splitlines()}
    if not directed:
        edges = {(min(u, v), max(u, v)) for (u, v) in edges}
    nodes = {v for edge in edges for v in edge}
    print(len(nodes), len(edges), len(edges) / len(nodes))

    i = input_file.rindex('.')
    input_file = input_file[:i] + '-weighted' + input_file[i:]
    edges = list(edges)
    edges.sort()
    with open(input_file, 'w') as f:
        f.writelines(f'({u},{v}) : {random.randint(1, 100)}\n' for (u, v) in edges)


def build_adjacency_matrix(data: str, directed=False, weighted=False) \
        -> tuple[list[list[int]], list[str]]:
    edges = set(re.findall(r'\((\d+),(\d+)\) : (\d+)', data))
    nodes = list({v for edge in edges for v in edge[:2]})

    adjacency_matrix = [[0] * len(nodes) for _ in range(len(nodes))]
    node_index = {node: i for i, node in enumerate(nodes)}

    for (u, v, weight) in edges:
        u, v = node_index[u], node_index[v]
        adjacency_matrix[u][v] = int(weight) if weighted else 1
        if not directed:
            adjacency_matrix[v][u] = adjacency_matrix[u][v]

    return adjacency_matrix, nodes


def build_adjacency_list(data: str, directed=False, weighted=False) \
        -> tuple[list[set[tuple]], list[str]]:
    edges = set(re.findall(r'\((\d+),(\d+)\) : (\d+)', data))
    nodes = list({v for edge in edges for v in edge[:2]})

    adjacency_list = [set() for _ in range(len(nodes))]
    node_index = {node: i for i, node in enumerate(nodes)}

    for (u, v, weight) in edges:
        u, v = node_index[u], node_index[v]
        weight = int(weight) if weighted else 1
        adjacency_list[u].add((v, weight))
        if not directed:
            adjacency_list[v].add((u, weight))

    return adjacency_list, nodes


def dijkstra1(src: int, adjacency_matrix: list[list[int]]) -> tuple[list, list]:
    n = len(adjacency_matrix)
    dist = [math.inf] * n
    pre: list[int | None] = [None] * n

    queue = {src}
    dist[src] = 0
    while queue:
        (_, u) = min((dist[node], node) for node in queue)
        queue.remove(u)

        for v in range(n):
            if adjacency_matrix[u][v] and dist[v] > dist[u] + adjacency_matrix[u][v]:
                dist[v] = dist[u] + adjacency_matrix[u][v]
                pre[v] = u
                queue.add(v)

    return dist, pre


def dijkstra2(src: int, adjacency_list: list[set[tuple]]) -> tuple[list, list]:
    n = len(adjacency_list)
    dist = [math.inf] * n
    pre: list[int | None] = [None] * n

    queue = [(0., src)]
    dist[src] = 0
    while queue:
        (_, u) = heapq.heappop(queue)
        for (v, weight) in adjacency_list[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                pre[v] = u
                heapq.heappush(queue, (dist[v], v))

    return dist, pre


def print_paths(src: int, nodes: list[str], dist: list[float], pre: list[int]):
    for v in range(0, len(dist), len(dist) // 5):
        path = ''
        node = nodes[v]
        distance = dist[v]
        if dist[v] < math.inf:
            while v != src:
                path = '-' + nodes[v] + path
                v = pre[v]
            path = nodes[v] + path
        print(f'{node}: {distance} ({path})')
    print()


def test(input_file: str):
    data = file_handle.readfile(input_file)
    adjacency_matrix, nodes = build_adjacency_matrix(data, False, True)
    adjacency_list, nodes = build_adjacency_list(data, False, True)

    src = 0
    print(f'number of nodes: {len(adjacency_list)} \t src: {nodes[0]}\n')

    timestamp = time.time()
    dist, pre = dijkstra1(src, adjacency_matrix)
    print('dijkstra (adjacency matrix)\t time:', time.time() - timestamp)
    print_paths(src, nodes, dist, pre)

    timestamp = time.time()
    dist, pre = dijkstra2(src, adjacency_list)
    print('dijkstra (adjacency list)\t time:', time.time() - timestamp)
    print_paths(src, nodes, dist, pre)


if __name__ == "__main__":
    # refine_file('./input/twitter.edges', True)
    # refine_file('./input/facebook-1912.edges', False)

    test('./input/facebook-weighted.edges')
    # test('./input/twitter-weighted.edges')
