import file_handle


def trails_from(start: tuple[int, int], heights: [list[int]]) -> list[list[tuple]]:
    x, y = start
    if heights[y][x] == 9:
        return [[start]]
    neighbors = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
    trails = []
    for (nx, ny) in neighbors:
        if 0 <= nx < len(heights[0]) and 0 <= ny < len(heights) and \
                heights[ny][nx] == heights[y][x] + 1:
            trails += [[(x, y)] + trail for trail in trails_from((nx, ny), heights)]
    return trails


def puzzle19(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    heights = [list(map(int, row)) for row in data.splitlines()]

    trailheads = [(x, y) for y in range(len(heights)) for x in range(len(heights[0]))
                  if heights[y][x] == 0]
    destinations = lambda trailhead: set(trail[-1] for trail in trails_from(trailhead, heights))

    return sum(len(destinations(trailhead)) for trailhead in trailheads)


def puzzle20(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    heights = [list(map(int, row)) for row in data.splitlines()]

    trailheads = [(x, y) for y in range(len(heights)) for x in range(len(heights[0]))
                  if heights[y][x] == 0]
    return sum(len(trails_from(trailhead, heights)) for trailhead in trailheads)


if __name__ == '__main__':
    print('Day #10, part one:', puzzle19('./input/day10.txt'))
    print('Day #10, part two:', puzzle20('./input/day10.txt'))
