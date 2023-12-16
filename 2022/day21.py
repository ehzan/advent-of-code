import operator

import file_handle

OPERATORS = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv, }


def parse_input(data: str) -> dict[str, list]:
    return {row.split(': ')[0]: row.split(': ')[1].split()
            for row in data.splitlines()}


def calc(var: str, equations: dict[str, list]) -> float:
    match equations[var]:
        case [number]:
            return int(number) if number else None
        case [var1, op, var2]:
            a = calc(var1, equations)
            b = calc(var2, equations)
            return OPERATORS[op](a, b) if a and b else None


def puzzle41(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    equations = parse_input(data)

    return int(calc('root', equations))


def puzzle42(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    equations = parse_input(data)

    equations['root'][1] = '-'
    equations['humn'] = [None]

    var, value = 'root', 0
    while var != 'humn':
        [var1, op, var2] = equations[var]
        val1 = calc(var1, equations)
        val2 = calc(var2, equations)
        (var, v, k) = (var2, val1, -1) if val1 else (var1, val2, 1)
        match op:
            case '+':
                value = value - v
            case '-':
                value = k * value + v
            case '*':
                value = value / v
            case '/':
                value = value ** k * v

    return int(value)


if __name__ == '__main__':
    print('Day #21, part one:', puzzle41('./input/day21.txt'))
    print('Day #21, part two:', puzzle42('./input/day21.txt'))
