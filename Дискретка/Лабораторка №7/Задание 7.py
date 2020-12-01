iFileName = "input.txt"
file = open(iFileName, "r")
text = file.read()
file.close()

amountOfA = 0
amountOfB = 0

for letter in text:
	if letter == "a":
		amountOfA += 1
	elif letter == "b":
		amountOfB += 1

if amountOfA > amountOfB:
	result = True
else:
	result = False

print(result)