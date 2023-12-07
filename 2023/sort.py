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


def selection_sort(data: list):
    for i in range(len(data)):
        idx_min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[idx_min]:
                idx_min = j
        data[i], data[idx_min] = data[idx_min], data[i]


def shell_sort(data: list):
    for gap in [701, 301, 132, 57, 23, 10, 4, 1]:  # Ciura gap sequence
        for i in range(gap, len(data)):
            j, ai = i, data[i]
            while 0 <= (j := j - gap) and ai < data[j]:
                data[j + gap], data[j] = data[j], data[j + gap]
            data[j + gap] = ai


def test():
    with open('./input/sort-data.txt', 'r', encoding='UTF-8') as f:
        sort_data = f.read().strip()

    the_data = list(map(int, sort_data.splitlines()))
    test_data = the_data.copy()
    test_data.sort()
    sys.setrecursionlimit(len(the_data))

    print('sorting algorithm \truntime(random / sorted data)')
    for func in [list.sort, exchange_sort, bubble_sort, insertion_sort, selection_sort,
                 shell_sort, ]:
        data = the_data.copy()

        t = timeit.timeit(stmt='func(data)', globals=locals(), number=1)
        print(f" •{func.__name__}    \t\t {round(t, 3)}", end='\t ')

        for i in range(0, len(test_data), 10000):
            assert data[i] == test_data[i]

        t = timeit.timeit(stmt='func(data)', globals=locals(), number=1)
        print(round(t, 3))

    print('(data size:', len(the_data), 'records)\n')


if __name__ == '__main__':
    test()
