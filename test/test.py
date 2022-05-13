def validate(n1, k1):
	for i in n1:
		for j in n1[1:]:
			if i + j == k1:
				return'yes'
			
				
n = [10, 3, 15, 7]
k = 17
print(validate(n, k))
