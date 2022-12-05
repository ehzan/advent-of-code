from fileHandle import readfile


def is_lower(i, j, data):
    return (i == 0 or data[i][j] < data[i - 1][j]) and \
        (i == len(data) - 1 or data[i][j] < data[i + 1][j]) and \
        (j == 0 or data[i][j] < data[i][j - 1]) and \
        (j == len(data[i]) - 1 or data[i][j] < data[i][j + 1])


def puzzle17(input_file='day9.txt'):
    data = readfile(input_file).split('\n')
    _sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if is_lower(i, j, data):
                _sum += 1 + int(data[i][j])
    return _sum


def check_neighbors(check_list, basin, data):
    if len(check_list) == 0:
        return len(basin)

    pos = check_list.pop()
    i, j = pos[0], pos[1]
    if data[i][j] < '9':
        basin.add(pos)
        for neighbor in {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}:
            if 0 <= neighbor[0] < len(data) and \
                    0 <= neighbor[1] < len(data[neighbor[0]]) and \
                    not neighbor in basin:
                check_list.add(neighbor)
    return check_neighbors(check_list, basin, data)


def puzzle18(input_file='day9.txt'):
    data = readfile(input_file).split('\n')
    max1, max2, max3 = 0, 0, 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if is_lower(i, j, data):
                check_list = {(i, j)}
                basin = set()
                size = check_neighbors(check_list, basin, data)
                max3 = max(max3, size)
                max2, max3 = max(max2, max3), min(max2, max3)
                max1, max2 = max(max1, max2), min(max1, max2)

    return max1, max2, max3, max1 * max2 * max3
