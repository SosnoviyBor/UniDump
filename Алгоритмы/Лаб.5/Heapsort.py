import time

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest) 

def heapSort(array): 
    start = time.perf_counter()
	
    n = len(array) 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(array, n, i) 
    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0) 

    end = time.perf_counter()
    finalTime = 1000 * (end - start)
    return "Heapsort for "+ str(len(array)) + " elements took "+ str(round(finalTime,3))+" miliseconds"
