import re

import fileHandle


def probe(velocity, target_area):
    step = 0
    x, y = 0, 0
    vx, vy = velocity
    while y >= target_area[3]:
        x += vx
        y += vy
        if target_area[0] <= x <= target_area[1] and target_area[2] <= y <= target_area[3]:
            return True
        vy -= 1
        vx += -1 if vx > 0 else 1 if vx < 0 else 0
    return False


def puzzle33(input_file):
    data = fileHandle.readfile(input_file)
    target_area = list(map(int, re.findall(r'-?\d+', data)), )
    print(target_area)
    probe(velocity, target_area)
