import time

import networkx

import file_handle


def pares_input(data: str) -> dict[str, list]:
    graph = {row.split(': ')[0]: row.split(': ')[1].split()
             for row in data.splitlines()}
    return graph


def puzzle49(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    graph = pares_input(data)

    nx_graph = networkx.Graph()
    nx_graph.add_edges_from((u, v) for u in graph for v in graph[u])

    minimum_cut = networkx.minimum_edge_cut(nx_graph)
    nx_graph.remove_edges_from(minimum_cut)
    component1, component2 = networkx.connected_components(nx_graph)

    return len(component1) * len(component2)


if __name__ == '__main__':
    timestamp = time.time()
    print('Day #25, part one:', puzzle49('./input/day25.txt'), f' (runtime={round(time.time() - timestamp, 1)}s) ')
