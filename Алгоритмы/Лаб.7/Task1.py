triangle1 = [7, 3, 8, 8, 1, 0, 2, 7, 4, 4, 4, 5, 2, 6, 5]

test = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5],
]
triangle_length = len(test)


def max(first, second):
    if first > second:
        return first
    return second


def min(first, second):
    if first < second:
        return first
    return second


def findMax(triangle, row, column):
    new_triangle = [[0 for j in range(triangle_length)] for i in range(triangle_length)]
    # Записываем в новую матрицу самый нижний рядок
    for x in range(len(triangle[-1])):
        new_triangle[-1][x] = triangle[-1][x]

    for x in range(triangle_length - 2, -1, -1):
        for i in range(len(triangle[x])):
            max_right = new_triangle[x + 1][i]
            max_left = new_triangle[x + 1][i + 1]
            current_value = triangle[x][i]
            path_sum = current_value + max(max_right, max_left)
            new_triangle[x][i] = path_sum
    # print(new_triangle)
    return "The max path from coordinates: y  - " + str(row) + ", x - " + str(column) + " is " + str(new_triangle[row][column])


def findMin(triangle, row, column):
    new_triangle = [[0 for j in range(triangle_length)] for i in range(triangle_length)]
    # Записываем в новую матрицу самый нижний рядок
    for x in range(len(triangle[-1])):
        new_triangle[-1][x] = triangle[-1][x]

    for x in range(triangle_length - 2, -1, -1):
        for i in range(len(triangle[x])):
            max_right = new_triangle[x + 1][i]
            max_left = new_triangle[x + 1][i + 1]
            current_value = triangle[x][i]
            path_sum = current_value + min(max_right, max_left)
            new_triangle[x][i] = path_sum
    # print(new_triangle)
    return "The min path from coordinates: y  - " + str(row) + ", x - " + str(column) + " is " + str(new_triangle[row][column])


print(findMax(test, 0, 0))
print(findMin(test, 0, 0))
