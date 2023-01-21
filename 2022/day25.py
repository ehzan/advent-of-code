import fileHandle


def parse_input(input_file):
    snafu_numbers = fileHandle.readfile(input_file).splitlines()
    return snafu_numbers


def int2base(n, base):
    sign = -1 if n < 0 else 1
    n *= sign
    digits = [] if n else ['0']
    while n:
        digits.append(str(n % base))
        n //= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)


def base2int(number, base):
    sign = -1 if number[0] == '-' else 1
    start = 1 if number[0] == '-' else 0
    n = 0
    for i in range(start, len(number)):
        n = n * base + int(number[i])
    return sign * n


def int2snafu(n):
    n5 = int2base(n, base=5)
    arr = list('0' + n5)
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] in ['3', '4', '5']:
            arr[i] = '=' if arr[i] == '3' else '-' if arr[i] == '4' else '0'
            arr[i - 1] = str(int(arr[i - 1]) + 1)
    if arr[0] == '0': arr.pop(0)
    return ''.join(arr)


def int2snafu2(n):
    m = len(int2base(n, base=5))
    med = n + base2int('2' * m, base=5)
    med5 = int2base(med, base=5)
    cipher = lambda d: '-' if d == -1 else '=' if d == -2 else str(d)
    snafu = '' if len(med5) == m else str(med5[0])
    for i in range(len(med5) - m, len(med5)):
        snafu += cipher(int(med5[i]) - 2)
    return snafu


def puzzle49(input_file):
    snafu_numbers = parse_input(input_file)
    decipher = lambda ch: -2 if ch == '=' else -1 if ch == '-' else int(ch)
    _sum = 0
    for snafu in snafu_numbers:
        med5 = [decipher(ch) for ch in snafu]
        _sum += base2int(med5, base=5)
    return int2snafu(_sum)


print('Day #25 Part One:', puzzle49('day25.txt'))
