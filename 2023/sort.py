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


def quick_sort(data: list, start: int = 0, end: int = None):
    end = len(data) if end is None else end
    if end - start <= 1:
        return

    pivot = data[end - 1]
    i = start
    for j in range(start, end - 1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1

    data[i], data[end - 1] = data[end - 1], data[i]
    quick_sort(data, start, i)
    quick_sort(data, i + 1, end)


def heap_sort(data: list):
    def sift_down(heap: list, root: int, last: int):
        while (child := 2 * root + 1) <= last:
            if child + 1 <= last and heap[child] < heap[child + 1]:
                child = child + 1
            if heap[child] <= heap[root]:
                break
            heap[root], heap[child] = heap[child], heap[root]
            root = child

    last = len(data) - 1
    for start in range(last // 2, -1, -1):  # heapify
        sift_down(data, start, last)

    while 0 < last:
        data[0], data[last] = data[last], data[0]
        last = last - 1
        sift_down(data, 0, last)


def merge_sort_simple(data: list):
    if len(data) <= 1:
        return

    middle = len(data) // 2
    merge_sort_simple(L := data[:middle])
    merge_sort_simple(R := data[middle:])

    data.clear()
    i, j = 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            data.append(L[i])
            i += 1
        else:
            data.append(R[j])
            j += 1
    data += L[i:] + R[j:]


def merge_sort_topdown(data: list):
    def split_merge(A: list, start: int, end: int, data: list):
        if end - start <= 1:
            return
        middle = (start + end) // 2
        split_merge(data, start, middle, A)
        split_merge(data, middle, end, A)
        i, j = start, middle
        for k in range(start, end):
            if i < middle and (j == end or A[i] < A[j]):
                data[k] = A[i]
                i += 1
            else:
                data[k] = A[j]
                j += 1

    split_merge(data.copy(), 0, len(data), data)


def merge_sort_bottomup(data: list):
    size, n = 1, len(data)
    A = data.copy()
    while size < n:
        for start in range(0, n, 2 * size):
            middle, end = min(start + size, n), min(start + 2 * size, n)
            i, j = start, middle
            for k in range(start, end):
                if i < middle and (j == end or A[i] < A[j]):
                    data[k] = A[i]
                    i += 1
                else:
                    data[k] = A[j]
                    j += 1
        A = data.copy()
        size *= 2


def test():
    with open('./input/sort-data.txt', 'r', encoding='UTF-8') as f:
        sort_data = f.read().strip()

    the_data = list(map(int, sort_data.splitlines()))
    test_data = the_data.copy()
    test_data.sort()
    sys.setrecursionlimit(len(the_data))

    print('sorting algorithm \truntime(random / sorted data)')
    for func in [list.sort, exchange_sort, bubble_sort, insertion_sort, selection_sort,
                 shell_sort, quick_sort, heap_sort,
                 merge_sort_simple, merge_sort_topdown, merge_sort_bottomup, ]:
        data = the_data.copy()

        t = timeit.timeit(stmt='func(data)', globals=locals(), number=1)
        print(f" •{func.__name__} \r\t\t\t\t{round(t, 3)}", end='\t ')

        for i in range(0, len(test_data), 10000):
            assert data[i] == test_data[i]

        t = timeit.timeit(stmt='func(data)', globals=locals(), number=1)
        print(round(t, 3))

    print('(data size:', len(the_data), 'records)\n')
    print('see more: https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_sorts')


if __name__ == '__main__':
    test()
