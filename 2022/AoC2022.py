# import re
import functools


def puzzle1(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n\n')
    themax = 0
    for food_list in data:
        foods = food_list.split('\n')
        # noinspection PyTypeChecker
        thesum = functools.reduce(lambda a, b: int(a) + int(b), foods)
        thesum = int(thesum)
        if thesum > themax:
            themax = thesum
    return themax


def puzzle2(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n\n')
    max1, max2, max3 = 0, 0, 0
    for food_list in data:
        foods = food_list.split('\n')
        # noinspection PyTypeChecker
        thesum = functools.reduce(lambda a, b: int(a) + int(b), foods)
        thesum = int(thesum)
        if thesum > max3:
            max3 = thesum
            if max3 > max2:
                max2, max3 = max3, max2
            if max2 > max1:
                max1, max2 = max2, max1
    return max1 + max2 + max3


def puzzle3(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n')
    score = 0
    for c in data:
        score += ord(c[2]) - ord('X') + 1
        match ord(c[2]) - ord('X') - ord(c[0]) + ord('A'):
            case 0:
                score += 3
            case 1 | -2:
                score += 6
    return score


def puzzle4(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n')
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


def main():
    # print('Answer #1:', puzzle1('day1.txt'), )
    # print('Answer #2:', puzzle2('day1.txt'), )
    # print('Answer #3:', puzzle3('day2.txt'), )
    # print('Answer #4:', puzzle4('day2.txt'), )
    return


if __name__ == '__main__':
    main()
