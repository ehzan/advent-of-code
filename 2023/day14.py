import file_handle


def plot(rocks: list[list[str]]):
    for row in rocks:
        print(*row, sep='')
    print()


def calc_loads(rocks: list[list[str]]) -> int:
    return sum(row.count('O') * (len(rocks) - y) for y, row in enumerate(rocks))


def tilt_north(rocks: list[list[str]]):
    width, height = len(rocks[0]), len(rocks)
    slots = [0] * width

    for y in range(height):
        for x in range(width):
            if rocks[y][x] == '#':
                slots[x] = y + 1
            if rocks[y][x] == 'O':
                rocks[y][x] = '.'
                rocks[slots[x]][x] = 'O'
                slots[x] += 1


def spin(rocks: list[list[str]]) -> list[list[str]]:
    rotating_rocks = [row.copy() for row in rocks]  # deepcopy by hand (since copy.deepcopy(rocks) is not efficient)
    for _ in range(4):
        tilt_north(rotating_rocks)
        rotating_rocks = [list(col) for col in zip(*rotating_rocks[::-1])]  # rotates 90°
    return rotating_rocks


def puzzle27(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rocks = [list(row) for row in data.splitlines()]

    tilt_north(rocks)
    return calc_loads(rocks)


def puzzle28(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rocks = [list(row) for row in data.splitlines()]

    seen = []
    for i in range(1000000000):
        if rocks not in seen:
            seen.append(rocks)
            rocks = spin(rocks)
        else:
            index = seen.index(rocks)
            period = i - index
            rocks = seen[index + (1000000000 - index) % period]
            break

    return calc_loads(rocks)


if __name__ == '__main__':
    print('Day #14, part one:', puzzle27('./input/day14.txt'))
    print('Day #14, part two:', puzzle28('./input/day14.txt'))
