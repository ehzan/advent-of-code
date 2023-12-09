import file_handle

SOURCE_X, SOURCE_Y = 500, 0


def pares_input(data: str) -> list[list[int]]:
    rocks = [[tuple(map(int, point.split(','))) for point in row.split(' -> ')]
             for row in data.splitlines()]

    max_y = max(point[1] for rock in rocks for point in rock)
    cave = [[0] * (SOURCE_X + max_y + 3) for _ in range(max_y + 1)]
    for rock in rocks:
        for (x1, y1), (x2, y2) in zip(rock, rock[1:]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cave[y][x1] = 1
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    cave[y1][x] = 1

    return cave


def pour_sand(cave: list[list[int]]) -> int:
    sx, sy = SOURCE_X, SOURCE_Y
    for sy in range(len(cave) - 1):
        if not cave[sy + 1][sx]:
            continue
        elif not cave[sy + 1][sx - 1]:
            sx -= 1
        elif not cave[sy + 1][sx + 1]:
            sx += 1
        else:
            cave[sy][sx] = 1
            return sy

    return sy + 1


def puzzle27(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    cave = pares_input(data)

    sands = 0
    while pour_sand(cave) < len(cave) - 1:
        sands += 1

    return sands


def puzzle28(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    cave = pares_input(data)
    cave.extend([[0] * len(cave[0]), [1] * len(cave[0])])

    sands = 0
    while pour_sand(cave) > SOURCE_Y:
        sands += 1

    return sands + 1


if __name__ == '__main__':
    print('Day #14, part one:', puzzle27('./input/day14.txt'))
    print('Day #14, part two:', puzzle28('./input/day14.txt'))
