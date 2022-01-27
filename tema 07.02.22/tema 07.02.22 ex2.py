def func(n):
    count=0
    if n==0:
        return 0
    elif n%2 == 0:
        count= count+n
        print(count)
        pass
    elif n % 2 ==1:
        count=count+n
        print(count)
    return n+func(n-1)
print(func(7))