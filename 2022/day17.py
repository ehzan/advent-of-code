import fileHandle, re


def check_under(rock, x, y, chamber):
    # print(x, y)
    for pixel in rock:
        xu = pixel[0] + x
        yu = pixel[1] + y - 1
        if yu < len(chamber) and chamber[yu][xu] == 1:
            return True
    return False


def draw():
    print()
    for i in range(len(chamber) - 1, -1, -1):
        for j in chamber[i]:
            if j:
                print('#', end='')
            else:
                print('.', end='')
        print()


def in_range(x, y):
    return 0 <= x <= 6 and y < len(chamber)


def gas_push(rock, x, y):
    global g, gas
    g = (g + 1) % len(gas)

    if gas[g] == '<':
        for pixel in rock:
            if not (0 <= x - 1 + pixel[0] <= 6) or in_range(x - 1 + pixel[0], y + pixel[1]) and chamber[y + pixel[1]][
                x - 1 + pixel[0]] == 1:
                break
        else:
            x -= 1
    if gas[g] == '>':
        for pixel in rock:
            # print(x + 1 + pixel[0])
            if not (0 <= x + 1 + pixel[0] <= 6) or in_range(x + 1 + pixel[0], y + pixel[1]) and chamber[y + pixel[1]][
                x + 1 + pixel[0]] == 1:
                break
        else:
            x += 1
    return x


def down(shape):
    global top, g, gas, chamber
    x = 2
    y = top + 5
    rock_shapes = ['-', '+', '_|', '|', 'o']
    match rock_shapes[shape % len(rock_shapes)]:
        case '-':
            rock = [(0, 0), (1, 0), (2, 0), (3, 0)]
            width = 4
            height = 1
        case '+':
            rock = [(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)]
            width = 3
            height = 3
        case '_|':
            rock = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
            width = 3
            height = 3
        case '|':
            rock = [(0, 0), (0, 1), (0, 2), (0, 3)]
            width = 1
            height = 4
        case 'o':
            rock = [(0, 0), (1, 0), (0, 1), (1, 1)]
            width = 2
            height = 2

    while True:
        y -= 1
        x = gas_push(rock, x, y)
        if check_under(rock, x, y, chamber):
            for l in range(top + 1, y + height):
                chamber.append([0] * 7)
            top = max(top, y + height - 1)
            for pixel in rock:
                # print(pixel, x, y, top)
                chamber[y + pixel[1]][x + pixel[0]] = 1
            break


def puzzle33(input_file):
    data = fileHandle.readfile(input_file)
    global gas, g, chamber, top
    gas = data
    g = -1
    chamber = [[1] * 7]
    top, last_top = 0, 0
    added = [0] * (10000 // 5)
    for i in range(1600):
        down(i)
        if i + 1 in range(1600, 10000, 1725):
            # added[i // 5] = top - last_top
            print(top - last_top)
            last_top = top
    # for i in range(len(added) - 10):
    #     if added[i] == 13 and added[i + 1] == 10 and added[i + 2] == 6:
    #         print(i * 5)

    n = 1000000000000
    a = (n - 1600) // 1725
    b = (n - 431) % 1725
    print(n, a, b)
    ans = top + a * 2734
    return ans


print('Day #17, Part One:', puzzle33('day17.txt'))
# print('Day #17, Part One:', puzzle33('input.txt'))
