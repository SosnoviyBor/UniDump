def to_arabic (k):
	# initial settings
	k+=" "
	result=0
	dictionary_={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1," ":0}
	J=list(dictionary_.keys())
	
	# convert digit
	for x in range(len(k)-1):
		if J.index(k[x])<=J.index(k[x+1]):
			result+=dictionary_.get(k[x])
		else: 
			result-=dictionary_.get(k[x])
	
	if result<=3000 and result>=1:
		print(result)
	else:
		print("Number must be between 1 and 3000")
	return