iii = input('enter text')
vv = input('second')
c = 0
for i in iii:
	if i in vv:
		c += 1
print(c / len(iii) * 100)
