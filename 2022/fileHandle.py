import re


def readfile(filename, strip=True):
    path = re.sub(r'[^\\]+$', 'input\\\\' + filename, __file__)
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()
    return data.strip() if strip else data
