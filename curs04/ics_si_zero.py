import random

tabla = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']


def display():
    print("\n")
    print(tabla[0] + " | " + tabla[1] + " | " + tabla[2] + "     1 | 2 | 3")
    print(tabla[3] + " | " + tabla[4] + " | " + tabla[5] + "     4 | 5 | 6")
    print(tabla[6] + " | " + tabla[7] + " | " + tabla[8] + "     7 | 8 | 9")
    print("\n")


joc_in_derulare = True
castigator = None
jucatori = ('x', '0')
jucator = random.choice(jucatori)


def joc():
    display()
    while joc_in_derulare:
        tura()
        gata_joc()
        schimb_jucator()
    if castigator == 'x' or castigator == '0':
        print(castigator, 'este castigator!')
    elif castigator is None:
        print('Remiza')
    replay()


def tura():
    print('Randul lui ' + jucator)
    if 'x' == jucator:
        pozitie_x()
    if '0' == jucator:
        pozitie_0()


def gata_joc():
    verifica_castigator()
    verifica_remiza()


def verifica_castigator():
    global castigator
    rand_castigator = verifica_rand()
    coloana_castigator = verifica_coloana()
    diagonala_castigator = verifica_diagonala()
    if rand_castigator:
        castigator = rand_castigator
    elif coloana_castigator:
        castigator = coloana_castigator
    elif diagonala_castigator:
        castigator = diagonala_castigator
    else:
        castigator = None


def verifica_rand():
    global joc_in_derulare
    rand1 = tabla[0] == tabla[1] == tabla[2] != '_'
    rand2 = tabla[3] == tabla[4] == tabla[5] != '_'
    rand3 = tabla[6] == tabla[7] == tabla[8] != '_'
    if rand1 or rand2 or rand3:
        joc_in_derulare = False
    if rand1:
        return tabla[0]
    if rand2:
        return tabla[3]
    if rand3:
        return tabla[4]
    return None


def verifica_coloana():
    global joc_in_derulare
    coloana1 = tabla[0] == tabla[3] == tabla[6] != '_'
    coloana2 = tabla[1] == tabla[4] == tabla[7] != '_'
    coloana3 = tabla[2] == tabla[5] == tabla[8] != '_'
    if coloana1 or coloana2 or coloana3:
        joc_in_derulare = False
    if coloana1:
        return tabla[0]
    if coloana2:
        return tabla[1]
    if coloana3:
        return tabla[2]
    return None


def verifica_diagonala():
    global joc_in_derulare
    diagonala1 = tabla[0] == tabla[4] == tabla[8] != '_'
    diagonala2 = tabla[6] == tabla[4] == tabla[2] != '_'
    if diagonala1 or diagonala2:
        joc_in_derulare = False
    if diagonala1:
        return tabla[0]
    if diagonala2:
        return tabla[6]
    return None


def verifica_remiza():
    global joc_in_derulare
    if'_'not in tabla:
        joc_in_derulare = False
        return True
    else:
        return False


def schimb_jucator():
    global jucator
    if jucator == 'x':
        jucator = '0'
    elif jucator == '0':
        jucator = 'x'
    return


def pozitie_x():
    pozitie = input('Selecteaza o pozitie de la 1 la 9')
    validare = False
    while not validare:
        while pozitie not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            pozitie = input('Selecteaza o alta pozitie')
        pozitie = int(pozitie) - 1
        if tabla[pozitie] == '_':
            validare = True
        else:
            print('nu se poate acolo')
    tabla[pozitie] = jucator
    display()


def pozitie_0():
    numere = '123456789'
    pozitie = random.choice(numere)
    # n1 = '1379'
    # n2 = '2468'
    # if tabla[4] == '_':
    #     pozitie = '5'
    # elif tabla[0] == '_' or tabla[2] == '_'or tabla[6] == '_'or tabla[8] == '_':
    #     pozitie = random.choice(n1)
    # elif tabla[1] == '_' or tabla[3] == '_' or tabla[5] == '_' or tabla[7] == '_':
    #     pozitie =random.choice(n2)
    validare = False
    while not validare:
        while pozitie not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            numere = '123456789'
            pozitie = random.choice(numere)
            # if tabla[4] == '_':
            #     pozitie = '5'
            # elif tabla[0] == '_' or tabla[2] == '_' or tabla[6] == '_' or tabla[8] == '_':
            #     pozitie = random.choice(n1)
            # elif tabla[1] == '_' or tabla[3] == '_' or tabla[5] == '_' or tabla[7] == '_':
            #     pozitie = random.choice(n2)
            print('Selecteaza o alta pozitie')
        pozitie = int(pozitie) - 1
        if tabla[pozitie] == '_':
            validare = True
        else:
            print('nu se poate acolo')
    tabla[pozitie] = jucator
    display()


def replay():
    if joc_in_derulare is True:
        restart = input('Vrei sa mai joci? y/n')
        if restart == 'y':
            joc()
        else:
            print('Multumim pentru joc!')
            quit()


joc()
