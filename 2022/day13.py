import fileHandle, re, functools


def compare(l1, l2):
    # print(l1, l2, l1.__class__, l2.__class__)
    if isinstance(l1, int) and isinstance(l2, int):
        return 1 if l1 < l2 else -1 if l1 > l2 else 0
    if isinstance(l1, int):  # and l2 is list
        l1 = [l1]
    if isinstance(l2, int):  # and l1 is list
        l2 = [l2]
    for i in range(min(len(l1), len(l2), )):
        cmp = compare(l1[i], l2[i])
        if cmp:  # i.e. cmp==1 or -1
            return cmp
    return 1 if len(l1) < len(l2) else -1 if len(l1) > len(l2) else 0


def puzzle25(input_file):
    data = fileHandle.readfile(input_file).split('\n\n')
    right_orders = []
    for i in range(len(data)):
        packet1, packet2 = map(eval, data[i].splitlines())
        if compare(packet1, packet2) == 1:
            right_orders.append(i + 1)
    # print(right_order)
    return sum(right_orders)


def puzzle26(input_file):
    data = fileHandle.readfile(input_file)
    data = re.split(r'\n+', data)
    packets = list(map(eval, data))  # i.e. packets=[eval(d) for d in data]
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=functools.cmp_to_key(compare), reverse=True)
    # print(*packets, sep='\n')
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


print('Day #13, Part One:', puzzle25('day13.txt'))
print('Day #13, Part Two:', puzzle26('day13.txt'))
