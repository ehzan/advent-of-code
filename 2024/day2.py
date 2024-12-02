import file_handle


def is_gradually_increasing(lst: list[int], differ: int = 3) -> bool:
    return all(lst[i] < lst[i + 1] <= lst[i] + differ
               for i in range(len(lst) - 1))


def is_safe(report: list[int]) -> bool:
    for i in range(len(report)):
        dampened_report = report[:i] + report[i + 1:]
        if is_gradually_increasing(dampened_report) or is_gradually_increasing(dampened_report[::-1]):
            return True
    return False


def puzzle3(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    reports = [list(map(int, row.split())) for row in data.splitlines()]

    return sum(is_gradually_increasing(report) or is_gradually_increasing(report[::-1])
               for report in reports)


def puzzle4(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    reports = [list(map(int, row.split())) for row in data.splitlines()]

    return sum(is_safe(report) for report in reports)


if __name__ == '__main__':
    print('Day #2, part one:', puzzle3('./input/day2.txt'))
    print('Day #2, part two:', puzzle4('./input/day2.txt'))
