import fileHandle


def puzzle15(input_file):
    data = fileHandle.readfile(input_file)
    h = [[int(ch) for ch in line] for line in data.splitlines()]
    visible = 2 * (len(h) + len(h[0])) - 4
    for y in range(1, len(h) - 1):
        for x in range(1, len(h[y]) - 1):
            row = h[y]
            col = [h[i][x] for i in range(len(h))]
            visible += h[y][x] > min(max(row[:x]), max(row[x + 1:]), max(col[:y]), max(col[y + 1:]))
    return visible


def calculate_scores(h):
    scores = [[0] * len(h[0]) for y in range(len(h), )]
    for y in range(1, len(h) - 1):
        for x in range(1, len(h[y]) - 1):
            row = h[y]
            col = [h[i][x] for i in range(len(h))]
            xl, xr, yu, yd = x - 1, x + 1, y - 1, y + 1
            while xl > 0 and row[xl] < h[y][x]:
                xl -= 1
            while xr < len(row) - 1 and row[xr] < h[y][x]:
                xr += 1
            while yu > 0 and col[yu] < h[y][x]:
                yu -= 1
            while yd < len(col) - 1 and col[yd] < h[y][x]:
                yd += 1
            scores[y][x] = (x - xl) * (xr - x) * (y - yu) * (yd - y)
    return scores


def puzzle16(input_file):
    data = fileHandle.readfile(input_file)
    h = [[int(ch) for ch in line] for line in data.splitlines()]
    scores = calculate_scores(h)
    max_score_of_rows = map(max, scores)
    return max(max_score_of_rows)


print('Day #8, Part One:', puzzle15('day8.txt'))
print('Day #8, Part Two:', puzzle16('day8.txt'))
