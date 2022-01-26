# def func(*x):
x=(1,5,-3,'abc',[12, 56,'cad'])
y=list(x)
print(y[0:])
matches = (x for x in y if x > 6)
print(matches)

    # try:
    #     z=[elem for elem in y if elem %2 == 0 or elem %2 ==1]
    # except TypeError:
    #     print(z)


# func(1,5,-3,'abc',[12, 56,'cad'])


