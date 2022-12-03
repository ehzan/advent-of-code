from fileHandle import readfile
import functools


def puzzle1(input_file='day1.txt'):
    data = readfile(input_file).split('\n\n')
    themax = 0
    for food_list in data:
        foods = food_list.split('\n')
        # noinspection PyTypeChecker
        thesum = functools.reduce(lambda a, b: int(a) + int(b), foods)
        thesum = int(thesum)
        if thesum > themax:
            themax = thesum
    return themax


def puzzle2(input_file='day1.txt'):
    data = readfile(input_file).split('\n\n')
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
    return max1, max2, max3, max1 + max2 + max3
