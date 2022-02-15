inp = input('>>')


def func():
    try:
        flt_input = float(inp)
        if flt_input >= 0 or flt_input <= 0:
            return True
    except:
        return False


if func() is True:
    print(inp, 'func')
else:
    print(0, 'func')


def func1():
    if inp.isnumeric():                # nu functioneaza cu float
        return True
    return False


if func1() is True:
    print(inp, 'func1')
else:
    print(0, 'func1')


def func2(inp):
    try:
        float(inp)
        return True
    except ValueError:
        return False


if func2(inp) is True:
    print(inp, 'func2')
else:
    print(0, 'func2')
