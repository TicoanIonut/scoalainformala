def func(n):
	if n == 0:
		return n
	if n % 2 == 0:
		return n + func(n - 1)
	return func(n - 1)


print(func(7))
