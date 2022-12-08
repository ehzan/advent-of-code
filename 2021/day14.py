import fileHandle
import collections


def step(polymer, rules):
    for pair in rules:
        polymer = polymer.replace(pair, pair[0] + rules[pair].lower() + pair[1])
        polymer = polymer.replace(pair, pair[0] + rules[pair].lower() + pair[1])
    return polymer.upper()


def puzzle27(input_file='day14.txt'):
    data = fileHandle.readfile(input_file).split('\n\n')
    polymer = data[0]
    rules = {l[0:2]: l[-1] for l in data[1].splitlines()}
    steps = 10
    for i in range(steps):
        polymer = step(polymer, rules)
    frequency = collections.Counter(polymer)
    least_frequent = min(frequency, key=frequency.get)
    most_frequent = max(frequency, key=frequency.get)
    print(least_frequent, frequency[least_frequent], most_frequent, frequency[most_frequent], )

    return frequency[most_frequent] - frequency[least_frequent]


def step2(pairs, rules):
    new_pairs = pairs.copy()
    for key in rules:
        key1 = key[0] + rules[key]
        key2 = rules[key] + key[1]
        number = pairs[key] if key in pairs else 0
        new_pairs.setdefault(key, 0)
        new_pairs.setdefault(key1, 0)
        new_pairs.setdefault(key2, 0)
        new_pairs[key] -= number
        new_pairs[key1] += number
        new_pairs[key2] += number
    return new_pairs


def puzzle28(input_file='day14.txt'):
    data = fileHandle.readfile(input_file).split('\n\n')
    polymer = data[0]
    rules = {l[0:2]: l[-1] for l in data[1].splitlines()}
    pairs = {}
    for i in range(len(polymer) - 1):
        key = polymer[i:i + 2]
        pairs[key] = pairs[key] + 1 if key in pairs else 1
    steps = 40
    for i in range(steps):
        pairs = step2(pairs, rules)

    frequency = {key[0]: 0 for key in pairs}
    for key in pairs:
        frequency[key[0]] += pairs[key]
    frequency[polymer[-1]] += 1
    least_frequent = min(frequency, key=frequency.get)
    most_frequent = max(frequency, key=frequency.get)
    print(least_frequent, frequency[least_frequent], most_frequent, frequency[most_frequent], )

    return frequency[most_frequent] - frequency[least_frequent]
