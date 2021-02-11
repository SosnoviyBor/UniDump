# Импортируем библиотеки
import math
import random

# Создаем переменные и сразу их выводим
a = float(random.randint(-10, 10))
b = float(random.randint(0, 20))
c = float(random.randint(0, 20))
print("a = "+str(a)+"; b = "+str(b)+"; c = "+str(c))

# Наша функция-оператор
def operator (x ,y):
	result = x+y/x
	return result

# Основная функция с подсчетами
def calc (a, b, c):
	if a == 0 or c == 0:
		return "Деление на ноль невозможно"
	z = (pow(a, 2) + pow(math.sin(operator(a, b)), 2)) / math.sqrt(math.atan(operator(c, a)))
	return z

# Вывод результата
print("result = "+str(calc(a, b, c)))