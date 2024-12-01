import file_handle


def parse_input(data: str) -> tuple[list[int], list[int]]:
    rows = [map(int, row.split()) for row in data.splitlines()]
    arr1, arr2 = zip(*rows)
    return list(arr1), list(arr2)


def puzzle1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    arr1, arr2 = parse_input(data)

    return sum(abs(a - b) for a, b in zip(sorted(arr1), sorted(arr2), ))


def puzzle2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    arr1, arr2 = parse_input(data)

    return sum(n * arr2.count(n) for n in arr1)


if __name__ == '__main__':
    print('Day #1, part one:', puzzle1('./input/day1.txt'))
    print('Day #1, part two:', puzzle2('./input/day1.txt'))
