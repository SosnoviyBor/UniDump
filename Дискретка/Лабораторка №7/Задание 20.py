n = 10

def ternary (n):
	if n == 0:
		return '0'
	nums = []
	while n:
		n, r = divmod(n, 3)
		nums.append(str(r))
	return ''.join(reversed(nums))

for i in range(0, n+1):
	print("Iteration #"+str(i)+": "+str(ternary(i)))