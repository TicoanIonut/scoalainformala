# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. (1 punct)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def del_lista(x):
    while len(x) > 2:
        del x[2::3]
        print(x)
        while len(x) > 0:
            del x[-1]
            print(x)


del_lista(lista)
