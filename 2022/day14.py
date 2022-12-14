import fileHandle


def scan_cave(data):
    cave = [[0] * 1000 for i in range(1000)]
    max_y = 0
    for line in data:
        points = line.split(' -> ')
        for i in range(len(points) - 1):
            x1, y1 = map(int, points[i].split(','))
            x2, y2 = map(int, points[i + 1].split(','))
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cave[x1][y] = 1
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    cave[x][y1] = 1
            max_y = max(max_y, y1, y2)
    return cave, max_y


def pour_sand(cave, max_y):
    x, y = 500, 0
    while y < max_y and cave[x][y + 1] * cave[x - 1][y + 1] * cave[x + 1][y + 1] == 0:
        if cave[x][y + 1] == 0:
            y += 1
        elif cave[x - 1][y + 1] == 0:
            x, y = x - 1, y + 1
        elif cave[x + 1][y + 1] == 0:
            x, y = x + 1, y + 1
    cave[x][y] = 1
    return x, y


def puzzle27(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    cave, max_y = scan_cave(data)
    sand = 0
    y = 0
    while y < max_y:
        sand += 1
        x, y = pour_sand(cave, max_y)
    return sand - 1


def puzzle28(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    cave, max_y = scan_cave(data)
    max_y += 2
    for x in range(1000):
        cave[x][max_y] = 1
    sand = 0
    y = True
    while y:
        sand += 1
        x, y = pour_sand(cave, max_y)
    return sand


print('Day #14, Part One:', puzzle27('day14.txt'))
print('Day #14, Part Two:', puzzle28('day14.txt'))
