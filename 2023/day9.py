import itertools

import file_handle


def extrapolate(sequence: list[int]) -> int:
    if len(set(sequence)) == 1:
        return sequence[0]

    diffs = [b - a for a, b in itertools.pairwise(sequence)]
    return sequence[-1] + extrapolate(diffs)


def puzzle17(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    sequences = [list(map(int, row.split())) for row in data.splitlines()]

    return sum(extrapolate(seq) for seq in sequences)


def puzzle18(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    sequences = [list(map(int, row.split())) for row in data.splitlines()]

    return sum(extrapolate(seq[::-1]) for seq in sequences)


if __name__ == '__main__':
    print('Day #9, part one:', puzzle17('./input/day9.txt'))
    print('Day #9, part two:', puzzle18('./input/day9.txt'))
