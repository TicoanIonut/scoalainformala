import csv
import datetime
import pandas as pd


def chan():                                                             # change task curently not working
    rz = pd.read_csv('task.csv', header=None)
    print(rz)
    try:
        change = int(input('\n'
                           'Scrie o cifra conform indexului pe care vrei sa il modifici\n'
                           '>>'))
        if change in range(len(rz.index + 1)):
            rz = rz.drop(rz.index[change])
            # with open('task.csv', 'w') as file:
            #     write = csv.writer(file)
            #     write.writerow([task(), data(), pers(), cat()])
            print(rz)
        else:
            chan()
    except ValueError:
        chan()


def delet():                                                                # delete task
    rd = pd.read_csv('task.csv', header=None)
    print(rd)
    try:
        dele = int(input('\n'
                         'Scrie o cifra conform indexului pe care vrei sa il stergi\n'
                         '>>'))
        if dele in range(len(rd.index + 1)):
            rd = rd.drop(rd.index[dele])
            print(rd)
        else:
            delet()
    except ValueError:
        delet()
    m_inp()


def men_inp():
    print('Alege o categorie 1-6\n'                                             # meniu principal
          '1 Listare date (sortare în funcție de categorie)\n'
          '2 Sortare: 8 optiuni \n'
          '3 Filtrare date (în funcție de detalii)\n'
          '4 Adaugarea unui nou task\n'
          '5 Editarea detaliilor (task, data, persoana responsabila sau categoria)\n'
          '6 Stergerea unui task')
    return


def aleg_sort():
    print('Alege sortare, o opțiune 1-8 sau 9 pentru meiu principal\n'          # meniu alegere sortare
          '1 Sortare ascendenta Task\n'
          '2 Sortare descendenta Task\n'
          '3 Sortare ascendenta data\n'
          '4 Sortare descendenta data\n'
          '5 Sortare ascendenta persoana responsabila\n'
          '6 Sortare descendenta persoana responsabila\n'
          '7 Sortare ascendenta categorie\n'
          '8 Sortare descendenta categorie\n'
          '9 Meniu principal')
    return


def filt_aleg():
    print('Alege o categorie de filtrare 1-4:\n'                        # meniu alegere filtre
          '1 task\n'
          '2 data\n'
          '3 persoana\n'
          '4 categorie\n'
          '5 pentru meniu principal')
    return


def m_inp():
    m = int(input('Press 0 pentu quit sau 1 pentru meniu\n'             # continuare in meniu sau quit
                  '>'))
    if m == 1:
        return meniu()
    if m != 0 or m != 1:
        return m
    if m == 0:
        print('Thank you caome again')
        quit()
    return m_inp()


def meniu():
    men_inp()
    command1 = int(input('>'))
    if command1 not in range(1, 7):
        return men_inp(), command1
    if command1 == 1:
        rd = pd.read_csv('task.csv', header=None)
        df = rd.sort_values(by=[3])                                         # categorie
        print(df)
        m_inp()
    if command1 == 2:
        aleg_sort()
        command2 = int(input('>>'))
        if command2 not in range(1, 10):
            return aleg_sort(), command2
        if command2 == 1:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[0])                                     # ascending task
            print(df)
            m_inp()
        if command2 == 2:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[0], ascending=False)                    # descending task
            print(df)
            m_inp()
        if command2 == 3:
            rd = pd.read_csv('task.csv', header=None)
            rd[1] = pd.to_datetime(rd[1], format="%d.%m.%Y")
            df = rd.sort_values(by=[1])                                     # ascending data
            print(df)
            m_inp()
        if command2 == 4:
            rd = pd.read_csv('task.csv', header=None)
            rd[1] = pd.to_datetime(rd[1], format="%d.%m.%Y")
            df = rd.sort_values(by=[1], ascending=False)                    # ascending data
            print(df)
            m_inp()
        if command2 == 5:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[2])                                     # ascending persoana
            print(df)
            m_inp()
        if command2 == 6:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[2], ascending=False)                    # ascending persoana
            print(df)
            m_inp()
        if command2 == 7:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[3])                                     # ascending categorie
            print(df)
            m_inp()
        if command2 == 8:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[3], ascending=False)                    # ascending categorie
            print(df)
            m_inp()
        if command2 == 9:
            return meniu()
    if command1 == 3:
        filt_aleg()
        command3 = int(input('>>>'))
        if command3 not in range(1, 6):
            return filt_aleg(), command3
        if command3 == 1:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[0])                                 # only ascending task
            print(df[0])
            m_inp()
        if command3 == 2:
            rd = pd.read_csv('task.csv', header=None)
            rd[1] = pd.to_datetime(rd[1], format="%d.%m.%Y")
            df = rd.sort_values(by=[1])                                 # only ascending data
            print(df[1])
            m_inp()
        if command3 == 3:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[2])                                 # only ascending pers
            print(df[2])
            m_inp()
        if command3 == 4:
            rd = pd.read_csv('task.csv', header=None)
            df = rd.sort_values(by=[3])                                 # only ascending categ
            print(df[3])
            m_inp()
        if command3 == 5:
            return meniu()
    if command1 == 4:
        taskuri_doi()                                                   # adaugare nou task
    if command1 == 5:
        chan()                                                          # editare task
    if command1 == 6:                                                   # deleting task
        delet()


def categorii():
    with open('categorii.csv', 'w') as file:                                # alegere categorii
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
    with open('categorii.csv') as file:                                     # verifica categorii
        reader = csv.reader(file)
        for line in reader:
            return line


def task():
    ttt = input('Introdu un Task ').lower()                                 # introducere taskuri
    with open('task.csv', 'r') as file:
        for line in file.readlines():
            if ttt in line:
                ttt = input('Introdu alt task, acesta exista deja')
    return ttt


def data():
    ddd = input('Introdu data limita Z.L.A ')                               # introducere data
    try:
        if datetime.datetime.strptime(ddd, "%d.%m.%Y"):
            return ddd
    except ValueError:
        return data()


def pers():
    ppp = input('Introdu persoana responsabila ').lower()                   # introducere pers
    while ppp.isalpha() is False:
        ppp = input('Introdu persoana responsabila ').lower()
    return ppp


def cat():
    ccc = input('Introdu o categorie ',).lower()                            # introducere categorie
    while ccc not in pcateg()[0:]:
        ccc = input(f'Eroare! \nAlege o categorie din cele disponibile!\n'
                    f'{pcateg()[0:]}\n'
                    f'>>').lower()
    return ccc


def taskuri_doi():
    while True:
        with open('task.csv', 'a') as file:                             # functia pentru adaugare taskuri
            write = csv.writer(file)
            write.writerow([task(), data(), pers(), cat()])
        iii = input('Next task?\nda pentru da\nsau orice pentru nu ').lower()
        if iii == 'da':
            return taskuri_doi()
        elif iii != 'da':
            meniu()


def taskuri():                                                          # functia principala
    categorii()
    with open('task.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([task(), data(), pers(), cat()])
    iii = input('Next task?\nDA pentru DA\nsau any key pentru NU ').lower()
    if iii == 'da':
        return taskuri_doi()
    elif iii != 'da':
        meniu()


taskuri()
