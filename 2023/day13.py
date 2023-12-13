import file_handle


def find_mirror(pattern: list[str], smudged: bool = False) -> int:
    for mirror in range(1, len(pattern)):
        upper_segment = pattern[:mirror][::-1]
        lower_segment = pattern[mirror:]
        if matrix_diff(upper_segment, lower_segment) == smudged:
            return mirror
    return 0


def matrix_diff(matrix1: list, matrix2: list) -> int:
    diff = 0
    for row1, row2 in zip(matrix1, matrix2):
        diff += sum(a != b for a, b in zip(row1, row2))
        if diff > 1:
            break
    return diff


def puzzle25(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    patterns = [part.splitlines() for part in data.split('\n\n')]

    return sum(100 * find_mirror(pattern) + find_mirror([*zip(*pattern)])
               for pattern in patterns)


def puzzle26(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    patterns = [part.splitlines() for part in data.split('\n\n')]

    return sum(100 * find_mirror(pattern, True) + find_mirror([*zip(*pattern)], True)
               for pattern in patterns)


if __name__ == '__main__':
    print('Day #13, part one:', puzzle25('./input/day13.txt'))
    print('Day #13, part two:', puzzle26('./input/day13.txt'))
