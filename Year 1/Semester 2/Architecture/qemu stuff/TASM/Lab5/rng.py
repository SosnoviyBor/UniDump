import random

file = open("arr_stack contents.txt", "w")

content = ""
for i in range(0, 16):
	content = content + "db "
	for j in range(0,15):
		content = content + str(random.randint(0,255)) + ", "
	content = content + str(random.randint(0,255)) + "\n"
# Отрезаем последний \n, чтобы файл был идеален-идеален
content = content[:len(content)-2]

file.write(content)

print("Thanks for using our services!")
file.close()