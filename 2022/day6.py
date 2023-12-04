import file_handle


def find_unique_substring(datastream: str, length: int) -> int | None:
    for i in range(len(datastream) - length + 1):
        substring = datastream[i:i + length]
        if len(set(substring)) == length:
            return i
    return None


def puzzle11(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    packet_offset = find_unique_substring(data, 4) + 4
    return packet_offset


def puzzle12(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    packet_offset = find_unique_substring(data, 4) + 4
    message_offset = find_unique_substring(data[packet_offset:], 14) + 14
    return packet_offset + message_offset


if __name__ == '__main__':
    print('Day #6, part one:', puzzle11('./input/day6.txt'))
    print('Day #6, part two:', puzzle12('./input/day6.txt'))
