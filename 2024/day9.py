from collections import defaultdict

import file_handle


def parse_input(diskmap: str) -> tuple[dict[int, list], list[list]]:
    files = {}
    free_spaces = []
    offset = 0
    for index, size_str in enumerate(diskmap):
        if index % 2 == 0:
            files[index // 2] = [offset, int(size_str)]
        else:
            free_spaces.append([offset, int(size_str)])
        offset += int(size_str)

    return files, free_spaces


def puzzle17(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    files, free_spaces = parse_input(data)

    checksum = 0
    free_space_index = 0
    for file_id in range(len(files) - 1, -1, -1):
        file = files[file_id]
        for free_space in free_spaces[free_space_index:file_id]:
            if free_space[1] < file[1]:
                offset, size = free_space[0], free_space[1]
                checksum += file_id * (offset * size + size * (size - 1) // 2)
                file[1] -= size
                free_space_index += 1
            else:
                offset, size = free_space[0], file[1]
                checksum += file_id * (offset * size + size * (size - 1) // 2)
                file[1] = 0
                free_space[0] += size
                free_space[1] -= size
                break

    checksum += sum(file_id * (offset * size + size * (size - 1) // 2)
                    for file_id, [offset, size] in files.items())
    return checksum


def puzzle18(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    files, free_spaces = parse_input(data)

    for file_id in range(len(files) - 1, -1, -1):
        file = files[file_id]
        file_offset, file_size = file
        for free_space in free_spaces[:file_id]:
            if free_space[1] >= file_size:
                file[0] = free_space[0]
                free_space[0] += file_size
                free_space[1] -= file_size
                break

    checksum = sum(file_id * (offset * size + size * (size - 1) // 2)
                   for file_id, [offset, size] in files.items())

    return checksum


if __name__ == '__main__':
    print('Day #9, part one:', puzzle17('./input/day9.txt'))
    print('Day #9, part two:', puzzle18('./input/day9.txt'))
