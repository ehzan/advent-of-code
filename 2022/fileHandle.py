import re


def readfile(filename):
    path = re.sub(r'[^\\]+$', filename, __file__)
    with open(path, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    return filedata[:-1]
