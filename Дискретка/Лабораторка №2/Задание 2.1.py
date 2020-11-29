# Импортируем библиотеку с математическими методами
import math

# Спрашиваем у пользователя значение, которое он бы хотел проверить
x = float(input("Ведите свой Х: "))

# *звуки интенсивной проверки*
def calc (x):
	right = 1 - pow(x, 3)/math.factorial(3) + pow(x, 5)/math.factorial(5) - pow(x, 7)/math.factorial(7) + pow(x, 9)/math.factorial(9)
	left = math.sin(x)
	if left == right:
		result = "equal"
	else: result = "not equal"
	return result

# Вывод ответа
print("x = "+str(x)+"; "+calc(x))