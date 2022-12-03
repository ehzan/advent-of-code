from fileHandle import *


def puzzle5(input_file='day3.txt'):
    numbers = readfile(input_file).split('\n')
    no1s = [0] * 12
    for num in numbers:
        for i in range(len(num)):
            no1s[i] += int(num[i])
    gamma = 0
    epsilon = 0
    for i in range(12):
        if no1s[i] > 500:
            gamma += pow(2, 11 - i)
        else:
            epsilon += pow(2, 11 - i)
    return gamma, epsilon, gamma * epsilon


def puzzle6(input_file='day3.txt'):
    numbers = readfile(input_file).split('\n')
    oxygen = numbers
    for i in range(12):
        zeros = []
        ones = []
        for item in oxygen:
            if item[i] == '0':
                zeros.append(item)
            else:
                ones.append(item)
        oxygen = zeros if len(zeros) > len(ones) else ones
    co2 = numbers
    for i in range(12):
        zeros = []
        ones = []
        for item in co2:
            if item[i] == '0':
                zeros.append(item)
            else:
                ones.append(item)
        co2 = zeros if len(zeros) <= len(ones) else ones
        if len(co2) == 1:
            break
    return oxygen, co2, int(oxygen[0], 2) * int(co2[0], 2)
