import file_handle


def puzzle1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    food_lists = data.split('\n\n')

    max_ = 0
    for food_list in food_lists:
        calories = map(int, food_list.splitlines())
        max_ = max(max_, sum(calories))

    return max_


def puzzle2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    food_lists = data.split('\n\n')

    max1 = max2 = max3 = 0
    for food_list in food_lists:
        calories = map(int, food_list.splitlines())
        max3 = max(max3, sum(calories))
        if max2 < max3:
            max2, max3 = max3, max2
        if max1 < max2:
            max1, max2 = max2, max1

    return max1 + max2 + max3


if __name__ == '__main__':
    print('Day #1, part one:', puzzle1('./input/day1.txt'))
    print('Day #1, part two:', puzzle2('./input/day1.txt'))
