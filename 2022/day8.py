import itertools

import file_handle


def is_visible(point: tuple[int, int], h: list[list[int]], ) -> bool:
    (x, y) = point
    if x in {0, len(h[0]) - 1} or y in {0, len(h) - 1}:
        return True
    row = h[y]
    col = [h[yi][x] for yi in range(len(h))]
    min_max = min(max(row[:x]), max(row[x + 1:]), max(col[:y]), max(col[y + 1:]))
    return h[y][x] > min_max


def calculate_scores(h: list[list[int]], ) -> list[list[int]]:
    n_rows, n_cols = len(h), len(h[0])
    scores = [[1] * n_cols for _ in range(n_rows)]
    for (x, y) in itertools.product(range(n_cols), range(n_rows)):
        row = h[y]
        col = [h[yi][x] for yi in range(n_rows)]
        views = {'left': row[x - 1::-1],
                 'right': row[x + 1:],
                 'up': col[y - 1::-1],
                 'down': col[y + 1:], }
        for key, view in views.items():
            i = -1
            for i, hi in enumerate(view):
                if hi >= h[y][x]:
                    break
            scores[y][x] *= (i + 1)

    return scores


def puzzle15(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    h = [list(map(int, row)) for row in data.splitlines()]

    visible_trees = [(x, y) for y in range(len(h)) for x in range(len(h[y]))
                     if is_visible((x, y), h)]
    return len(visible_trees)


def puzzle16(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    h = [list(map(int, row)) for row in data.splitlines()]

    scores = calculate_scores(h)
    return max(map(max, scores))


if __name__ == '__main__':
    print('Day #8, part one:', puzzle15('./input/day8.txt'))
    print('Day #8, part two:', puzzle16('./input/day8.txt'))
