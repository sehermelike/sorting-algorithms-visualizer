import time

# Bubble Sort
def bubble_sort(data, drawData, timeTick, chartType):
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ['yellow' if x == j or x == j + 1 else '#A90042' for x in range(len(data))], chartType)
                time.sleep(timeTick)
    drawData(data, ['yellow' for _ in range(len(data))], chartType)


# Insertion Sort
def insertion_sort(data, drawData, timeTick, chartType):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawData(data, ['yellow' if x == j + 1 else '#A90042' for x in range(len(data))], chartType)
        time.sleep(timeTick)
    drawData(data, ['yellow' for _ in range(len(data))], chartType)


# Selection Sort
def selection_sort(data, drawData, timeTick, chartType):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        drawData(data, ['yellow' if x == i or x == min_index else '#A90042' for x in range(len(data))], chartType)
        time.sleep(timeTick)
    drawData(data, ['yellow' for _ in range(len(data))], chartType)


# Merge Sort
def merge_sort(data, drawData, timeTick, chartType):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, drawData, timeTick, chartType)
        merge_sort(right_half, drawData, timeTick, chartType)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

        drawData(data, ['yellow' for _ in range(len(data))], chartType)
        time.sleep(timeTick)


# Heap Sort
def heapify(data, n, i, drawData, timeTick, chartType):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[i] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawData(data, ['yellow' if x == i or x == largest else '#A90042' for x in range(len(data))], chartType)
        time.sleep(timeTick)
        heapify(data, n, largest, drawData, timeTick, chartType)


def heap_sort(data, drawData, timeTick, chartType):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick, chartType)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        drawData(data, ['yellow' if x == i or x == 0 else '#A90042' for x in range(len(data))], chartType)
        time.sleep(timeTick)
        heapify(data, i, 0, drawData, timeTick, chartType)


# Quick Sort
def partition(data, low, high, drawData, timeTick, chartType):
    i = low - 1
    pivot = data[high]

    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            drawData(data, ['yellow' if x == i or x == j else '#A90042' for x in range(len(data))], chartType)
            time.sleep(timeTick)

    data[i + 1], data[high] = data[high], data[i + 1]
    drawData(data, ['yellow' if x == i + 1 or x == high else '#A90042' for x in range(len(data))], chartType)
    time.sleep(timeTick)

    return i + 1


def quick_sort(data, low, high, drawData, timeTick, chartType):
    if low < high:
        pi = partition(data, low, high, drawData, timeTick, chartType)
        quick_sort(data, low, pi - 1, drawData, timeTick, chartType)
        quick_sort(data, pi + 1, high, drawData, timeTick, chartType)


# def bubble_sort(data, drawData, timeTick, chartType):
#     for _ in range(len(data) - 1):
#         for j in range(len(data) - 1):
#             if data[j] > data[j+1]:
#                 data[j],data[j+1] = data [j+1], data[j]
#                 drawData(data, ['yellow' if x==j or x== j+1 else '#A90042' for x in range(len(data))], chartType)
#                 time.sleep(timeTick)
#     drawData(data, ['yellow' if x==j or x== j+1 else '#A90042' for x in range(len(data))], chartType)

# def selection_sort

#     return data
# data = [1,6,3,9,4,9,4,0,5]
# data = bubble_sort(data)
# print (data)