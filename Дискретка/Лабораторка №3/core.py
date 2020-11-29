import random

# Генератор для случайных дат рождения в формате "день.месяц"
def dateGenerator ():
	month = random.randint(1,12)
	if month == 2:
		lastDay = 28
	elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
		lastDay = 31
	else:
		lastDay = 30
	day = random.randint(1,lastDay)
	date = str(day)+"."+str(month)
	return date

# Открываем файл со входными данными в режиме чтения и файл с выходными данными в режими перезаписи
iFileName = "input.txt"
oFileName = "output.txt"
file = open(iFileName, "r")
newFile = open(oFileName, "w")

# Построчно дополняем файл с выходными данными
for currentLine in file:
	currentLine = currentLine[:len(currentLine)-1]
	editedLine = currentLine + " " + dateGenerator() +"\n"
	newFile.write(editedLine)

# Закрываем файлы и пишем об окончании выполнения кода
file.close()
newFile.close()
print(oFileName+" был успешно сгенерирован")