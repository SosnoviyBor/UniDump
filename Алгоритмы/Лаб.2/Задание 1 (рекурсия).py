k=input("Write your number here: ")
str_our_input=str(k)
leng_str_our_input=len(str_our_input)
result=0
def funFunction(our_input):
	if str_our_input[leng_str_our_input-1]== "0":
		global result
		if our_input > 0 :
			reminder=our_input%10
			result = result * 10 + reminder

			funFunction(our_input // 10)
		return "0"+str(result)
	else:
		return "Wrong input. Your number have to end with 0"
print(funFunction(int(k)))
