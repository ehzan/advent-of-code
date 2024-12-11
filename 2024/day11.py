from collections import defaultdict

import file_handle


def puzzle21(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    stones = map(int, data.split())

    stone_counts = defaultdict(int)
    for label in stones:
        stone_counts[label] += 1

    for _ in range(25):
        new_counts = defaultdict(int)
        for label in stone_counts.keys():
            if label == 0:
                new_counts[1] += stone_counts[0]
            elif len(label_str := str(label)) % 2 == 0:
                mid = len(label_str) // 2
                a, b = label_str[:mid], label_str[mid:]
                new_counts[int(a)] += stone_counts[label]
                new_counts[int(b)] += stone_counts[label]
            else:
                new_counts[label * 2024] += stone_counts[label]
        stone_counts = new_counts

    return sum(stone_counts.values())


def puzzle22(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    stones = map(int, data.split())

    stone_counts = defaultdict(int)
    for label in stones:
        stone_counts[label] += 1

    for _ in range(75):
        new_counts = defaultdict(int)
        for label in stone_counts.keys():
            if label == 0:
                new_counts[1] += stone_counts[0]
            elif len(label_str := str(label)) % 2 == 0:
                mid = len(label_str) // 2
                a, b = label_str[:mid], label_str[mid:]
                new_counts[int(a)] += stone_counts[label]
                new_counts[int(b)] += stone_counts[label]
            else:
                new_counts[label * 2024] += stone_counts[label]
        stone_counts = new_counts

    return sum(stone_counts.values())


if __name__ == '__main__':
    print('Day #11, part one:', puzzle21('./input/day11.txt'))
    print('Day #11, part two:', puzzle22('./input/day11.txt'))
