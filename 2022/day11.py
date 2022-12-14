import fileHandle


def calculate(operand, operation):
    operand2 = operation.split(' ')[1]
    operand2 = operand if operand2 == 'old' else int(operand2)
    if operation[0] == '+':
        return operand + operand2
    elif operation[0] == '*':
        return operand * operand2
    else:
        return 'error'


def read_monkey_attributes(data):
    monkeys = []
    worry_level = []
    item = 0
    for p in data:
        lines = p.splitlines()
        id = int(lines[0][-2])
        items = []
        for level in lines[1].split('Starting items: ')[1].split(', '):
            items.append(item)
            worry_level.append(int(level))
            item += 1
        operation = lines[2].split('new = old ')[1]
        test_divisor = int(lines[3].split('divisible by ')[1])
        if_true = int(lines[4].split('throw to monkey ')[1])
        if_false = int(lines[5].split('throw to monkey ')[1])
        monkeys.append({'id': id, 'items': items, 'operation': operation, 'activity': 0,
                        'test_divisor': test_divisor, 'if_true': if_true, 'if_false': if_false, })
    return monkeys, worry_level


def puzzle21(input_file):
    data = fileHandle.readfile(input_file).split('\n\n')
    monkeys, worry_level = read_monkey_attributes(data)
    for round in range(20):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['activity'] += 1
                worry_level[item] = calculate(worry_level[item], monkey['operation']) // 3
                receiver = monkey['if_true'] if worry_level[item] % monkey['test_divisor'] == 0 \
                    else monkey['if_false']
                monkeys[receiver]['items'].append(item)
            monkey['items'].clear()
    activities = sorted([monkey['activity'] for monkey in monkeys])
    print(activities)
    return activities[-1] * activities[-2]


def puzzle22(input_file):
    data = fileHandle.readfile(input_file).split('\n\n')
    monkeys, worry_level = read_monkey_attributes(data)
    common_multiple = 1
    for monkey in monkeys:
        common_multiple *= monkey['test_divisor']
    for round in range(10000):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['activity'] += 1
                worry_level[item] = calculate(worry_level[item], monkey['operation']) % common_multiple
                receiver = monkey['if_true'] if worry_level[item] % monkey['test_divisor'] == 0 \
                    else monkey['if_false']
                monkeys[receiver]['items'].append(item)
            monkey['items'].clear()
    activities = sorted([monkey['activity'] for monkey in monkeys])
    print(activities)
    return activities[-1] * activities[-2]


print('Day #11, Part One:', puzzle21('day11.txt'))
print('Day #11, Part Two:', puzzle22('day11.txt'))
