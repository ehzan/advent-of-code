from fileHandle import readfile
import re


def sign(number):
    return -1 if number < 0 else 1 if number > 0 else 0


def puzzle9(input_file='day5.txt'):
    data = readfile(input_file).split('\n')
    segments = []
    for line in data:
        coordinates = re.split(r' -> |,', line)
        p1 = {'x': int(coordinates[0]), 'y': int(coordinates[1])}
        p2 = {'x': int(coordinates[2]), 'y': int(coordinates[3])}
        segments.append([p1, p2])
    segments = list(filter(
        lambda p: p[0]['x'] == p[1]['x'] or p[0]['y'] == p[1]['y'],
        segments))
    # print(*segments, sep='\n')
    maxX, maxY = 0, 0
    for p in segments:
        maxX = max(maxX, p[0]['x'], p[1]['x'])
        maxY = max(maxY, p[0]['y'], p[1]['y'])
    # print(maxX, maxY)
    points = [[0] * (maxY + 1) for i in range(maxX + 1)]
    for p in segments:
        if p[0]['x'] == p[1]['x']:
            step = sign(p[1]['y'] - p[0]['y'])
            for y in range(p[0]['y'], p[1]['y'] + step, step):
                points[p[0]['x']][y] += 1
        elif p[0]['y'] == p[1]['y']:
            step = sign(p[1]['x'] - p[0]['x'])
            for x in range(p[0]['x'], p[1]['x'] + step, step):
                points[x][p[0]['y']] += 1
        # print(*points, sep='\n')
    cnt = 0
    for row in points:
        for p in row:
            cnt += (p > 1)
    return cnt


def puzzle10(input_file='day5.txt'):
    data = readfile(input_file).split('\n')
    segments = []
    for line in data:
        coordinates = re.split(r' -> |,', line)
        p1 = {'x': int(coordinates[0]), 'y': int(coordinates[1])}
        p2 = {'x': int(coordinates[2]), 'y': int(coordinates[3])}
        segments.append([p1, p2])
    segments = list(filter(
        lambda p: p[0]['x'] == p[1]['x'] or p[0]['y'] == p[1]['y'] or
                  abs(p[0]['x'] - p[1]['x']) == abs(p[0]['y'] - p[1]['y']),
        segments))
    # print(*segments, sep='\n')
    maxX, maxY = 0, 0
    for p in segments:
        maxX = max(maxX, p[0]['x'], p[1]['x'])
        maxY = max(maxY, p[0]['y'], p[1]['y'])
    # print(maxX, maxY)
    points = [[0] * (maxY + 1) for i in range(maxX + 1)]
    for p in segments:
        if p[0]['x'] == p[1]['x']:
            step = sign(p[1]['y'] - p[0]['y'])
            for y in range(p[0]['y'], p[1]['y'] + step, step):
                points[p[0]['x']][y] += 1
        elif p[0]['y'] == p[1]['y']:
            step = sign(p[1]['x'] - p[0]['x'])
            for x in range(p[0]['x'], p[1]['x'] + step, step):
                points[x][p[0]['y']] += 1
        elif p[0]['x'] - p[1]['x'] == p[0]['y'] - p[1]['y']:
            step = sign(p[1]['x'] - p[0]['x'])
            for x in range(p[0]['x'], p[1]['x'] + step, step):
                y = p[0]['y'] + x - p[0]['x']
                points[x][y] += 1
        elif p[0]['x'] - p[1]['x'] == -p[0]['y'] + p[1]['y']:
            step = sign(p[1]['x'] - p[0]['x'])
            for x in range(p[0]['x'], p[1]['x'] + step, step):
                y = p[0]['y'] - x + p[0]['x']
                points[x][y] += 1
        # print(*points, sep='\n')
    cnt = 0
    for row in points:
        for p in row:
            cnt += (p > 1)
    return cnt
