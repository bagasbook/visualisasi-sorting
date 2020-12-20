import time


def bubble_sort(data, drawdata, timetick):
    N = len(data)
    for bypass in range(N-1):
        for i in range(N - bypass - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                drawdata(data, ['cyan' if x == i or x == i +
                                1 else 'deep sky blue' for x in range(N)])
                time.sleep(timetick)
