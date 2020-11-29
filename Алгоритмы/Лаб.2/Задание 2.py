result = 0


def fun_fuction(m, n):
	if 0 < m or m < n:
		return "Wrong input"
	else:
		Variable_to_save_m = m
		Variable_to_save_n = n
		global result
		if m == n or m == 0:
			result += 1
		else:
			if 0 < m and m < n:
				fun_fuction(m - 1, n - 1)
				fun_fuction(Variable_to_save_m, Variable_to_save_n - 1)
	return result

print(fun_fuction(int(input("M = ")), int(input("N = "))))