import time


def shellsort(data):
    start = time.perf_counter()
    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp
        gap //= 2


    end = time.perf_counter()
    finalTime = 1000 * (end - start)
    return "Shellsort for "+ str(len(data)) + " elements took "+ str(round(finalTime,3))+" miliseconds"
