# Объявляем массив
table = [1, 5, -3, 10, 10, 1, 20, 0]

# Считаем, два самых больших элемента и выводим их
def sum (table):
	biggest = table[0]
	secondBiggest = table[0]
	for i in table:
		if i > secondBiggest:
			if i >= biggest:
				secondBiggest = biggest
				biggest = i
			else: secondBiggest = i
	result = biggest + secondBiggest
	print("Biggest number = "+str(biggest)+"; Second biggest number = "+str(secondBiggest))
	return result

# Выводим результат подсчета
print("Result = "+str(sum(table)))