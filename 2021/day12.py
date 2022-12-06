from fileHandle import readfile
import functools


def adjacents(node):
    adjacent_edges = [edge for edge in edges if node in edge]
    return functools.reduce(lambda a, b: a | b, adjacent_edges) - {node, 'start'}


def go_on(path, visited, flag):
    for adjacent in adjacents(path[-1]):
        if adjacent == 'end':
            valid_paths.append(path + ['end'])
        elif adjacent.isupper():
            go_on(path + [adjacent], visited, flag)
        elif adjacent.islower() and not adjacent in visited:
            go_on(path + [adjacent], visited | {adjacent}, flag)
        elif adjacent.islower() and adjacent in visited and flag:
            # visited.add(adjacent) <- bug because of by reference parameter passing
            go_on(path + [adjacent], visited, False)


def puzzle23(input_file='day12.txt'):
    data = readfile(input_file).split('\n')
    global edges, valid_paths
    edges = [set(line.split('-')) for line in data]
    valid_paths = []
    go_on(['start'], set(), False)
    return len(valid_paths)


def puzzle24(input_file='day12.txt'):
    data = readfile(input_file).split('\n')
    global edges, valid_paths
    edges = [set(line.split('-')) for line in data]
    valid_paths = []
    go_on(['start'], set(), True)
    return len(valid_paths)
