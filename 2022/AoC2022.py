import re
from day1 import *


def readfile(filename):
    path = re.sub(r'[^\\]+$', filename, __file__)
    with open(path, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    return filedata[:-1]


def main():
    print('Answer #1:', puzzle1(), )
    print('Answer #2:', puzzle2(), )
    return


if __name__ == '__main__':
    main()
