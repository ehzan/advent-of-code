import file_handle


def puzzle5(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rucksacks = data.splitlines()

    intersections = []
    for rucksack in rucksacks:
        middle = len(rucksack) // 2
        part1, part2 = rucksack[:middle], rucksack[middle:]
        common_items = set(part1) & set(part2)
        intersections.append(common_items.pop())

    priority = lambda ch: ord(ch.lower()) - ord('a') + 1 + 26 * ch.isupper()
    return sum(map(priority, intersections))


def puzzle6(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rucksacks = data.splitlines()

    intersections = []
    for i in range(0, len(rucksacks), 3):
        rucksack1, rucksack2, rucksack3 = rucksacks[i:i + 3]
        common_items = set(rucksack1) & set(rucksack2) & set(rucksack3)
        intersections.append(common_items.pop())

    priority = lambda ch: ord(ch.lower()) - ord('a') + 1 + 26 * ch.isupper()
    return sum(map(priority, intersections))


if __name__ == '__main__':
    print('Day #3, part one:', puzzle5('./input/day3.txt'))
    print('Day #3, part two:', puzzle6('./input/day3.txt'))
