import time

def insertion_sort(nums):
	for i in range(len(nums)):
		j = i
		
		while j>0 and nums[j-1] > nums[j]:
			nums[j], nums[j-1] = nums[j-1], nums[j]
			j = j - 1

	return nums


def bucket_sort(data, elements_in_bucket = 20):
    
    start = time.perf_counter()
    
    arr = []

    buckets = len(data) // elements_in_bucket

    min_value = min(data)
    max_value = max(data)
    bucket_step = (max_value - min_value)/buckets

    for i in range(buckets):
        arr.append([])

    for j in data:
        if j != max_value:
            index = int((j+min_value) / bucket_step)
            arr[index].append(j)
        else :
            arr[-1].append(j)

    for i in range(buckets):
        arr[i] = insertion_sort(arr[i])

    data = []
    for i in range(buckets):
        for j in range(len(arr[i])):
            data.append(arr[i][j])



    end = time.perf_counter()
    finalTime = 1000 * (end - start)
    return "Bucketsort for "+ str(len(data)) + " elements took "+ str(round(finalTime,3))+" miliseconds"
 
 

