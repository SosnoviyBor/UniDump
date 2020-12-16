triangle = [7, 3, 8, 8, 1, 0, 2, 7, 4, 4, 4, 5, 2, 6, 5]
triangle_length = len(triangle)
maximum = 0
temp_number = 0
minimum = 2 ^ 32 - 1


def finder(x, level):
    global triangle_length
    global maximum
    global temp_number
    global minimum
    if x < 0:
        return "Exception"
    if x + level + 1 > triangle_length:
        if temp_number < minimum:
            minimum = temp_number
        if temp_number > maximum:
            maximum = temp_number
        return
    temp_number += triangle[x + level]
    finder(x + level, level + 1)
    finder(x + level + 1, level + 1)
    temp_number -= triangle[x + level]
    return


# Функция которая находит на каком уровне находиться елемент где x индекс елемента в массиве
def getLevel(x):
    maxLevelItem = 0
    level = 0
    if x < 0:
        print("Exception")
        return -1
    while maxLevelItem < x:
        level += 1
        maxLevelItem += level + 1
    return level


def findByXY(row_index, column_index):
    dumpy = []
    index_array = []
    for i in range(row_index + 1):
        for z in range(i):
            dumpy.append(0)
    index = len(dumpy)
    for i in range(row_index):
        index_array.append(index)
        index += 1
    finder(index_array[column_index], getLevel(index_array[column_index]))


element_index = 3
finder(element_index, getLevel(element_index))
print(maximum)
print(minimum)
print(getLevel(element_index))

findByXY(2, 0)
print(maximum)
