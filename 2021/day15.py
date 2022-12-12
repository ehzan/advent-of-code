import fileHandle
import heapq


def adjacent(node, node_risk):
    neighbors = set()
    y, x = node[0], node[1]
    if y > 0: neighbors.add((y - 1, x))
    if y < len(node_risk) - 1: neighbors.add((y + 1, x))
    if x > 0: neighbors.add((y, x - 1))
    if x < len(node_risk[y]) - 1: neighbors.add((y, x + 1))
    return neighbors


def calculate_path_risks(s, node_risk, path_risk):
    check_list = {s}
    while check_list:
        node = check_list.pop()
        current_risk = path_risk[node[0]][node[1]]
        for a in adjacent(node, node_risk):
            if path_risk[a[0]][a[1]] > current_risk + node_risk[a[0]][a[1]]:
                path_risk[a[0]][a[1]] = current_risk + node_risk[a[0]][a[1]]
                check_list.add(a)


def puzzle29(input_file='day15.txt'):
    data = fileHandle.readfile(input_file)
    node_risk = [[int(d) for d in line] for line in data.splitlines()]
    MAX_RISK = len(node_risk) * 10
    path_risk = [[MAX_RISK] * len(row) for row in node_risk]
    path_risk[0][0] = 0
    calculate_path_risks((0, 0), node_risk, path_risk)
    return path_risk[-1][-1]


def calculate_path_risks2(s, node_risk, path_risk):
    reached_list = [(path_risk[s[0]][s[1]], s)]
    while reached_list:
        least = heapq.heappop(reached_list)
        node = least[1]
        current_risk = path_risk[node[0]][node[1]]
        for a in adjacent(node, node_risk):
            if path_risk[a[0]][a[1]] > current_risk + node_risk[a[0]][a[1]]:
                path_risk[a[0]][a[1]] = current_risk + node_risk[a[0]][a[1]]
                heapq.heappush(reached_list, (path_risk[a[0]][a[1]], a))


def puzzle30(input_file='day15.txt'):
    data = fileHandle.readfile(input_file)
    data = data.splitlines()
    node_risk = [[0] * len(data[0]) * 5 for i in range(len(data) * 5)]
    for y in range(len(node_risk)):
        for x in range(len(node_risk[y])):
            node_risk[y][x] = int(data[y % len(data)][x % len(data[0])]) + y // len(data) + x // len(data[0])
            node_risk[y][x] = node_risk[y][x] % 9 if node_risk[y][x] % 9 else 9
    MAX_RISK = len(node_risk) * 10 * 25
    path_risk = [[MAX_RISK] * len(row) for row in node_risk]
    path_risk[0][0] = 0
    calculate_path_risks2((0, 0), node_risk, path_risk)
    return path_risk[-1][-1]
