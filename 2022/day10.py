import fileHandle


def puzzle19(input_file):
    data = fileHandle.readfile(input_file)
    instructions = [line for line in data.splitlines()]
    cycle = 1
    x = 1
    _sum = 0
    for instruction in instructions:
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            _sum += cycle * x
        if instruction[:4] == 'addx':
            cycle += 1
            x = x + int(instruction.split(' ')[1])
            if cycle in [20, 60, 100, 140, 180, 220]:
                _sum += cycle * x
    return _sum


def draw(pixel, screen, x):
    screen[pixel] = '#' if pixel % 40 in [x - 1, x, x + 1] else '.'


def puzzle20(input_file):
    data = fileHandle.readfile(input_file)
    instructions = [line for line in data.splitlines()]
    screen = ['*'] * 240
    cycle = 1
    x = 1
    draw(cycle - 1, screen, x)
    for instruction in instructions:
        draw(cycle - 1, screen, x)
        cycle += 1
        if instruction[:4] == 'addx':
            draw(cycle - 1, screen, x)
            cycle += 1
            x = x + int(instruction.split(' ')[1])

    for i in range(len(screen)):
        print(screen[i] + screen[i], end='')
        if i + 1 in [40, 80, 120, 160, 200, 240]:
            print()
    return 'RZHFGJCB'


print('Day #10, Part One:', puzzle19('day10.txt'))
print('Day #10, Part Two:', puzzle20('day10.txt'))
