n = int(input())
for i in range(n + 1):
	if i % 2 != 0:
		continue
	print('numere pare:', sum(i))
