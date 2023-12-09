import functools
import re

import file_handle


def compare(val1: int | list, val2: int | list) -> int:
    if isinstance(val1, int) and isinstance(val2, int):
        return 1 if val1 < val2 else -1 if val1 > val2 else 0

    l1 = [val1] if isinstance(val1, int) else val1
    l2 = [val2] if isinstance(val2, int) else val2

    for item1, item2 in zip(l1, l2):
        if compare(item1, item2):  # i.e. cmp is 1 or -1
            return compare(item1, item2)

    return 1 if len(l1) < len(l2) else -1 if len(l1) > len(l2) else 0


def puzzle25(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    pairs = [map(eval, pair.splitlines()) for pair in data.split('\n\n')]

    right_ordered_pairs = [i + 1 for i, pair in enumerate(pairs) if compare(*pair) == 1]

    return sum(right_ordered_pairs)


def puzzle26(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    packets = re.split(r'\n+', data)
    packets = list(map(eval, packets))

    packets.extend([[[2]], [[6]], ])
    packets.sort(key=functools.cmp_to_key(compare), reverse=True)

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == '__main__':
    print('Day #13, part one:', puzzle25('./input/day13.txt'))
    print('Day #13, part two:', puzzle26('./input/day13.txt'))
