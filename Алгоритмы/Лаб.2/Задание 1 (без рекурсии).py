
def funFunction(our_input):
	dummy = int(our_input) // 10
	if int(our_input) == dummy * 10:
		our_input=str(our_input)
		blankList = []
		for x in our_input:
			blankList.append(x)
		blankList.reverse()
		return ("".join(blankList))
	else:
		return "Wrong input. Your number have to end with 0"
print(funFunction(input("Input your number: ")))