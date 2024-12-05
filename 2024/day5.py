import file_handle


def merge_sort(l: list[int], orders: set[tuple[int, ...]]):
    size, n = 1, len(l)
    _l = l.copy()
    while size < n:
        for start in range(0, n, 2 * size):
            middle, end = min(start + size, n), min(start + 2 * size, n)
            i, j = start, middle
            for k in range(start, end):
                if j < end and (i == middle or (_l[j], _l[i]) in orders):
                    l[k] = _l[j]
                    j += 1
                else:
                    l[k] = _l[i]
                    i += 1
        _l = l.copy()
        size *= 2

    return l


def is_sorted(l: list[int], orders: set[tuple[int, ...]]) -> bool:
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if (l[j], l[i]) in orders:
                return False
    return True


def puzzle9(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    orders, lists = data.split('\n\n')
    orders = {tuple(map(int, row.split('|'))) for row in orders.splitlines()}
    lists = [list(map(int, row.split(','))) for row in lists.splitlines()]

    return sum(l[len(l) // 2] for l in lists if is_sorted(l, orders))


def puzzle10(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    orders, lists = data.split('\n\n')
    orders = {tuple(map(int, row.split('|'))) for row in orders.splitlines()}
    lists = [list(map(int, row.split(','))) for row in lists.splitlines()]

    return sum(merge_sort(l, orders)[len(l) // 2] for l in lists if not is_sorted(l, orders))


if __name__ == '__main__':
    print('Day #5, part one:', puzzle9('./input/day5.txt'))
    print('Day #5, part two:', puzzle10('./input/day5.txt'))
