import math
import re

import file_handle


def move_robots(robots: list[list[int]], nx: int, ny: int, time: int = 1):
    for robot in robots:
        (px, py, vx, vy) = robot
        robot[0] = (px + time * vx) % nx
        robot[1] = (py + time * vy) % ny


def plot_robots(robots: list[list[int]], nx: int, ny: int):
    plot = [[' '] * nx for _ in range(ny)]
    for x, y, _, _ in robots:
        plot[y][x] = '*'
    print('\n'.join(''.join(row) for row in plot))


def puzzle27(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    robots = [list(map(int, re.findall(r'[=,](-?\d+)', row)))
              for row in data.splitlines()]
    nx, ny = 101, 103  # nx, ny = 11, 7

    move_robots(robots, nx, ny, 100)
    robot_counts = [0, 0, 0, 0]
    for (px, py, _, _) in robots:
        if px != nx // 2 and py != ny // 2:
            quadrant = 2 * (py > ny // 2) + (px > nx // 2)
            robot_counts[quadrant] += 1

    return math.prod(robot_counts)


def puzzle28(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    robots = [list(map(int, re.findall(r'[=,](-?\d+)', row)))
              for row in data.splitlines()]
    nx, ny = 101, 103  # nx, ny = 11, 7

    time = 0
    while time := time + 1:
        move_robots(robots, nx, ny)
        positions = {(px, py) for (px, py, _, _) in robots}
        if len(positions) == len(robots):
            if __name__ == '__main__':
                plot_robots(robots, nx, ny)
            break

    return time


if __name__ == '__main__':
    print('Day #14, part one:', puzzle27('./input/day14.txt'))
    print('Day #14, part two:', puzzle28('./input/day14.txt'))
