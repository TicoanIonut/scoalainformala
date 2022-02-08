def func(n):
    if n == 0:
        return 0
    if n % 2 == 1:                    #numere impare
        return n  + func(n-1)
    else:
        return func(n-1)

def func1(n):
    if n == 0:
        return 0
    if n % 2 == 0:                    #numere pare
        return n  + func1(n-1)
    else:
        return func1(n-1)

def func2(n):
    if n == 0:
        return 0
    else:                               #suma numere
        return n+ func2(n-1)

print(func(7),'nr impare\n',func1(7),'nr pare\n',func2(7),'suma nr\n')