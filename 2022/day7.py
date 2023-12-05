import file_handle


def get_filesystem(terminal_output: list[str]) -> dict:
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


def puzzle13(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    dirs = get_filesystem(data.splitlines())
    return sum(size for size in dirs.values() if size < 100000)


def puzzle14(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    dirs = get_filesystem(data.splitlines())
    required_free_up = dirs['root'] - 40000000
    return min(size for size in dirs.values() if size > required_free_up)


if __name__ == '__main__':
    print('Day #7, part one:', puzzle13('./input/day7.txt'))
    print('Day #7, part two:', puzzle14('./input/day7.txt'))
