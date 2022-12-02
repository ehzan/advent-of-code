import re
from sys import argv


def puzzle1(filepath):
    print('===puzzle1===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = f.read()
    depth = data.split('\n')
    depth.pop()
    print(len(depth), depth[0], depth[len(depth) - 1])
    cnt = 0
    for i in range(len(depth) - 1):
        if int(depth[i]) < int(depth[i + 1]):
            cnt += 1
    return cnt


def puzzle2(filepath):
    print('===puzzle2===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = f.read()
    depth = data.split('\n')
    depth.pop()
    print(len(depth), depth[0], depth[len(depth) - 1])
    cnt = 0
    for i in range(len(depth) - 3):
        if int(depth[i]) < int(depth[i + 3]):
            cnt += 1
    return cnt


def puzzle3(filepath):
    print('===puzzle3===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = f.read()
    command = data.split('\n')
    command.pop()
    print(len(command), command[0], command[len(command) - 1])
    position = [0, 0]
    for i in range(len(command)):
        cmd = command[i].split(' ')
        if cmd[0] == 'forward':
            position[0] += int(cmd[1])
        elif cmd[0] == 'up':
            position[1] -= int(cmd[1])
        elif cmd[0] == 'down':
            position[1] += int(cmd[1])
    return position, position[0] * position[1]


def puzzle4(filepath):
    print('===puzzle4===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = f.read()
    command = data.split('\n')
    command.pop()
    print(len(command), command[0], command[len(command) - 1])
    position = [0, 0]
    aim = 0
    for i in range(len(command)):
        cmd = command[i].split(' ')
        if cmd[0] == 'forward':
            position[0] += int(cmd[1])
            position[1] += aim * int(cmd[1])
        elif cmd[0] == 'up':
            aim -= int(cmd[1])
        elif cmd[0] == 'down':
            aim += int(cmd[1])
    return position, position[0] * position[1]


def puzzle5(filepath):
    print('===puzzle5===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = f.read()
    numbers = data.split('\n')
    numbers.pop()
    print(len(numbers), numbers[0], numbers[len(numbers) - 1])
    no1s = [0] * 12
    for num in numbers:
        for i in range(len(num)):
            no1s[i] += int(num[i])
    gamma = 0
    epsilon = 0
    for i in range(12):
        if no1s[i] > 500:
            gamma += pow(2, 11 - i)
        else:
            epsilon += pow(2, 11 - i)
    return no1s, gamma, epsilon, gamma * epsilon


def puzzle6(filepath):
    print('===puzzle6===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = f.read()
    numbers = data.split('\n')
    numbers.pop()

    oxygen = numbers
    for i in range(12):
        zeros = []
        ones = []
        for item in oxygen:
            if item[i] == '0':
                zeros.append(item)
            else:
                ones.append(item)
        oxygen = zeros if len(zeros) > len(ones) else ones
    print(oxygen)

    co2 = numbers
    for i in range(12):
        zeros = []
        ones = []
        for item in co2:
            if item[i] == '0':
                zeros.append(item)
            else:
                ones.append(item)
        co2 = zeros if len(zeros) <= len(ones) else ones
        if len(co2) == 1: break;
    print(co2)

    return int(oxygen[0], 2) * int(co2[0], 2)


def search(number, board):
    for i in range(5):
        for j in range(5):
            if board[i][j]['value'] == number:
                board[i][j]['flag'] = True
                rowismarked = True
                columnismarked = True
                for k in range(5):
                    rowismarked &= board[i][k]['flag']
                    columnismarked &= board[k][j]['flag']
                return rowismarked or columnismarked
    return False


def puzzle7(filepath):
    print('===puzzle7===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n\n')
    numbers = data[0].split(',')
    boards = []
    for board in data[1:]:
        rows = board.split('\n')
        b = [re.split(' +', re.sub('^ *', '', row)) for row in rows]
        b = [[dict(value=col, flag=False) for col in row] for row in b]
        boards.append(b)

    for number in numbers:
        for board in boards:
            if search(number, board):
                print('found', *board, sep='\n')
                sum = 0
                for row in board:
                    for col in row:
                        sum += 0 if col['flag'] else int(col['value'])
                return int(number), sum, int(number) * sum
    return None


def puzzle8(filepath):
    print('===puzzle8===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n\n')
    numbers = data[0].split(',')
    print(*numbers)
    boards = []
    for board in data[1:]:
        rows = board.split('\n')
        b = [re.split(' +', re.sub('^ *', '', row)) for row in rows]
        b = [[dict(value=col, flag=False) for col in row] for row in b]
        boards.append(b)

    toberemoved = []
    for number in numbers:
        for board in toberemoved:
            boards.remove(board)
        toberemoved.clear()
        for board in boards:
            if search(number, board):
                if len(boards) == 1:
                    print('found', *board, sep='\n')
                    sum = 0
                    for row in board:
                        for col in row:
                            sum += 0 if col['flag'] else int(col['value'])
                    return int(number), sum, int(number) * sum
                toberemoved.append(board)
    return None


def puzzle9(filepath):
    print('===puzzle9===')
    with open(filepath, 'r', encoding='UTF-8') as f:
        filedata = f.read()
    data = filedata[:-1].split('\n')
    segments = []
    for line in data:
        l = re.split(r' -> |,', line)
        p1 = {'x': int(l[0]), 'y': int(l[1])}
        p2 = {'x': int(l[2]), 'y': int(l[3])}
        segments.append([p1, p2])
    segments = list(filter(lambda seg: seg[0]['x'] == seg[1]['x'] or seg[0]['y'] == seg[1]['y'], segments))
    # print(*segments, sep='\n')
    maxX = 0
    for seg in segments:
        maxX = max(maxX, seg[0]['x'], seg[1]['x'])
    print(maxX)
    points = [[]] * (maxX + 1)
    print(points)
    for seg in segments:
        if seg[0]['x'] == seg[1]['x']:
            print('x=', seg[0]['x'])
            y1 = min(seg[0]['y'], seg[1]['y'])
            y2 = max(seg[0]['y'], seg[1]['y'])
            for y in range(y1, y2 + 1):
                points[seg[0]['x']].append(y)
        elif seg[0]['y'] == seg[1]['y']:
            print('y=', seg[0]['y'])
            x1 = min(seg[0]['x'], seg[1]['x'])
            x2 = max(seg[0]['x'], seg[1]['x'])
            for x in range(x1, x2 + 1):
                points[x].append(seg[0]['y'])
    seen = set()
    for x in range(maxX):
        print(x)
        seen.clear()
        y_list = {y for y in points[x] if y in seen or seen.add(y)}
        print(y_list)

    # print(points)
    return None


def main():
    print('Answer #9:', puzzle9('day5.txt'), )
    return


if __name__ == '__main__':
    main()
