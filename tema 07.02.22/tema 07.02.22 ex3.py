def func():
    in_put = input('>>')
    try:
        flt_in_put = float(in_put)
        if flt_in_put>= 0 or flt_in_put <=0:
            print(in_put)
    except:
        print(0)
func()

