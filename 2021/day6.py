from fileHandle import readfile


def folk_no(days):
    return folk_no(days - 7) + folk_no(days - 9) if days > 0 else 1


def puzzle11(input_file='day6.txt'):
    data = readfile(input_file).split(',')
    days = 80
    no = 0
    for fish_time in data:
        no += folk_no(days - int(fish_time))
    return no


def puzzle12(input_file='day6.txt'):
    data = readfile(input_file).split(',')
    days = 256
    folk_n = [0] * (days + 1)
    for d in range(1, 8):
        folk_n[d] = 2
    folk_n[0], folk_n[8], folk_n[9] = 1, 3, 3
    for d in range(10, days + 1):
        folk_n[d] = folk_n[d - 7] + folk_n[d - 9]
    no = 0
    for fish_time in data:
        no += folk_n[days - int(fish_time)]
    return no
