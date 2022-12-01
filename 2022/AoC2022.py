import re
from sys import argv
import functools


def puzzle1(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n\n')
    max = 0
    for food_list in data:
        foods = food_list.split('\n')
        sum = functools.reduce(lambda a, b: int(a) + int(b), foods)
        sum = int(sum)
        if sum > max:
            max = sum
    return max


def puzzle2(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n\n')
    print('length:', len(data))
    max1 = 0
    max2 = 0
    max3 = 0
    for food_list in data:
        foods = food_list.split('\n')
        sum = functools.reduce(lambda a, b: int(a) + int(b), foods)
        sum = int(sum)
        if sum > max3:
            max3 = sum
            if max3 > max2:
                max2, max3 = max3, max2
            if max2 > max1:
                max1, max2 = max2, max1
    return max1 + max2 + max3


def main():
    print('Answer #1:', puzzle1('day1.txt'), )
    print('Answer #2:', puzzle2('day1.txt'), )
    return


if __name__ == '__main__':
    main()
