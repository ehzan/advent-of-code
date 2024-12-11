import heapq
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
                offset, size = free_space
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


def puzzle18_slow(input_file: str) -> int:
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


def free_spaces_as_dict(free_spaces: list[list[tuple[int, int]]]) -> dict[int, list[int]]:
    free_dict = defaultdict(list)
    for free_space in free_spaces:
        free_dict[free_space[1]].append(free_space[0])
    for offset_list in free_dict.values():
        heapq.heapify(offset_list)
    return free_dict


def puzzle18(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    files, free_spaces = parse_input(data)

    free_dict = free_spaces_as_dict(free_spaces)

    for file_id in range(len(files) - 1, -1, -1):
        file = files[file_id]
        file_offset, file_size = file
        candidates = [(offset_list[0], free_size)
                      for free_size, offset_list in free_dict.items()
                      if free_size >= file_size and offset_list and offset_list[0] < file_offset]
        if candidates:
            (free_offset, free_size) = min(candidates)
            file[0] = free_offset
            heapq.heappop(free_dict[free_size])
            heapq.heappush(free_dict[free_size - file_size], free_offset + file_size)

    checksum = sum(file_id * (offset * size + size * (size - 1) // 2)
                   for file_id, [offset, size] in files.items())
    return checksum


if __name__ == '__main__':
    print('Day #9, part one:', puzzle17('./input/day9.txt'))
    print('Day #9, part two:', puzzle18('./input/day9.txt'))
