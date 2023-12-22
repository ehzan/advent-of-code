import itertools
import re
from collections import namedtuple, defaultdict

import file_handle


def parse_input(data: str) -> list[dict]:
    bricks = re.findall(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)', data)
    bricks = [{'x': range(int(x1), int(x2) + 1),
               'y': range(int(y1), int(y2) + 1),
               'z': range(int(z1), int(z2) + 1),
               'underlying': set(),
               'overlying': set(), }
              for (x1, y1, z1, x2, y2, z2) in bricks]
    bricks.sort(key=lambda brick: brick['z'].start)

    return bricks


def bricks_fall(bricks: list[dict]):
    Top_Cube = namedtuple('TopCube', ('brick_index', 'z'))
    top_cubes = defaultdict(lambda: Top_Cube(-1, 0))

    for i, brick in enumerate(bricks):
        horizontal_surface = list(itertools.product(brick['x'], brick['y']))

        z_start = max(top_cubes[(x, y)].z for (x, y) in horizontal_surface) + 1
        brick['z'] = range(z_start, z_start + brick['z'].stop - brick['z'].start)

        for (x, y) in horizontal_surface:
            if 1 < brick['z'].start == top_cubes[(x, y)].z + 1:
                brick['underlying'].add(top_cubes[(x, y)].brick_index)
                bricks[top_cubes[(x, y)].brick_index]['overlying'].add(i)
            top_cubes[(x, y)] = Top_Cube(i, brick['z'].stop - 1)


def fall_count(index: int, falling_chain: set, bricks: list[dict]) -> int:
    for over in bricks[index]['overlying']:
        if not (bricks[over]['underlying'] - falling_chain):
            falling_chain.add(over)
            fall_count(over, falling_chain, bricks)
    return len(falling_chain)


def puzzle43(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    bricks = parse_input(data)
    bricks_fall(bricks)

    removable_bricks = [brick for brick in bricks
                        if all(len(bricks[i]['underlying']) > 1 for i in brick['overlying'])]
    return len(removable_bricks)


def puzzle44(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    bricks = parse_input(data)
    bricks_fall(bricks)

    fall_counts = [fall_count(b, {b}, bricks) - 1 for b in range(len(bricks))]
    return sum(fall_counts)


if __name__ == '__main__':
    print('Day #22, part one:', puzzle43('./input/day22.txt'))
    print('Day #22, part two:', puzzle44('./input/day22.txt'))
