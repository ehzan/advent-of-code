import re

import file_handle


def custom_hash(string: str) -> int:
    return sum(17 ** (len(string) - i) * ord(ch) for i, ch in enumerate(string)) % 256


def puzzle29(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    return sum(map(custom_hash, data.split(',')))


def puzzle30(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    steps = re.findall(r'^|,(\w*)([-=])(\d?)', data)

    boxes = [{'labels': [], 'focal': []} for _ in range(256)]
    for (label, op, focal) in steps:
        box = boxes[custom_hash(label)]
        if label in box['labels']:
            i = box['labels'].index(label)
            if op == '=':
                box['focal'][i] = focal
            else:
                box['labels'].pop(i)
                box['focal'].pop(i)
        else:
            if op == '=':
                box['labels'].append(label)
                box['focal'].append(focal)

    return sum((i + 1) * (j + 1) * int(focal)
               for i, box in enumerate(boxes)
               for j, focal in enumerate(box['focal']))


if __name__ == '__main__':
    print('Day #15, part one:', puzzle29('./input/day15.txt'))
    print('Day #15, part two:', puzzle30('./input/day15.txt'))
