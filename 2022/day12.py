import fileHandle


def adjacent(position, h):
    neighbors = set()
    y, x = position[0], position[1]
    if y > 0: neighbors.add((y - 1, x))
    if y < len(h) - 1: neighbors.add((y + 1, x))
    if x > 0: neighbors.add((y, x - 1))
    if x < len(h[y]) - 1: neighbors.add((y, x + 1))
    return neighbors


def find_S_E(h):
    S, E = None, None
    for i in range(len(h)):
        if 'S' in h[i]:
            S = (i, h[i].index('S'))
            h[S[0]][S[1]] = 'a'
        if 'E' in h[i]:
            E = (i, h[i].index('E'))
            h[E[0]][E[1]] = 'z'
    return S, E


def shortest_path(S, E, h):
    MAX_PATH_LENGTH = len(h) * len(h[0])
    path_length = [[MAX_PATH_LENGTH] * len(h[i]) for i in range(len(h))]
    path_length[S[0]][S[1]] = 0
    check_list = {S}
    while check_list:
        point = check_list.pop()
        for a in adjacent(point, h):
            if ord(h[a[0]][a[1]]) <= ord(h[point[0]][point[1]]) + 1 and \
                    path_length[a[0]][a[1]] > path_length[point[0]][point[1]] + 1:
                path_length[a[0]][a[1]] = path_length[point[0]][point[1]] + 1
                if a != E:
                    check_list.add(a)
    return path_length[E[0]][E[1]]


def puzzle23(input_file):
    data = fileHandle.readfile(input_file)
    h = [[ch for ch in line] for line in data.splitlines()]
    S, E = find_S_E(h)
    return shortest_path(S, E, h)


def puzzle24b(input_file):
    data = fileHandle.readfile(input_file)
    h = [[ch for ch in line] for line in data.splitlines()]
    S, E = find_S_E(h)
    shortest_paths = set()
    for i in range(len(h)):
        for j in range(len(h[i])):
            if h[i][j] == 'a':
                S = (i, j)
                shortest_paths.add(shortest_path(S, E, h))
    return min(shortest_paths)


def reverse_shortest_path(E, h):
    MAX_PATH_LENGTH = len(h) * len(h[0])
    path_length = [[MAX_PATH_LENGTH] * len(h[i]) for i in range(len(h))]
    path_length[E[0]][E[1]] = 0
    check_list = {E}
    while check_list:
        point = check_list.pop()
        for a in adjacent(point, h):
            if ord(h[a[0]][a[1]]) >= ord(h[point[0]][point[1]]) - 1 and \
                    path_length[a[0]][a[1]] > path_length[point[0]][point[1]] + 1:
                path_length[a[0]][a[1]] = path_length[point[0]][point[1]] + 1
                check_list.add(a)
    return path_length


def puzzle24(input_file):
    data = fileHandle.readfile(input_file)
    h = [[ch for ch in line] for line in data.splitlines()]
    S, E = find_S_E(h)
    path_length = reverse_shortest_path(E, h)
    _shortest_path = len(h) * len(h[0])
    for i in range(len(h)):
        for j in range(len(h[i])):
            if h[i][j] == 'a' and path_length[i][j] < _shortest_path:
                _shortest_path = path_length[i][j]
    return _shortest_path


print('Day #12, Part One:', puzzle23('day12.txt'))
print('Day #12, Part Two:', puzzle24('day12.txt'))
