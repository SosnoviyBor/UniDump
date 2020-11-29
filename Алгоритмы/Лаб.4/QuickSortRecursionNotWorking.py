import time
def swap(array,left,right):
	temp = array[left]
	array[left] = array[right]
	array[right] = temp


def quickSort (array):
	start = time.perf_counter()
	# Когда-то здесь будет код
	Quick(array, 0,len(array)-1)


	end = time.perf_counter()
	finalTime = 1000 * (end - start)
	estimatedTime = "Quick sort for " + str(len(table)) + " elements took " + str(round(finalTime, 3)) + " miliseconds"

	return estimatedTime


def Quick(array, left, right):
	if left < right:
		pivotIndex = partition(array,left,right)
		Quick(array,left,pivotIndex-1)
		Quick(array,pivotIndex,right)


def partition(array,left,right):
	pivot = array[right]
	pivotIndex = left

	for x in range(right):
		if array[x]<=pivot:
			swap(array,x,pivotIndex)
			pivotIndex+=1
	swap(array,pivotIndex,right)

	return pivotIndex;
