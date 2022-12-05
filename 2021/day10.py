import functools

from fileHandle import readfile


def couple(ch):
    _couple = {'(': ')', '[': ']', '{': '}', '<': '>'}
    if ch in _couple:
        return _couple[ch]
    else:
        return None


def puzzle19(input_file='day10.txt'):
    data = readfile(input_file).split('\n')
    score = 0
    value = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for line in data:
        stack = []
        for ch in line:
            if ch in {'(', '[', '{', '<'}:
                stack.append(ch)
            elif ch in {')', ']', '}', '>'}:
                if len(stack) == 0 or not couple(stack.pop()) == ch:
                    score += value[ch]
                    break
    return score


def puzzle20(input_file='day10.txt'):
    data = readfile(input_file).split('\n')
    scores = []
    value = {')': 1, ']': 2, '}': 3, '>': 4}
    for line in data:
        stack = []
        for ch in line:
            if ch in {'(', '[', '{', '<'}:
                stack.append(ch)
            elif ch in {')', ']', '}', '>'}:
                if len(stack) == 0 or not couple(stack.pop()) == ch:
                    break
        else:
            score = 0
            while len(stack) > 0:
                score = score * 5 + value[couple(stack.pop(), )]
            scores.append(score)

    scores.sort()
    return scores[len(scores) // 2]
