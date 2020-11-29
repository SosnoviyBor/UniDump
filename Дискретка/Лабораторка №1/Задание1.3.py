# Импортируем библиотеку с математическими методами
import math

# Переменные, даные в задании
a = 0.4
b = 10.8
x_start = 2
x_end = 20
n = 10

# Дополнительные переменные
d = (x_end - x_start) / (n-1)
counter = 0
x = 0

# Подсчет результата
while x != x_end:
	x = x_start + d*counter
	counter = counter + 1
	y = math.pow(a+b*x, 2)+a*b*math.sin(x)
	print("Iteration #"+str(counter)+" equals "+str(y))