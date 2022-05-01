in_put = input('>>')


def func():
	try:
		flt_in_put = float(in_put)
		if flt_in_put >= 0 or flt_in_put <= 0:
			return True
	except ValueError:
		return False


if func() is True:
	print(in_put)
else:
	print(0)

# inpt = input('>')
#
#
# def func1():
#     if inpt.isnumeric():
#         return True
#     return False
#
#
# if func1() is True:
#     print(inpt)
# else:
#     print(0)

inp = input('>>>')


def func2(string):
	try:
		float(string)
		return True
	except ValueError:
		return False


if func2(inp) is True:
	print(inp)
else:
	print(0)
