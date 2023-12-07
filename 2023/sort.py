import sys
import timeit


def exchange_sort(data: list):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]


def bubble_sort(data: list):
    i, swapped = len(data), True
    while swapped:
        i, swapped = i - 1, False
        for j in range(i):
            if data[j + 1] < data[j]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True


def insertion_sort(data: list):
    for i in range(1, len(data)):
        j, ai = i, data[i]
        while 0 <= (j := j - 1) and ai < data[j]:
            data[j + 1] = data[j]
        data[j + 1] = ai
