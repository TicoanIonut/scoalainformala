def only_number_sum(my_list):
    num_list = []
    for mixed in my_list:
        if type(mixed) in [type(1), type(1.0)]:
            num_list.append(mixed)
    return sum(num_list)


lst = (-1, 3, 5, 'gsaaf', [2, 3, 'cad'])
print(only_number_sum(lst))




def suma_int_real(*arr1, **arr2):
    return sum(filter(lambda i: isinstance(i, int), arr1))


print(suma_int_real(1, 5, -3, 'abc', [12, 56, 'cad']))
print(suma_int_real())
print(suma_int_real(2, 4, 'abc', param_1=2))
