import re

import file_handle


def max_color(color: str, game: str) -> int:
    counts = re.findall(rf'\d+(?= {color})', game)
    return max(map(int, counts))


def puzzle3(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    bounds = {'red': 12, 'green': 13, 'blue': 14}
    game_id = lambda game: int(re.search(r'\d+(?=:)', game)[0])

    return sum(game_id(game) for game in data.splitlines()
               if all(max_color(color, game) <= bounds[color] for color in bounds))


def puzzle4(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()

    return sum(max_color('red', game) * max_color('green', game) * max_color('blue', game)
               for game in data.splitlines())


if __name__ == '__main__':
    print('Day #2, part one:', puzzle3('./input/day2.txt'))
    print('Day #2, part two:', puzzle4('./input/day2.txt'))
