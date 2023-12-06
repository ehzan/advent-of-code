import file_handle


def update_screen(screen: list[chr], pixel_index: int, x: int):
    screen[pixel_index - 1] = '#' if x - 1 <= (pixel_index - 1) % 40 <= x + 1 else '.'


def plot(screen: list[chr]):
    for i, pixel in enumerate(screen):
        print(pixel * 2, end='')
        if (i + 1) % 40 == 0:
            print()


def puzzle19(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    instructions = data.splitlines()
    important_cycles = range(20, 221, 40)

    cycle, x = 0, 1
    signal_strengths = []
    for instruction in instructions:
        cycle += 1
        if cycle in important_cycles:
            signal_strengths.append(cycle * x)
        if instruction.startswith('addx'):
            cycle += 1
            if cycle in important_cycles:
                signal_strengths.append(cycle * x)
            x = x + int(instruction.split(' ')[1])

    return sum(signal_strengths)


def puzzle20(input_file: str) -> str:
    data = file_handle.readfile(input_file).strip()
    instructions = data.splitlines()

    cycle, x = 0, 1
    screen = ['*'] * 240
    for instruction in instructions:
        cycle += 1
        update_screen(screen, cycle, x)
        if instruction.startswith('addx'):
            cycle += 1
            update_screen(screen, cycle, x)
            x = x + int(instruction.split(' ')[1])

    if __name__ == '__main__':
        plot(screen)
    return 'RZHFGJCB'


if __name__ == '__main__':
    print('Day #10, part one:', puzzle19('./input/day10.txt'))
    print('Day #10, part two:', puzzle20('./input/day10.txt'))
