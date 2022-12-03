from fileHandle import readfile


def puzzle3(input_file='day2.txt'):
    data = readfile(input_file).split('\n')
    score = 0
    for c in data:
        score += ord(c[2]) - ord('X') + 1
        match ord(c[2]) - ord('X') - ord(c[0]) + ord('A'):
            case 0:
                score += 3
            case 1 | -2:
                score += 6
    return score


def puzzle4(input_file='day2.txt'):
    data = readfile(input_file).split('\n')
    score = 0
    for c in data:
        match c[2]:
            case 'X':
                score += 3 if c[0] == 'A' else ord(c[0]) - ord('A')
            case 'Y':
                score += 3 + ord(c[0]) - ord('A') + 1
            case 'Z':
                score += 6 + (1 if c[0] == 'C' else ord(c[0]) - ord('A') + 2)
    return score
