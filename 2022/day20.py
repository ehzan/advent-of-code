import time

import file_handle


def mix(lst: list[tuple], numbers: list[int]):
    n = len(lst)
    for item in enumerate(numbers):
        i = lst.index(item)
        lst.pop(i)
        j = (i + item[1]) % (n - 1)
        lst.insert(j, item)


def puzzle39(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    numbers = [int(d) for d in data.splitlines()]

    lst = list(enumerate(numbers))
    mix(lst, numbers)
    index0 = lst.index((numbers.index(0), 0))
    x, y, z = [lst[(index0 + offset) % len(lst)][1] for offset in [1000, 2000, 3000]]

    return x + y + z


def puzzle40(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    numbers = [811589153 * int(d) for d in data.splitlines()]

    lst = list(enumerate(numbers))
    for _ in range(10):
        mix(lst, numbers)
    index0 = lst.index((numbers.index(0), 0))
    x, y, z = [lst[(index0 + offset) % len(lst)][1] for offset in [1000, 2000, 3000]]

    return x + y + z


if __name__ == '__main__':
    print('Day #20, part one:', puzzle39('./input/day20.txt'))
    print('Day #20, part two:', puzzle40('./input/day20.txt'))
