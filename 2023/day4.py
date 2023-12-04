import re
from collections import defaultdict

import file_handle


def puzzle7(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    total_points = 0
    for row in data.splitlines():
        card, winning_numbers, your_numbers = map(str.split, re.split(r': | \| ', row))
        matches_count = sum(your_numbers.count(number) for number in winning_numbers)
        total_points += 2 ** (matches_count - 1) if matches_count else 0

    return total_points


def puzzle8(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    card_count = defaultdict(lambda: 1)
    for row in data.splitlines():
        card, winning_numbers, your_numbers = map(str.split, re.split(r': | \| ', row))
        matches_count = sum(your_numbers.count(number) for number in winning_numbers)

        card_id = int(card[1])
        for i in range(card_id + 1, card_id + 1 + matches_count):
            card_count[i] += card_count[card_id]

    return sum(card_count.values())


if __name__ == '__main__':
    print('Day #4, part one:', puzzle7('./input/day4.txt'))
    print('Day #4, part two:', puzzle8('./input/day4.txt'))
