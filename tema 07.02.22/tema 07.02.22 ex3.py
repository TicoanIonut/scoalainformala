def func(r):
    in_put = input('>>')
    try:
        flt_in_put = float(in_put)
        if flt_in_put>= 0:
            print(in_put)
        elif flt_in_put <= 0:
            print(in_put)
    except:
        print(0)

func(0)

