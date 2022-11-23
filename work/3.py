# def make_acount():
#     return {'ballance':0}
# def depo(account, ammount):
#     account['ballance'] +=ammount
#     return account['ballance']
#
# a = make_acount()
# print(depo(a,10))

# def f(a, list=[]):
#     for i in range(a):
#         list.append(i*i)
#         print(list)
# f(3)
# f(2,[1,2,3])
# f(2)
lst = [1, 2, 45, 55, 66, 45, 2, 3, 4, 55, 66, 7, 8, 77, 66]
z = max(lst, key=lst.count)
print(z)
s = lst.count(z)
print(s)


def mx_mn(hl):
	mm = hl.split()
	return max(mm) + ' ' + min(mm)


hl = '1 2 3 4 5 6 7 8 9 -5'
print(mx_mn(hl))
