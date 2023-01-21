import fileHandle


def parse_input(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    cubes = [line.split(',') for line in data]
    cubes = [(int(c[0]) + 1, int(c[1]) + 1, int(c[2]) + 1) for c in cubes]
    return cubes


def are_adjacent(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2]) == 1


def puzzle35(input_file):
    cubes = parse_input(input_file)
    exposed_sides = 0
    for i in range(len(cubes)):
        exposed_sides += 6
        for j in range(0, i):
            if are_adjacent(cubes[i], cubes[j]):
                exposed_sides -= 2
    return exposed_sides


def adjacents(cube, cubes):
    if not hasattr(adjacents, 'max_x'):
        adjacents.max_x = max(cubes, key=lambda c: c[0])[0] + 1
    if not hasattr(adjacents, 'max_y'):
        adjacents.max_y = max(cubes, key=lambda c: c[1])[1] + 1
    if not hasattr(adjacents, 'max_z'):
        adjacents.max_z = max(cubes, key=lambda c: c[2])[2] + 1
    x, y, z = cube
    _adjacents = set()
    if 0 < x:
        _adjacents.add((x - 1, y, z))
    if x < adjacents.max_x:
        _adjacents.add((x + 1, y, z))
    if 0 < y:
        _adjacents.add((x, y - 1, z))
    if y < adjacents.max_y:
        _adjacents.add((x, y + 1, z))
    if 0 < z:
        _adjacents.add((x, y, z - 1))
    if z < adjacents.max_z:
        _adjacents.add((x, y, z + 1))

    return _adjacents


def puzzle36(input_file):
    cubes = parse_input(input_file)
    wet_sides = 0
    boundary = {(0, 0, 0)}
    reached = {(0, 0, 0)}
    while boundary:
        cube = boundary.pop()
        for a in adjacents(cube, cubes):
            if a not in reached:
                if a in cubes:
                    wet_sides += 1
                else:
                    boundary.add(a)
                    reached.add(a)
    return wet_sides


print('Day #18, Part One:', puzzle35('day18.txt'))
print('Day #18, Part Two:', puzzle36('day18.txt'))
