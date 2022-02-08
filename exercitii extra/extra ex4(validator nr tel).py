def nr_tl():
    nr_tel=input('introduceti nnumarul de telefon')
    if nr_tel.isnumeric() and len(nr_tel)==10:
        return nr_tel
    else:
        return False
print(nr_tl())