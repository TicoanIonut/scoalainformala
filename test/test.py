import csv
import datetime
import pandas as pd


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


def aleg_sort():
    asort = int(input('Alege sortare, o opțiune 1-8 sau 9 pentru meiu principal\n'
                      '1 Sortare ascendenta Task\n'
                      '2 Sortare descendenta Task\n'
                      '3 Sortare ascendenta data\n'
                      '4 Sortare descendenta data\n'
                      '5 Sortare ascendenta persoana responsabila\n'
                      '6 Sortare descendenta persoana responsabila\n'
                      '7 Sortare ascendenta categorie\n'
                      '8 Sortare descendenta categorie\n'
                      '9 Meniu principal\n'
                      '>>'))
    return asort


def filt_aleg():
    fi_ale = int(input('Alege o categorie de filtrare 1-4:\n'
                       '1 task\n'
                       '2 data\n'
                       '3 persoana\n'
                       '4 categorie\n'
                       '5 pentru meniu principal\n'
                       '>>'))
    return fi_ale


def m_inp():
    m = int(input('0 pentu quit sau 1 pentru meniu'))
    if m == 1:
        return men_inp()
    if m != 0 or m != 1:
        return m
    if m == 0:
        quit()


def meniu():
    if men_inp() not in range(1, 7):
        return men_inp()
    elif men_inp() == 1:
        print('Listare date (sortare în funcție de categorie)')             # formula sortare
        m_inp()
    if men_inp() == 2:
        aleg_sort()
        if aleg_sort() not in range(1, 10):
            return aleg_sort()
        if aleg_sort() == 1:
            print('sortare ascendenta task')                                # formula sortare
            m_inp()
        if aleg_sort() == 2:
            print('sortare descendenta task')                               # formula sortare
            m_inp()
        if aleg_sort() == 3:
            print('sortare ascendenta data')                               # formula sortare
            m_inp()
        if aleg_sort() == 4:
            print('sortare descendenta data')                               # formula sortare
            m_inp()
        if aleg_sort() == 5:
            print('sortare ascendenta persoana')                               # formula sortare
            m_inp()
        if aleg_sort() == 6:
            print('sortare descendenta persoana')                               # formula sortare
            m_inp()
        if aleg_sort() == 7:
            print('sortare ascendenta categorie')                               # formula sortare
            m_inp()
        if aleg_sort() == 8:
            print('sortare descendenta categorie')                               # formula sortare
            m_inp()
        if aleg_sort() == 9:
            print('meniu principal')
            return men_inp()
    if men_inp() == 3:
        if filt_aleg() not in range(1, 6):
            return filt_aleg()
        if filt_aleg() == 1:
            print('filtrare task')
            m_inp()
        if filt_aleg() == 2:
            print('filtrare data')
            m_inp()
        if filt_aleg() == 3:
            print('filtrare persoana')
            m_inp()
        if filt_aleg() == 4:
            print('filtrare categorie')
            m_inp()
        if filt_aleg() == 5:
            return men_inp()
    if men_inp() == 4:
        print('adaugare nou task')
    if men_inp() == 5:
        print('Editarea detaliilor (task, data, persoana responsabila sau categoria)')
    if men_inp() == 6:
        print('stergerea unui task')


def categorii():
    with open('categorii.csv', 'w') as file:
        categ1 = input('Alge categoria 1 ')
        categ2 = input('Alge categoria 2 ')
        while categ2 == categ1:
            categ2 = input('Alege categoria 2 diferita ')
        categ3 = input('Alge categoria 3 ')
        while categ3 == categ2 or categ3 == categ1:
            categ3 = input('Alege categoria 3 diferita ')
        categ4 = input('Alge categoria 4 ')
        while categ4 == categ3 or categ4 == categ2 or categ4 == categ1:
            categ4 = input('Alege categoria 4 diferita ')
        write = csv.writer(file)
        write.writerow([categ1, categ2, categ3, categ4])
        return


def pcateg():
    with open('categorii.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            return line


def task():
    ttt = input('Introdu un Task ').lower()
    with open('task.csv', 'r') as file:
        for line in file.readlines():
            if ttt in line:
                ttt = input('Introdu alt task, acesta exista deja')
    return ttt


def data():
    ddd = input('Introdu data limita Z.L.A ')
    try:
        if datetime.datetime.strptime(ddd, "%d.%m.%Y"):
            return ddd
    except ValueError:
        return data()


def pers():
    ppp = input('Introdu persoana responsabila ').lower()
    while ppp.isnumeric():
        ppp = input('Introdu persoana responsabila ').lower()
    return ppp


def cat():
    ccc = input('Introdu o categorie ',).lower()
    while ccc not in pcateg()[0:]:
        ccc = input(f'Eroare! \nAlege o categorie din cele disponibile! {pcateg()[0:]}').lower()
    return ccc


def taskuri_doi():
    while True:
        with open('task.csv', 'a') as file:
            write = csv.writer(file)
            write.writerow([task(), data(), pers(), cat()])
        iii = input('Next task?\nda pentru da\nsau orice pentru nu ').lower()
        if iii == 'da':
            return taskuri_doi()
        elif iii != 'da':
            meniu()


def taskuri():
    categorii()
    with open('task.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([task(), data(), pers(), cat()])
    iii = input('Next task?\nda pentru da\nsau orice pentru nu ').lower()
    if iii == 'da':
        return taskuri_doi()
    elif iii != 'da':
        meniu()


taskuri()
