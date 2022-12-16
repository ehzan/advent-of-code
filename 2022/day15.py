import fileHandle, itertools, re


def get_sensors(data):
    sensors = []
    for line in data:
        Sx, Sy, Bx, By = map(int, re.findall(r'-?\d+', line))
        d = abs(Sx - Bx) + abs(Sy - By)
        sensors.append((Sx, Sy, d))
    return sensors


def join(segments):
    segments.sort()
    sg = segments[0]
    joined_segments = [sg]
    i = 1
    while i < len(segments):
        if segments[i][0] <= sg[1]:
            sg[1] = max(sg[1], segments[i][1])
        else:
            joined_segments.append(sg)
            sg = segments[i]
            joined_segments.append(sg)
        i += 1
    return joined_segments


def puzzle29(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    sensors = get_sensors(data)
    y = 2000000
    segments = []
    for s in sensors:
        d = s[2] - abs(y - s[1])
        if d >= 0:
            segments.append([s[0] - d, s[0] + d])
    joined_segments = join(segments)
    print(*joined_segments)
    segment_lengths = map(lambda sg: sg[1] - sg[0], joined_segments)
    return sum(segment_lengths)


def puzzle30(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    sensors = get_sensors(data)
    b, c = 0, 0
    for s1, s2 in itertools.product(sensors, sensors):
        x1, y1, d1 = s1
        x2, y2, d2, = s2
        # y=x+b
        b1 = y1 - x1 - d1
        b2 = y2 - x2 + d2
        if b1 == b2 + 2:
            b = b2 + 1
            print('y=x+', b, end=', ')
        # y=-x+c
        c1 = y1 + x1 - d1
        c2 = y2 + x2 + d2
        if c1 == c2 + 2:
            c = c2 + 1
            print('y=-x+', c, end=', ')
    y = (b + c) // 2
    x = (c - b) // 2
    print('(x,y) =', (x, y))
    return x * 4000000 + y


print('Day #15, Part One:', puzzle29('day15.txt'))
print('Day #15, Part Two:', puzzle30('day15.txt'))
