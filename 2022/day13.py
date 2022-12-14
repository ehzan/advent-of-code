import fileHandle, re, functools


def compare(l1, l2):
    # print(l1, l2, l1.__class__, l2.__class__)
    if isinstance(l1, int) and isinstance(l2, int):
        return 1 if l1 < l2 else -1 if l1 > l2 else 0
    elif isinstance(l1, int):
        return compare([l1], l2)
    elif isinstance(l2, int):
        return compare(l1, [l2])
    for i in range(min(len(l1), len(l2), )):
        cmp = compare(l1[i], l2[i])
        if cmp: return cmp
    return 1 if len(l1) < len(l2) else -1 if len(l1) > len(l2) else 0


def puzzle25(input_file='day13.txt'):
    data = fileHandle.readfile(input_file).split('\n\n')
    right_order = []
    for i in range(len(data)):
        pair = data[i].splitlines()
        packet1 = eval(pair[0])
        packet2 = eval(pair[1])
        if compare(packet1, packet2) == 1:
            right_order.append(i + 1)
    # print(right_order)
    return sum(right_order)


def puzzle26(input_file='day13.txt'):
    data = fileHandle.readfile(input_file)
    data = re.split(r'\n+', data)
    packets = [eval(d) for d in data]
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=functools.cmp_to_key(compare), reverse=True)
    # print(*packets, sep='\n')
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
