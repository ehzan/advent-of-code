import file_handle

VECTORS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1), }


def shift(point: tuple[int, int], direction: chr) -> tuple[int, int]:
    (x, y) = point
    (dx, dy) = VECTORS[direction]
    return x + dx, y + dy


def pull(head: tuple[int, int], tail: tuple[int, int], ) -> tuple[int, int]:
    (Hx, Hy), (Tx, Ty) = head, tail
    if abs(Hx - Tx) <= 1 and abs(Hy - Ty) <= 1:
        return tail

    (x, y) = tail
    if Ty == Hy:
        x = (Hx + Tx) // 2
    elif Tx == Hx:
        y = (Hy + Ty) // 2
    else:
        x = (Hx + Tx) // 2 if abs(Hx - Tx) > 1 else Hx
        y = (Hy + Ty) // 2 if abs(Hy - Ty) > 1 else Hy

    return x, y


def puzzle17(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    moves = [{'direction': row.split(' ')[0], 'steps': int(row.split(' ')[1])}
             for row in data.splitlines()]

    head = tail = (0, 0)
    visited = {tail}
    for move in moves:
        for _ in range(move['steps']):
            head = shift(head, move['direction'])
            tail = pull(head, tail)
            visited.add(tail)

    return len(visited)


def puzzle18(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    moves = [{'direction': row.split(' ')[0], 'steps': int(row.split(' ')[1])}
             for row in data.splitlines()]

    rope = [(0, 0)] * 10
    visited = {rope[-1]}
    for move in moves:
        for _ in range(move['steps']):
            rope[0] = shift(rope[0], move['direction'])
            for i in range(1, 10):
                rope[i] = pull(rope[i - 1], rope[i])
            visited.add(rope[-1])

    return len(visited)


if __name__ == '__main__':
    print('Day #9, part one:', puzzle17('./input/day9.txt'))
    print('Day #9, part two:', puzzle18('./input/day9.txt'))
