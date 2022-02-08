from goto import with_goto  # pip install goto-statement
# if module throws an exception, change code in it on next lines:
# 53 -> return code.replace(co_code=codestring)
# 175 -> return _make_code(code, buf.tobytes())

@with_goto	# enables usage of "goto" and "label" operators
def main():
	uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	# 26 chars long
	lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"	# 26 chars long
	maxWords = 100
	# if any of these conditions are met, we assume, its a next page
	pageWords = 235
	pageLetters = 1800

	# read whole file in single string
	# usage of functions here is inevitable
	with open("task2input.txt", "r", encoding="utf8") as file:
		content = file.read()
	# add an a special symbol to the end of our content
	content += "$"


	# lowercase the string, ignore special symbols and numbers, swap newlines to spaces
	tmp = ""
	i = 0
	label .sCheck
	if content[i] in lowercaseLetters:
		tmp += content[i]
	elif content[i] in uppercaseLetters:
		j = 0
		label .upperLetterPicker
		if content[i] != uppercaseLetters[j]:
			j+=1
			goto .upperLetterPicker
		tmp += lowercaseLetters[j]
	elif content[i] == "\n" or content[i] == " ":
		tmp += " "
	elif content[i] == "$":
		content = tmp + "$"
		goto .sCheckEnd
	i+=1
	goto .sCheck


	label .sCheckEnd
	# count words
	word = ""
	currentPage = 1
	letterCounter = 0
	wordCounter = 0
	wordsInResult = -1
	result = [ [None, 0, []] ]	# [word, timesWritten, [pagesWritten]]
	i = 0
	label .wCheck
	if content[i] == " ":
		j = 0
		wordCounter+=1
		if wordCounter >= pageWords or letterCounter >= pageLetters:
			currentPage+=1
			letterCounter -= pageLetters
			wordCounter = 0
		label .wordInserter
		if word == result[j][0]:
			result[j][1]+=1
			if currentPage not in result[j][2]:
				result[j][2] += [currentPage]
			word = ""
			i+=1
			goto .wCheck
		elif result[j][0] == None:
			result[j][0] = word
			result[j][1] = 1
			result[j][2] += [currentPage]
			result += [ [None, 0, []] ]
			wordsInResult += 1
			word = ""
			i+=1
			goto .wCheck
		else:
			j+=1
			goto .wordInserter
	elif content[i] == "$":
		result = result[:-1]
		goto .wCheckEnd
	else:
		word += content[i]
	i+=1
	letterCounter+=1
	goto .wCheck


	label .wCheckEnd
	# throw out too common words
	i = 0
	label .wThrower
	if result[i][1] > maxWords or result[i][0] == "":
		wordsInResult -= 1
		del result[i]
	i+=1
	if i >= wordsInResult:
		goto .wThrowerEnd
	goto .wThrower


	label .wThrowerEnd
	# sort the result
	i = 0
	# selection sort algorithm scratched from my almost one year old asm lab work
	label .sorter
	maxId = i
	j = i+1

	label .sorterInner
	if result[maxId][0] > result[j][0]:
		maxId = j
	if j >= wordsInResult:
		goto .sorterInnerEnd
	j+=1
	goto .sorterInner
	
	label .sorterInnerEnd
	result[i], result[maxId] = result[maxId], result[i]
	i+=1
	if i >= wordsInResult:
		goto .sorterEnd
	goto .sorter


	label .sorterEnd
	# time to print the result
	i = 0
	print("---------------------------")
	label .printer
	print(f"#{i+1}. {result[i][0]} - {result[i][2]}")
	if i < wordsInResult:
		i+=1
		goto .printer
	print("---------------------------")

	return

main()