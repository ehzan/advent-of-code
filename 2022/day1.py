import fileHandle


def puzzle1(input_file):
    data = fileHandle.readfile(input_file).split('\n\n')
    _max = 0
    for food_list in data:
        calories = map(int, food_list.splitlines())
        calories = list(calories)  # because map is idiot
        _max = max(_max, sum(calories))
    return _max


def puzzle2(input_file):
    data = fileHandle.readfile(input_file).split('\n\n')
    max1, max2, max3 = 0, 0, 0
    for food_list in data:
        calories = map(int, food_list.splitlines())
        calories = list(calories)
        max3 = max(max3, sum(calories))
        if max2 < max3:
            max2, max3 = max3, max2
        if max1 < max2:
            max1, max2 = max2, max1
    print(max1, max2, max3)
    return max1 + max2 + max3


print('Day #1, Part One:', puzzle1('day1.txt'))
print('Day #1, Part Two:', puzzle2('day1.txt'))
