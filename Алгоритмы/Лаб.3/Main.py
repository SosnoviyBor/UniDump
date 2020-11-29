import random
from InsertionSort import *
from BubleSort import *
from SelectionSort import *

# Метод по созданию упорядоченных списков
def make_consistent_list(list_range):
    empty_list = []
    for x in range(list_range):
        empty_list.append(x)
    return empty_list

# Метод по созданию случайных списков
def make_random_list(list_range):
    empty_list = []
    for x in range(list_range):
        empty_list.append(random.randrange(0, list_range))
    return empty_list

# Создаем наши списки и помещаем их в другой список для более удобного взаимодействия с ними
listOfLists = []
listOfLists.insert(0, make_random_list(100))
listOfLists.insert(1, make_random_list(1_000))
listOfLists.insert(2, make_random_list(10_000))
listOfLists.insert(3, make_consistent_list(100))
listOfLists.insert(4, make_consistent_list(1_000))
listOfLists.insert(5, make_consistent_list(10_000))

# Начинаем сортировать списки
counter = 0
for i in listOfLists:
    if counter == 0:
        print("\n##### Random Lists #####")
    elif counter == 3:
        print("\n\n##### Consistent Lists #####")
    else: print("----------")
    print(bubbleSort(i.copy()))
    print(insertionSort(i.copy()))
    print(SelectionSort(i.copy()))
    counter += 1