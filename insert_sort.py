import time


def insert_sort(data, drawdata, timetick):
    N = len(data)
    for top in range(1, N):
        k = top
        while k > 0 and data[k] < data[k-1]:
            data[k], data[k-1] = data[k-1], data[k]
            k -= 1
            drawdata(data, ['cyan' if x == k or x ==
                            k-1 else 'deep sky blue' for x in range(N)])
            time.sleep(timetick)
