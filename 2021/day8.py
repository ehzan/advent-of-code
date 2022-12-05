from fileHandle import readfile
import functools


def puzzle15(input_file='day8.txt'):
    data = readfile(input_file).split('\n')
    four_digits = [d.split(' | ')[1].split(' ') for d in data]
    cnt = 0
    for four_digit in four_digits:
        for digit in four_digit:
            cnt += len(digit) in {2, 3, 4, 7}
    return cnt


def mapping(ten_digits_str):
    _map = [{''}] * 10
    for digit in ten_digits_str.split(' '):
        match len(digit):
            case 2:
                _map[1] = set(digit)
            case 4:
                _map[4] = set(digit)
            case 3:
                _map[7] = set(digit)
            case 7:
                _map[8] = set(digit)
    for digit in ten_digits_str.split(' '):
        match len(digit):
            case 6:
                if set(_map[4]) < set(digit):
                    _map[9] = set(digit)
                elif set(_map[1]) < set(digit):
                    _map[0] = set(digit)
                else:
                    _map[6] = set(digit)
            case 5:
                if set(_map[1]) < set(digit):
                    _map[3] = set(digit)
                elif len(set(digit) - set(_map[4])) == 3:
                    _map[2] = set(digit)
                else:
                    _map[5] = set(digit)
    return _map


def puzzle16(input_file='day8.txt'):
    data = readfile(input_file).split('\n')
    _sum = 0
    for line in data:
        ten_digit_str = line.split(' | ')[0]
        four_digit_str = line.split(' | ')[1]
        _map = mapping(ten_digit_str)
        four_digit = [_map.index(set(digit)) for digit in four_digit_str.split(' ')]
        value = functools.reduce(lambda a, b: 10 * a + b, four_digit)
        _sum += value
    return _sum
