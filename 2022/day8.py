import fileHandle


def puzzle15(input_file='day8.txt'):
    data = fileHandle.readfile(input_file)
    h = [[int(ch) for ch in line] for line in data.splitlines()]
    visible = 2 * (len(h) + len(h[0])) - 4
    for y in range(1, len(h) - 1):
        for x in range(1, len(h[y]) - 1):
            row = h[y]
            col = [h[i][x] for i in range(len(h))]
            visible += h[y][x] > min([max(row[:x]), max(row[x + 1:]), max(col[:y]), max(col[y + 1:])])
    return visible


def puzzle16(input_file='day8.txt'):
    data = fileHandle.readfile(input_file)
    h = [[int(ch) for ch in line] for line in data.splitlines()]
    score = [[0] * len(h[0]) for y in range(len(h), )]
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
            score[y][x] = (x - xl) * (xr - x) * (y - yu) * (yd - y)
    max_score = 0
    for y in range(len(h)):
        for x in range(len(h[y])):
            max_score = max(max_score, score[y][x])
    return max_score
