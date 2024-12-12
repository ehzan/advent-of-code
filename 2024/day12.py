from collections import defaultdict

import file_handle


def get_region(x: int, y: int, label: str, regions: dict[str, list[dict]]) \
        -> dict[str, int | set[tuple[int, int]]]:
    for region in regions[label]:
        if (x, y) in region['squares']:
            return region


def build_regions_dict(grid: list[str]) -> dict[str, list[dict]]:
    n = len(grid)
    assert n == len(grid[0])

    regions = defaultdict(list)

    for y in range(n):
        for x in range(n):
            label = grid[y][x]
            top = get_region(x, y - 1, label, regions) if 0 <= y - 1 and grid[y - 1][x] == label else None
            left = get_region(x - 1, y, label, regions) if 0 <= x - 1 and grid[y][x - 1] == label else None

            if top and left:
                sides_diff = -2 * (not (0 <= y - 1 and x + 1 < n and grid[y - 1][x + 1] == label))
                top['sides'] += sides_diff
                # top['perimeter'] += 0
                top['squares'].add((x, y))
                if top != left:
                    top['sides'] += left['sides']
                    top['perimeter'] += left['perimeter']
                    top['squares'].update(left['squares'])
                    regions[label].remove(left)
            elif top:
                sides_diff = 2 * (0 <= y - 1 and 0 <= x - 1 and grid[y - 1][x - 1] == label) + \
                             2 * (0 <= y - 1 and x + 1 < n and grid[y - 1][x + 1] == label)
                top['sides'] += sides_diff
                top['perimeter'] += 2
                top['squares'].add((x, y))
            elif left:
                sides_diff = 2 * (0 <= y - 1 and 0 <= x - 1 and grid[y - 1][x - 1] == label)
                left['sides'] += sides_diff
                left['perimeter'] += 2
                left['squares'].add((x, y))
            else:
                new_region = {'label': label, 'sides': 4, 'perimeter': 4, 'squares': {(x, y)}, }
                regions[label].append(new_region)

    return regions


def puzzle23(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()

    regions = build_regions_dict(grid)
    return sum(len(region['squares']) * region['perimeter']
               for region_list in regions.values() for region in region_list)


def puzzle24(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()

    regions = build_regions_dict(grid)
    return sum(len(region['squares']) * region['sides']
               for region_list in regions.values() for region in region_list)


if __name__ == '__main__':
    print('Day #12, part one:', puzzle23('./input/day12.txt'))
    print('Day #12, part two:', puzzle24('./input/day12.txt'))
