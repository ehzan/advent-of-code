import file_handle


def snafu2int(snafu: str) -> int:
    n = 0
    for ch in snafu:
        n = n * 5 + ('=-012'.index(ch) - 2)
    return n


def int2snafu(n: int) -> str:
    snafu = ''
    while not -2 <= n <= 2:
        n, m = divmod(n, 5)
        if 2 < m:
            m -= 5
            n += 1
        snafu = '=-012'[m + 2] + snafu
    snafu = '=-012'[n + 2] + snafu

    return snafu


def puzzle49(input_file: str) -> str:
    data = file_handle.readfile(input_file).strip()
    snafu_numbers = data.splitlines()

    sum_ = sum(snafu2int(snafu) for snafu in snafu_numbers)
    return int2snafu(sum_)


if __name__ == '__main__':
    print('Day #25, part one:', puzzle49('./input/day25.txt'))
