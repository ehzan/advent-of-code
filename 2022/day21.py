import fileHandle


def parse_input(input_file):
    data = fileHandle.readfile(input_file).splitlines()
    monkeys = {line.split(': ')[0]: line.split(': ')[1] for line in data}
    return monkeys


def value(name, monkeys):
    if monkeys[name].isnumeric():
        return int(monkeys[name])
    a, op, b = monkeys[name].split(' ')
    return eval(f'{value(a, monkeys)} {op} {value(b, monkeys)}')


def puzzle41(input_file):
    monkeys = parse_input(input_file)
    return value('root', monkeys)


def puzzle42(input_file):
    monkeys = parse_input(input_file)
    monkeys['root'] = monkeys['root'].replace(monkeys['root'][5], '-')
    monkeys['humn'] = 'x'

    name, result = 'root', 0
    while name != 'humn':
        a, op, b = monkeys[name].split(' ')
        try:
            val = value(a, monkeys)
        except ValueError:
            val = value(b, monkeys)
            match op:
                case '+':
                    result = result - val
                case '-':
                    result = result + val
                case '*':
                    result = result / val
                case '/':
                    result = result * val
            name = a
        else:
            match op:
                case '+':
                    result = result - val
                case '-':
                    result = val - result
                case '*':
                    result = result / val
                case '/':
                    result = val / result
            name = b

    return result


print('Day #21 Part One:', puzzle41('day21.txt'))
print('Day #21 Part Two:', puzzle42('day21.txt'))
