lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

rezultat = zip(lista_1, lista_2)
print(list(rezultat))



def zip_function(lista_1, lista_2):
    lista = []
    for i in range(0, min(len(lista_1), len(lista_2))):
        lista.append((lista_1[i],lista_2[i]))
    return lista
print(zip_function(lista_1, lista_2))
