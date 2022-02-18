#FILTER

litera = ['a','b','c','d','e','i','j']
lista_numere = [1,2,3,4,5,6,7,8,9,10]
def functie_nr_pare(numere):
    if numere % 2 == 0:
        return  True
    return False

iterator_numere_pare = filter(functie_nr_pare, lista_numere)
print(list(iterator_numere_pare))



litere=['a','b','c','d','e','i','j']

def filtre_vocale(lettter):
    vocale = ['a', 'e', 'i', 'o', 'u']
    return True if lettter in vocale else False

print(filtre_vocale(litere))
filtrare_vocale = filter(filtre_vocale, litere)
print(list(filtrare_vocale))

