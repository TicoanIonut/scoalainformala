# import pandas as pd
#
# rd = pd.read_csv('task.csv', header=None)
# print(rd.head(1))
# alegeri = ["task", 'data', 'persoana', 'categorie']
# def filt_aleg():
#     fi_ale = int(input('Alege o categorie de filtrare dintre urmatoarele:\n'
#                    'task, data, persoana, categorie\n'
#                    'sau meniu pentru meniu principal\n'
#                    '>>'))
#     return fi_ale
#
# # print(filt_aleg(), type(filt_aleg))
# if filt_aleg() in range(1,6):
#     print('works')
# else:
#     print('nono')
#
# print(filt_aleg, type(filt_aleg))


# fi_ale = int(input('Alege o categorie de filtrare dintre urmatoarele:\n'
#                     'task, data, persoana, categorie\n'
#                     'sau meniu pentru meniu principal\n'
#                     '>>'))
# if fi_ale in range(1,6):
#     print('works')
# else:
#     print('nono')


def men_inp():
    minp = int(input('Alege o categorie 1-6\n'
                 '1 Listare date (sortare în funcție de categorie)\n'
                 '2 Sortare: se alege o opțiune din cele 8 de mai jos\n'
                 '3 Filtrare date (în funcție de detalii)\n'
                 '4 Adaugarea unui nou task\n'
                 '5 Editarea detaliilor (task, data, persoana responsabila sau categoria)\n'
                 '6 stergerea unui task\n'
                 '>>'))
    return minp


men_inp()

if men_inp == 2:
    print(men_inp, type(men_inp))
else:
    print('nunu')             # formula sortare


