import file_handle


def parse_input(data: str) -> set[tuple]:
    return {tuple(map(int, row.split(','))) for row in data.splitlines()}


DIRECTIONS = {
    (-1, 0, 0), (1, 0, 0),
    (0, -1, 0), (0, 1, 0),
    (0, 0, -1), (0, 0, 1),
}


def adjacency(cube: tuple[int, ...]) -> set[tuple]:
    (x, y, z) = cube
    return {(x + dx, y + dy, z + dz) for (dx, dy, dz) in DIRECTIONS}


def is_inside_boundary(cube: tuple[int, ...], bounds: list[tuple]) -> bool:
    return all(min_ <= cord <= max_
               for cord, min_, max_ in zip(cube, bounds[0], bounds[1], ))


def puzzle35(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    cubes = parse_input(data)

    exposed_sides = len(cubes) * 6
    for cube in cubes:
        for adjacent_cube in adjacency(cube):
            exposed_sides -= adjacent_cube in cubes
    return exposed_sides


def puzzle36(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    cubes = parse_input(data)

    bounds = [tuple(min(cords) - 1 for cords in zip(*cubes)),
              tuple(max(cords) + 1 for cords in zip(*cubes)), ]

    wet_sides = 0
    outside = {bounds[0]}
    visited = set()
    while outside:
        cube = outside.pop()
        if cube in visited:
            continue
        visited.add(cube)

        for adjacent_cube in adjacency(cube):
            if is_inside_boundary(adjacent_cube, bounds):
                if adjacent_cube in cubes:
                    wet_sides += 1
                else:
                    outside.add(adjacent_cube)

    return wet_sides


if __name__ == '__main__':
    print('Day #18, part one:', puzzle35('./input/day18.txt'))
    print('Day #18, part two:', puzzle36('./input/day18.txt'))
