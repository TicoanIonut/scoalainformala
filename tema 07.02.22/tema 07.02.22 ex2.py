def func(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n  + func(n-1)
    #if n % 2 ==1:
        #return n + func(n-1)
    else:
        return func(n-1)
print(func(7))