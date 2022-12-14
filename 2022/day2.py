import fileHandle


def puzzle3(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    score = 0
    for c in data:
        score += ord(c[2]) - ord('X') + 1
        match ord(c[2]) - ord('X') - ord(c[0]) + ord('A'):
            case 0:
                score += 3
            case 1 | -2:
                score += 6
    return score


def puzzle4(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    score = 0
    for c in data:
        match c[2]:
            case 'X':
                score += ord(c[0]) - ord('A') if c[0] != 'A' else 3
            case 'Y':
                score += 3 + ord(c[0]) - ord('A') + 1
            case 'Z':
                score += 6 + (ord(c[0]) - ord('A') + 2 if c[0] != 'C' else 1)
    return score


print('Day #2, Part One:', puzzle3('day2.txt'))
print('Day #2, Part Two:', puzzle4('day2.txt'))
