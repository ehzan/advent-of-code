import fileHandle, functools


def calc(typeId, operands):
    operators = {0: 'sum', 1: 'product', 2: 'min', 3: 'max', 5: '>', 6: '<', 7: '=='}
    operator = operators[typeId]
    match operator:
        case 'sum' | 'min' | 'max':
            return eval(operator + '(operands)')
        case 'product':
            return functools.reduce(lambda a, b: a * b, operands)
        case '>' | '<' | '==':
            return eval('operands[0]' + operator + 'operands[1]')


def parse_literal():
    global i
    literal = ''
    last = False
    while not last:
        last = (packet[i] == '0')
        literal += packet[i + 1:i + 5]
        i += 5
    return int(literal, base=2)


def parse_operator(typeId):
    global i
    operands = []
    match packet[i]:
        case '0':
            length_of_subpackets = int(packet[i + 1:i + 16], base=2)
            i += 16
            operands.clear()
            l = i + length_of_subpackets
            while i < l:
                operands.append(parse())
        case '1':
            numbers_of_subpackets = int(packet[i + 1:i + 12], base=2)
            i += 12
            operands.clear()
            for j in range(numbers_of_subpackets):
                operands.append(parse())
    return calc(typeId, operands)


def parse():
    global i, sum_of_versions
    version = int(packet[i:i + 3], base=2)
    sum_of_versions += version
    typeId = int(packet[i + 3:i + 6], base=2)
    i += 6
    if typeId == 4:
        return parse_literal()
    else:
        return parse_operator(typeId)


def puzzle31(input_file):
    data = fileHandle.readfile(input_file)
    global sum_of_versions
    sum_of_versions = 0
    global i, packet
    i = 0
    # packet = f'{int(data, base=16):0>{len(data) * 4}b}'
    packet = bin(int(data, base=16))[2:].zfill(len(data) * 4)
    parse()
    return sum_of_versions


def puzzle32(input_file):
    data = fileHandle.readfile(input_file)
    global i, packet
    i = 0
    packet = f'{int(data, base=16):0>{len(data) * 4}b}'
    return parse()
