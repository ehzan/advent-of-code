from fileHandle import readfile
import functools


def puzzle13(input_file='day7.txt'):
    data = readfile(input_file).split(',')
    crab_x = [int(x) for x in data]
    max_x = functools.reduce(lambda a, b: max(a, b), crab_x)
    nx = [0] * (max_x + 1)
    for x in crab_x:
        nx[x] += 1
    fuel = [0] * (max_x + 1)
    for x in range(max_x + 1):
        for i in range(max_x + 1):
            fuel[x] += nx[i] * abs(x - i)
        if x > 0 and fuel[x] > fuel[x - 1]:
            return x - 1, fuel[x - 1]
    else:
        return max_x, fuel[max_x]


def puzzle14(input_file='day7.txt'):
    data = readfile(input_file).split(',')
    crab_x = [int(x) for x in data]
    max_x = functools.reduce(lambda a, b: max(a, b), crab_x)
    fuel = [0] * (max_x + 1)
    for x in range(max_x + 1):
        for cx in crab_x:
            fuel[x] += abs(x - cx) * (abs(x - cx) + 1) // 2
        if x > 0 and fuel[x] > fuel[x - 1]:
            return x - 1, fuel[x - 1]
    else:
        return max_x, fuel[max_x]


def calc_g(nx):
    # g[x] = Sigma(i=0,x-1) nx[i] - Sigma(i=x,n) nx[i]
    g = [0] * len(nx)
    g[0] = -functools.reduce(lambda a, b: a + b, nx)
    for x in range(1, len(nx)):
        g[x] = g[x - 1] + 2 * nx[x - 1]
        if g[x] > 0:
            break
    return g[:x]


def f(x, nx, g):
    value = 0
    if x == 0:
        for i in range(len(nx)):
            value += i * nx[i]
    else:
        value = f(x - 1, nx, g) + g[x]
    return value


def puzzle13b(input_file='day7.txt'):
    data = readfile(input_file).split(',')
    crab_x = [int(x) for x in data]
    max_x = functools.reduce(lambda a, b: max(a, b), crab_x)
    nx = [0] * (max_x + 1)
    for x in crab_x:
        nx[x] += 1
    # g[x] = Σ(i=0,x-1) nx[i] - Σ(i=x,n) nx[i]
    g = calc_g(nx)
    best_x = len(g) - 1
    best_fuel = f(best_x, nx, g)
    return best_x, best_fuel
