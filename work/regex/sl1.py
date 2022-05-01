import re

# while True:
#     n = input()
#     # pat = r'^gl'
#     pat = r'gl'
#     if re.match(pat, n):
#         print('yes yes')
#     else:
#         print('nonon')
#     if n == 'gata':
#         print('gata')
#         break
#     cn = re.findall(pat, n)
#     count = 0
#     for w in cn:
#         count += 1
#     print(count)

# n = input()
# # pat = r'^gl'
# pat = r'00'
# s = re.sub(pat, '+', n)
# print(s)
# while True:
#     n = input()
#     pat = r'^m..e$'
#     if re.match(pat, n):
#         print('Match')
#     else:
#         print('nono')
while True:
	n = input()
	pat = r'[A-Za-z]@.com$'
	if re.search(pat, n):
		print('Match')
	else:
		print('nono')
