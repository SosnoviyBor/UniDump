# Импортируем библиотеку с математическими методами
import math

# Делаем функцию для подсчета значения нужной нам функции
def calc ():
	a = 5.016
	c = 3.5
	if a <= b:
		x = 2*math.cos(a+c)
	else:
		x = (-b*math.pow(c, 2)) / (3 + (3*math.pow(c, 2)/5))
	return print(x)

# Выбираем, какое значение переменной В мы будем использовать
print("Input '1' if you want b to equal 7.22 \n Input '2' if you want b to equal 10.98")
i = int(input())
if i == 1:
	b = 7.22
	calc()
elif i == 2:
	b = 10.98
	calc()
else:
	print("Wrong input")