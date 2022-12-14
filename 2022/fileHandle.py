import re


def readfile(filename):
    path = re.sub(r'[^\\]+$', 'input\\\\' + filename, __file__)
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read().strip()
    return data
