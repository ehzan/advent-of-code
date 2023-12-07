from collections import namedtuple

import file_handle


def hand_type(hand: str, joker_rule=False) -> str:
    distinct_labels = set(list(hand))
    jokers = 0
    if joker_rule:
        distinct_labels.discard('J')
        jokers = hand.count('J')
    max_of_a_kind = max(0, 0, *map(hand.count, distinct_labels), ) + jokers

    match len(distinct_labels):
        case 0 | 1:
            return '5'
        case 2:
            return '4-1' if max_of_a_kind == 4 else '3-2'
        case 3:
            return '3-1-1' if max_of_a_kind == 3 else '2-2-1'
        case 4:
            return '2-1-1-1'
        case _:
            return '1-1-1-1-1'


def hand_value(hand: str, joker_rule=False) -> str:
    if joker_rule:
        hand = hand.replace('J', '0')

    label_value = lambda label: label if label.isdigit() else 'EDCBA'['AKQJT'.index(label)]
    return ''.join(map(label_value, list(hand)))


HandTuple = namedtuple('HandTuple', ('hand', 'bid'))


def puzzle13(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    hands = [HandTuple(*row.split()) for row in data.splitlines()]

    hands.sort(key=lambda hand: (hand_type(hand.hand), hand_value(hand.hand),))
    winning_amounts = [(i + 1) * int(hands[i].bid) for i in range(len(hands))]

    return sum(winning_amounts)


def puzzle14(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    hands = [HandTuple(*row.split()) for row in data.splitlines()]

    hands.sort(key=lambda hand: (hand_type(hand.hand, True), hand_value(hand.hand, True),))
    winning_amounts = [(i + 1) * int(hands[i].bid) for i in range(len(hands))]

    return sum(winning_amounts)


if __name__ == '__main__':
    print('Day #7, part one:', puzzle13('./input/day7.txt'))
    print('Day #7, part two:', puzzle14('./input/day7.txt'))
