def func(result):
    if flt_in_put> 0:
        print(in_put)
    elif flt_in_put <= 0:
        print(in_put)
    else:
        print(0)
    return result
in_put = input('>>')
try:
    flt_in_put = float(in_put)
except:
    print(0)
    quit()
call_func = func(flt_in_put)

