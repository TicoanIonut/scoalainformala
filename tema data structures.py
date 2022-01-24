mylist=[7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
mylist.sort()
print('lista ordonata',mylist)                    #lista ordonata ascendent

mylist.sort()
mylist.reverse()
print('lista ordonata',mylist)                    #lista ordonata inversata
print('lista ordonata',mylist[-1::-1])            #lista ordonata inversata(fara reverse)

mylist.sort()
print('numere pare',mylist[1::2])                 #numere pare

mylist.sort()
print('numere impare',mylist[0::2])               #numere impare

mylist.sort()
print(mylist)
del mylist[0::3]                                 #multilpi ai nr 3 daca se cunoaste lista, folosind slicing
del mylist[0::2]
print('multipli ai numarului 3',mylist)           


mylist = [elem for elem in mylist if elem % 3== 0]        #multipli ai numarului 3
print(mylist)

