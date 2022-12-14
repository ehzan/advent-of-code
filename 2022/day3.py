import fileHandle, itertools


def puzzle5(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    items = []
    for rucksack in data:
        n = int(len(rucksack) / 2)
        part1 = rucksack[:n]
        part2 = rucksack[n:]
        for x in part1:
            for y in part2:
                if x == y:
                    items.append(x)
                    break
            else:
                continue
            break

    _sum = 0
    for l in items:
        _sum += ord(l.lower()) - ord('a') + (27 if l.isupper() else 1)
    return _sum


def puzzle6(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    items = []
    for i in range(0, len(data), 3):
        for x, y, z in itertools.product(data[i], data[i + 1], data[i + 2]):
            if x == y and y == z:
                items.append(x)
                break

    _sum = 0
    for l in items:
        _sum += ord(l.lower()) - ord('a') + (27 if l.isupper() else 1)
    return _sum


print('Day #3, Part One:', puzzle5('day3.txt'))
print('Day #3, Part Two:', puzzle6('day3.txt'))
