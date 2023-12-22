import time

import file_handle


def is_safe(pos: tuple, t: int, weather_map: list[str]) -> bool:
    (x, y) = pos
    w, h = len(weather_map[0]), len(weather_map)
    if (x, y) in [(0, -1), (w - 1, h)]:
        return True

    return (0 <= x < w and 0 <= y < h) and \
        weather_map[y][(x - t) % w] != '>' and \
        weather_map[y][(x + t) % w] != '<' and \
        weather_map[(y - t) % h][x] != 'v' and \
        weather_map[(y + t) % h][x] != '^'


def shortest_time(start: tuple, end: tuple, weather_map: list[str], t0: int) -> int:
    next_positions, t = {start}, t0
    while True:
        t += 1
        current_positions = next_positions
        next_positions = set()

        for (x, y) in current_positions:
            if (x, y + 1) == end or (x, y - 1) == end:
                return t

            for pos in {(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}:
                if is_safe(pos, t, weather_map):
                    next_positions.add(pos)


def puzzle47(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    weather_map = [row[1:-1] for row in data.splitlines()[1:-1]]

    start = (0, -1)
    end = (len(weather_map[0]) - 1, len(weather_map))

    return shortest_time(start, end, weather_map, 0)


def puzzle48(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    weather_map = [row[1:-1] for row in data.splitlines()[1:-1]]

    start = (0, -1)
    end = (len(weather_map[0]) - 1, len(weather_map))

    time1 = shortest_time(start, end, weather_map, 0)
    time2 = shortest_time(end, start, weather_map, time1)
    total_time = shortest_time(start, end, weather_map, time2)
    return total_time


if __name__ == '__main__':
    print('Day #24, part one:', puzzle47('./input/day24.txt'))
    print('Day #24, part two:', puzzle48('./input/day24.txt'))
