#REGULI
#daca primul cuvant si ultimul se repetau in cuvant, caracterul trebuie afisat
#restul caracterelor erau ascunse
#sapte sanse de a ghici cuvantul
# word o_o___o_ee
# litera_cuvant=input('alege o litera')
# print(litera_cuvant)
word='onomaatopee'
lista_cuvant=[]
for iterator in word:
    lista_cuvant.append('_')
    if iterator== word[0] or iterator == word[-1]:
        lista_cuvant[-1]=iterator
print(''.join(lista_cuvant))
numar_incercari=1
lista_litere_incercate=set()
while numar_incercari<=7:
    litera=input('alege o litera').lower()
    if litera in word.lower():
        for index, valoare in enumerate(word):
            if valoare.lower() == litera:
                lista_cuvant[index]=litera
        print('de adaugat lista cuvant')
    else:
        if litera.lower() not in list(lista_litere_incercate):
            numar_incercari += 1
        lista_litere_incercate.add(litera.lower())
        print(f'litera nu exista,deja ai incercat{",".join(lista_litere_incercate)}')
        print(f"mai ai {8-numar_incercari}")
    if numar_incercari>7:
        print(f"ai pierdut cuvantul era {word}")
    elif ''.join(lista_cuvant) == word:
        print('ai castigat')
        break
    else:
        print(''.join(lista_cuvant))



