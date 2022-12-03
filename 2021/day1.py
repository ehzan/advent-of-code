from fileHandle import *


def puzzle1(input_file='day1.txt'):
    depth = readfile(input_file).split('\n')
    cnt = 0
    for i in range(len(depth) - 1):
        if int(depth[i]) < int(depth[i + 1]):
            cnt += 1
    return cnt


def puzzle2(input_file='day1.txt'):
    depth = readfile(input_file).split('\n')
    cnt = 0
    for i in range(len(depth) - 3):
        if int(depth[i]) < int(depth[i + 3]):
            cnt += 1
    return cnt
