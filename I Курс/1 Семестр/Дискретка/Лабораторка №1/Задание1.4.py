# Данные, даные в задании
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Объявление дополнительных переменных
blankList = []
index = -1
counter = -1

# Разделяем все элементы стринга alphabet и помещаем их в таблицу blankList
for x in alphabet:
	blankList.append(x)
	index += 1

# Пеереворачиваем таблицу
blankList.reverse()

# Выводим каждый элемент поочередно
while counter < index:
	counter += 1
	print(blankList[counter])