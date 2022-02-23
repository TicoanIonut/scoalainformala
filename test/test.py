import csv
import datetime


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
        elif iii != 'da':                           # aici ce urmeaza
            print('merge bine')
            break


def taskuri():
    categorii()
    with open('task.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([task(), data(), pers(), cat()])
    iii = input('Next task?\nda pentru da\nsau orice pentru nu ').lower()
    if iii == 'da':
        return taskuri_doi()
    elif iii != 'da':
        print('merge bine')
        quit()                      # aici ce urmeaza


taskuri()
