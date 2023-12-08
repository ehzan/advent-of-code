from collections import deque

import file_handle


def neighbors(point: tuple[int, int], heightmap: list[list[str]], ) -> set[tuple]:
    (x, y) = point
    adjacent_cells = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
    return {(x, y) for x, y in adjacent_cells
            if 0 <= y < len(heightmap) and 0 <= x < len(heightmap[y])}


def locate(label: str, heightmap: list[list[str]], ) -> tuple[int, int]:
    for y, row in enumerate(heightmap):
        if label in row:
            x = row.index(label)
            return x, y


def shortest_paths(start: tuple[int, int], heightmap: list[list[str]],
                   descending: bool = False) -> list[list[int]]:
    k = 1 - 2 * descending  # i.e., k = -1 if descending else 1
    path_lengths = [[-1] * len(heightmap[0]) for _ in range(len(heightmap))]
    path_lengths[start[1]][start[0]] = 0

    bfs_queue = deque([start])
    while bfs_queue:
        (px, py) = bfs_queue.popleft()
        for (nx, ny) in neighbors((px, py), heightmap):
            if path_lengths[ny][nx] == -1 and \
                    k * (ord(heightmap[ny][nx]) - ord(heightmap[py][px])) <= 1:
                path_lengths[ny][nx] = path_lengths[py][px] + 1
                bfs_queue.append((nx, ny))

    return path_lengths


def puzzle23(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    heightmap = [list(row) for row in data.splitlines()]

    (Sx, Sy) = locate('S', heightmap)
    (Ex, Ey) = locate('E', heightmap)
    heightmap[Sy][Sx] = 'a'
    heightmap[Ey][Ex] = 'z'
    path_lengths = shortest_paths((Sx, Sy), heightmap)

    return path_lengths[Ey][Ex]


def puzzle24(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    heightmap = [list(row) for row in data.splitlines()]

    (Sx, Sy) = locate('S', heightmap)
    (Ex, Ey) = locate('E', heightmap)
    heightmap[Sy][Sx] = 'a'
    heightmap[Ey][Ex] = 'z'
    path_lengths = shortest_paths((Ex, Ey), heightmap, descending=True)

    acceptable_lengths = [path_lengths[y][x] for y, row in enumerate(heightmap)
                          for x, height in enumerate(row)
                          if height == 'a' and path_lengths[y][x] != -1]

    return min(acceptable_lengths)


if __name__ == '__main__':
    print('Day #12, part one:', puzzle23('./input/day12.txt'))
    print('Day #12, part two:', puzzle24('./input/day12.txt'))
