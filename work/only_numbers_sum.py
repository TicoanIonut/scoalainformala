# def only_number_sum(my_list):
#     num_lst = []
#     for mixed in my_list:
#         if type(mixed) in [type(1), type(1.0)]:
#             num_lst.append(mixed)
#     return sum(num_lst)
#
#
# lst = (-1, 3, 5, 'gsaf', [2, 3, 'g'])
# print(only_number_sum(lst))


def your_func(*args):
	for i in args:
		if i in type(1):
			return i


your_func(1, 5, -3, 'abc', [12, 56, 'cad'])
