import time
from collections import defaultdict

import file_handle

NEIGHBORS = {
    'N': ((-1, -1), (0, -1), (1, -1)),
    'S': ((-1, 1), (0, 1), (1, 1)),
    'W': ((-1, -1), (-1, 0), (-1, 1)),
    'E': ((1, -1), (1, 0), (1, 1)),
}

NEIGHBORS_SET = set().union(*NEIGHBORS.values())


def parse_input(data: str) -> set[tuple]:
    occupied_cells = {(x, y) for y, row in enumerate(data.splitlines())
                      for x, cell in enumerate(row) if cell == '#'}
    return occupied_cells


def is_isolated(x: int, y: int, occupied_cells: set[tuple]) -> bool:
    for (dx, dy) in NEIGHBORS_SET:
        if (x + dx, y + dy) in occupied_cells:
            return False
    return True
    # not efficient: return not any((x + dx, y + dy) in occupied_cells for (dx, dy) in NEIGHBORS_SET)


def aim(x: int, y: int, occupied_cells: set[tuple], dirs: str) -> tuple | None:
    for d in dirs:
        for (dx, dy) in NEIGHBORS[d]:
            if (x + dx, y + dy) in occupied_cells:
                break
        # not efficient: if any((x + dx, y + dy) in occupied_cells for (dx, dy) in NEIGHBORS[d]): continue
        else:
            (dx, dy) = NEIGHBORS[d][1]
            return x + dx, y + dy

    return None


def spread(occupied_cells: set[tuple], dirs: str) -> bool:
    positions = defaultdict(list)
    for (x, y) in occupied_cells:
        if is_isolated(x, y, occupied_cells) or (the_aim := aim(x, y, occupied_cells, dirs)) is None:
            positions[(x, y)].append((x, y))
        else:
            positions[the_aim].append((x, y))

    occupied_cells.clear()
    settled = True
    for pos, propose_list in positions.items():
        if len(propose_list) == 1 and propose_list[0] != pos:
            occupied_cells.add(pos)
            settled = False
        else:
            occupied_cells.update(positions[pos])

    return not settled


def puzzle45(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    occupied_cells = parse_input(data)

    dirs = 'NSWE'
    for _ in range(10):
        spread(occupied_cells, dirs)
        dirs = dirs[1:] + dirs[:1]

    x_min, y_min = map(min, zip(*occupied_cells))
    x_max, y_max = map(max, zip(*occupied_cells))
    area = (y_max - y_min + 1) * (x_max - x_min + 1)

    return area - len(occupied_cells)


def puzzle46(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    occupied_cells = parse_input(data)

    dirs, i = 'NSWE', 1
    while spread(occupied_cells, dirs):
        dirs = dirs[1:] + dirs[:1]
        i += 1
    return i


if __name__ == '__main__':
    print('Day #23, part one:', puzzle45('./input/day23.txt'))
    timestamp = time.time()
    print('Day #23, part two:', puzzle46('./input/day23.txt'), f' (runtime: {round(time.time() - timestamp, 1)}s) ')
