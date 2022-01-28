def only_number_sum(my_list):
    num_list = []
    for mixed in my_list:
        if type(mixed) in [type(1) , type(1.0)]:
             num_list.append(mixed)
    return sum(num_list)
lst=(1,3,4,'gsaaf',[2,3,'g'])
print(only_number_sum(lst))