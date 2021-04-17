import time


def mergeSortTimer(array):
    start = time.perf_counter()
    def mergeSort(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        # Делим на 2 части правлую и левую
        right = mergeSort(array[mid:]) # центральный елемент включительно
        left = mergeSort(array[:mid])

        return merge(left, right)

    def merge(left, right):
        merged = [0 for x in range(len(left)+len(right))] # пустой список
        left_array_index = 0
        right_array_index = 0
        k = 0
        # Сортировка +добовление элементов в масив
        while left_array_index < len(left) and right_array_index < len(right):
            if left[left_array_index] < right[right_array_index]:
                merged[k] = left[left_array_index]
                left_array_index += 1
            else:
                merged[k] = right[right_array_index]
                right_array_index += 1
            k += 1
        while right_array_index < len(right):
            merged[k] = right[right_array_index]
            right_array_index += 1
            k += 1
        while left_array_index < len(left):
            merged[k] = left[left_array_index]
            left_array_index += 1
            k += 1

        return merged

    mergeSort(array)
    end = time.perf_counter()
    finalTime = 1000 * (end - start)
    return "Merge sort for "+ str(len(array)) + " elements took "+ str(round(finalTime,3))+" miliseconds"
