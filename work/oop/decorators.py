# import time


def func(f):
	def wrapper(*args, **kwargs):
		print("Started")
		rv = f(*args, **kwargs)
		print("Ended")
		return rv
	
	return wrapper()


@func
def func2(x, y):
	print(x)
	return x, y


@func
def func3():
	print('i am func3')


x = func2(5, 6)
print(x)

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         rv =func()
#         total = time.time() - start
#         print("Time ", total)
#         return rv
#     return wrapper()
#
#
# @timer
# def test():
#     for _ in range(10000):
#         pass
#
#
# @timer
# def test2():
#     time.sleep(2)
#
#
# test()
# test2()
