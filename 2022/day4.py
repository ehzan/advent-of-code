from fileHandle import readfile


def puzzle7(input_file='day4.txt'):
    data = readfile(input_file).split('\n')

    pairs = [d.split(',') for d in data]
    pairs = [[ids.split('-') for ids in pair] for pair in pairs]
    cnt = 0
    for elf in pairs:
        cnt += (int(elf[0][0]) <= int(elf[1][0])) and (int(elf[0][1]) >= int(elf[1][1])) or \
               (int(elf[0][0]) >= int(elf[1][0])) and (int(elf[0][1]) <= int(elf[1][1]))
    return cnt


def puzzle8(input_file='day4.txt'):
    data = readfile(input_file).split('\n')

    pairs = [d.split(',') for d in data]
    pairs = [[ids.split('-') for ids in pair] for pair in pairs]
    cnt = 0
    for elf in pairs:
        cnt += (int(elf[0][0]) <= int(elf[1][0])) and (int(elf[0][1]) >= int(elf[1][0])) or \
               (int(elf[0][0]) >= int(elf[1][0])) and (int(elf[0][0]) <= int(elf[1][1]))
    return cnt
