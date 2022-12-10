import fileHandle


def shift(node, direction):
    vector = {'L': [-1, 0], 'R': [1, 0], 'U': [0, -1], 'D': [0, 1]}
    return [node[0] + vector[direction][0], node[1] + vector[direction][1]]


def pull(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail

    if tail[1] == head[1]:
        tail[0] = (head[0] + tail[0]) // 2
    elif tail[0] == head[0]:
        tail[1] = (head[1] + tail[1]) // 2
    else:
        tail[0] = (head[0] + tail[0]) // 2 if abs(head[0] - tail[0]) > 1 else head[0]
        tail[1] = (head[1] + tail[1]) // 2 if abs(head[1] - tail[1]) > 1 else head[1]
    return tail


def puzzle17(input_file='day9.txt'):
    data = fileHandle.readfile(input_file)
    steps = [(line.split(' ')[0], int(line.split(' ')[1])) for line in data.splitlines()]
    H = [0, 0]
    T = [0, 0]
    visited = {(T[0], T[1])}
    for step in steps:
        for i in range(step[1]):
            H = shift(H, step[0])
            pull(H, T)
            visited.add((T[0], T[1]))
    return len(set(visited))


def puzzle18(input_file='day9.txt'):
    data = fileHandle.readfile(input_file)
    steps = [(line.split(' ')[0], int(line.split(' ')[1])) for line in data.splitlines()]
    rope = [[0, 0] for i in range(10)]
    visited = {(rope[9][0], rope[9][1])}
    for step in steps:
        for i in range(step[1]):
            rope[0] = shift(rope[0], step[0])
            for j in range(1, 10):
                pull(rope[j - 1], rope[j])
            visited.add((rope[9][0], rope[9][1]))
    return len(set(visited))
