import fileHandle


def parse_input(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    numbers = [int(d) for d in data]
    return numbers


def mix_numbers(lst, numbers):
    n = len(lst)
    for order in range(n):
        i = lst.index((order, numbers[order]))
        item = lst[i]
        j = (i + lst[i][1]) % (n - 1)
        j = n - 1 if j == 0 else j
        if i <= j:
            lst = lst[:i] + lst[i + 1:j + 1] + [item] + lst[j + 1:]
        else:
            lst = lst[:j] + [item] + lst[j:i] + lst[i + 1:]
    return lst


def puzzle39(input_file):
    numbers = parse_input(input_file)
    l = list(enumerate(numbers))
    l = mix_numbers(l, numbers)
    n = len(l)
    i0 = next(index for index, item in enumerate(l) if item[1] == 0)
    x, y, z = l[(i0 + 1000) % n], l[(i0 + 2000) % n], l[(i0 + 3000) % n]
    print(x, y, z)
    return x[1] + y[1] + z[1]


def puzzle40(input_file):
    numbers = [num * 811589153 for num in parse_input(input_file)]
    l = list(enumerate(numbers))
    for _ in range(10):
        l = mix_numbers(l, numbers)
    n = len(l)
    i0 = next(index for index, item in enumerate(l) if item[1] == 0)
    x, y, z = l[(i0 + 1000) % n], l[(i0 + 2000) % n], l[(i0 + 3000) % n]
    return x[1] + y[1] + z[1]


print('Day #20 Part One:', puzzle39('day20.txt'))
print('Day #20 Part Two:', puzzle40('day20.txt'))
