import functools
import re
from collections import namedtuple

import file_handle

Record = namedtuple('Record', ('conditions', 'groups'))


def parse_input(data: str) -> list[Record[str, tuple]]:
    rows = [row.split() for row in data.splitlines()]
    return [Record(row[0], tuple(row[1].split(',')), )
            for row in rows]


@functools.cache
def count_arrangements(conditions: str, groups: tuple[int, ...]) -> int:
    if len(groups) == 0:
        return '#' not in conditions

    regex = f'(^|[.?])(?=[#?]{{%s}}[.?]*$)' % groups[-1]
    return sum(count_arrangements(conditions[:match.start()], groups[:-1])
               for match in re.finditer(regex, conditions))


def puzzle23(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    records = parse_input(data)

    return sum(count_arrangements(r.conditions, r.groups)
               for r in records)


def puzzle24(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    records = parse_input(data)

    return sum(count_arrangements('?'.join([r.conditions] * 5), r.groups * 5)
               for r in records)


if __name__ == '__main__':
    print('Day #12, part one:', puzzle23('./input/day12.txt'))
    print('Day #12, part two:', puzzle24('./input/day12.txt'))
