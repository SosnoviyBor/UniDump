iFileName = "input.txt"
oFileName = "output.txt"
file = open(iFileName, "r")
newFile = open(oFileName, "w")
inputText = file.read()
outputText = ""

for letter in inputText:
	if letter == "a":
		letter = letter.upper()
	outputText += letter
newFile.write(outputText)

file.close()
newFile.close()
print(oFileName+" был успешно сгенерирован")