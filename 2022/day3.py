from fileHandle import readfile
from itertools import product


def puzzle5(input_file='day3.txt'):
    data = readfile(input_file).split('\n')
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

    p_sum = 0
    for item in items:
        p_sum += ord(item.lower()) - ord('a') + (27 if item.isupper() else 1)
    return p_sum


def puzzle6(input_file='day3.txt'):
    data = readfile(input_file).split('\n')
    items = []
    for i in range(0, len(data), 3):
        for x, y, z in product(data[i], data[i + 1], data[i + 2]):
            if x == y and y == z:
                items.append(x)
                break
                
    p_sum = 0
    for item in items:
        p_sum += ord(item.lower()) - ord('a') + (27 if item.isupper() else 1)
    return p_sum
