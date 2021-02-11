import time


def counting_sort(data):
    start = time.perf_counter()
    accurrance_arr = [0]*(max(data)+1)
    output_arr = [0]*len(data)

    for i in range(0,len(data)):
        accurrance_arr[data[i]] += 1

    for i in range(1,(max(data)+1)): #add +1
        accurrance_arr[i] += accurrance_arr[i-1]

    i = len(data) -1;
    while i>=0:
        output_arr[accurrance_arr[data[i]] - 1] = data[i]
        accurrance_arr[data[i]] -= 1
        i -=1

    for i in range(0,len(data)):
        data[i] = output_arr[i]

    end = time.perf_counter()
    finalTime = 1000 * (end - start)
    return "CountingSort for "+ str(len(data)) + " elements took "+ str(round(finalTime,3))+" miliseconds"
