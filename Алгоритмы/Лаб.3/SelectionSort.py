import time

def SelectionSort( itemsList ):
    start = time.time()

    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i
        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j
        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    end = time.time()
    finalTime = 1000 * (end - start)
    estimatedTime = "Selection sort for " + str(n) + " elements took " + str(round(finalTime, 3)) + " miliseconds"

    return estimatedTime