import time

def quickSort(data, left, right):
    if left >= right : return

    pivot = data[(left+right)//2]
    index = partition(data,left,right,pivot)

    quickSort(data, left, index-1)
    quickSort(data, index, right)

def partition(data,left,right,pivot):
    while left <= right:
        while data[left] < pivot:
            left += 1

        while data[right] > pivot:
            right -= 1

        if left <= right:
            data[left],data[right]=data[right],data[left]
            left += 1
            right -= 1

    return left

def QuickSortik (data):
	start = time.perf_counter()

	quickSort(data, 0, len(data)-1)

	end = time.perf_counter()
	finalTime = 1000 * (end - start)
	estimatedTime = "Quick sort for " + str(len(data)) + " elements took " + str(round(finalTime, 3)) + " miliseconds"

	return estimatedTime
