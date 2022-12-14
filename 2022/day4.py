import fileHandle, re


def puzzle7(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    pairs = [re.split(r',|-', pair) for pair in data]
    cnt = 0
    for sections in pairs:
        cnt += int(sections[0]) <= int(sections[2]) and int(sections[3]) <= int(sections[1]) or \
               int(sections[2]) <= int(sections[0]) and int(sections[1]) <= int(sections[3])
    return cnt


def puzzle8(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    pairs = [re.split(r',|-', pair) for pair in data]
    cnt = 0
    for sections in pairs:
        cnt += int(sections[0]) <= int(sections[2]) <= int(sections[1]) or \
               int(sections[2]) <= int(sections[0]) <= int(sections[3])
    return cnt


print('Day #4, Part One:', puzzle7('day4.txt'))
print('Day #4, Part Two:', puzzle8('day4.txt'))
