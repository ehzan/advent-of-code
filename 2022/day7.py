import fileHandle


def get_filesystem(terminal_output):
    path = ['root']
    dirs = {'root': 0, }
    terminal_output.append('$ cd /')
    for line in terminal_output:
        if line[0] == '$':
            match line:
                case '$ ls':
                    dirs['/'.join(path)] = 0
                case '$ cd ..':
                    size = dirs['/'.join(path)]
                    path.pop()
                    dirs['/'.join(path)] += size
                case '$ cd /':
                    while len(path) > 1:
                        size = dirs['/'.join(path)]
                        path.pop()
                        dirs['/'.join(path)] += size
                case other:
                    if other[:5] == '$ cd ':
                        path.append(line[5:])
        elif line[:3] != 'dir':
            size = int(line.split(' ')[0])
            dirs['/'.join(path)] += size

    return dirs


def puzzle13(input_file='day7.txt'):
    data = fileHandle.readfile(input_file).split('\n')
    dirs = get_filesystem(data)
    _sum = 0
    for path in dirs:
        _sum += dirs[path] * (dirs[path] < 100000)
    return _sum


def puzzle14(input_file='day7.txt'):
    data = fileHandle.readfile(input_file).split('\n')
    dirs = get_filesystem(data)
    needed_space = dirs['root'] - 40000000
    min_size = dirs['root']
    best_choice = 'root'
    for path in dirs:
        if needed_space < dirs[path] < min_size:
            min_size = dirs[path]
            best_choice = path
    return best_choice, dirs[best_choice]
