from fileHandle import readfile


def puzzle11(input_file='day6.txt'):
    data = readfile(input_file)
    for i in range(4, len(data) + 1):
        if len(set(data[i - 4:i])) == 4:
            return i
    return None


def puzzle12(input_file='day6.txt'):
    data = readfile(input_file)
    s = puzzle11(input_file)
    for i in range(s + 14, len(data) + 1):
        if len(set(data[i - 14:i])) == 14:
            return i
    return None
