# inceput script
print('Joc de X si 0 vs AI')

# niste variabile
castiga = 0
pierde = 0
X = 'X'
O = 'O'


# Condidii peste conditii
def conditii_castig():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9
    global o_castiga, x_castiga, remiza
    global nume_jucator, nume_jucator1
    global castiga
    if a1 == 'X' and a2 == 'X' and a3 == 'X':
        x_castiga = True
    elif a4 == 'X' and a5 == 'X' and a6 == 'X':
        x_castiga = True
    elif a7 == 'X' and a8 == 'X' and a9 == 'X':
        x_castiga = True
    elif a1 == 'X' and a4 == 'X' and a7 == 'X':
        x_castiga = True
    elif a2 == 'X' and a5 == 'X' and a8 == 'X':
        x_castiga = True
    elif a3 == 'X' and a6 == 'X' and a9 == 'X':
        x_castiga = True
    elif a1 == 'X' and a5 == 'X' and a9 == 'X':
        x_castiga = True
    elif a3 == 'X' and a5 == 'X' and a7 == 'X':
        x_castiga = True
    elif a1 == 'O' and a2 == 'O' and a3 == 'O':
        o_castiga = True
    elif a4 == 'O' and a5 == 'O' and a6 == 'O':
        o_castiga = True
    elif a7 == 'O' and a8 == 'O' and a9 == 'O':
        o_castiga = True
    elif a1 == 'O' and a4 == 'O' and a7 == 'O':
        o_castiga = True
    elif a2 == 'O' and a5 == 'O' and a8 == 'O':
        o_castiga = True
    elif a3 == 'O' and a6 == 'O' and a9 == 'O':
        o_castiga = True
    elif a1 == 'O' and a5 == 'O' and a9 == 'O':
        o_castiga = True
    elif a3 == 'O' and a5 == 'O' and a7 == 'O':
        o_castiga = True
    if x_castiga:
        castiga = True
        return print('EU AM CASTIGAT, mai incearca :D '), castiga
    if o_castiga:
        castiga = True
        return print('Castigatorul este', nume_jucator.upper(), 'BRAVOS' '\n--Runda Terminata--\n'), castiga
    if a1 != '-' and a2 != '-' and a3 != '-' and a4 != '-' and a5 != '-' and a6 != '-' and a7 != '-' and a8 != '-' and a9 != '-':
        remiza = True
        return print('Egalitate'), remiza

def verifica_o():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, command_2
    validare_reincercare = False
    if command_2 == 1 and a1 == '-':
        a1 = O
    elif command_2 == 2 and a2 == '-':
        a2 = O
    elif command_2 == 3 and a3 == '-':
        a3 = O
    elif command_2 == 4 and a4 == '-':
        a4 = O
    elif command_2 == 5 and a5 == '-':
        a5 = O
    elif command_2 == 6 and a6 == '-':
        a6 = O
    elif command_2 == 7 and a7 == '-':
        a7 = O
    elif command_2 == 8 and a8 == '-':
        a8 = O
    elif command_2 == 9 and a9 == '-':
        a9 = O
    elif command_2 == 1 and a1 != '-' or command_2 == 2 and a2 != '-' or command_2 == 3 and a3 != '-' or command_2 == 4 and a4 != '-' or command_2 == 5 and a5 != '-' or command_2 == 6 and a6 != '-' or command_2 == 8 and a8 != '-' or command_2 == 7 and a7 != '-' or command_2 == 9 and a9 != '-':
        while not validare_reincercare:
            command_2 = int(input("Nu poti sa pui acolo, este deja completat"))
            verifica_o()
            validare_reincercare = True
    elif command_2 > 9:
        validare_reincercare = False
        while not validare_reincercare:
            command_2 = int(input("Selecteaza un numar de la 1 la 9 numai: "))
            verifica_o()
            validare_reincercare = True

    return a1, a2, a3, a4, a5, a6, a7, a8, a9


def verifica_x():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, command
    validare_reincercare = False
    if command == 1 and a1 == '-':
        a1 = X
    elif command == 2 and a2 == '-':
        a2 = X
    elif command == 3 and a3 == '-':
        a3 = X
    elif command == 4 and a4 == '-':
        a4 = X
    elif command == 5 and a5 == '-':
        a5 = X
    elif command == 6 and a6 == '-':
        a6 = X
    elif command == 7 and a7 == '-':
        a7 = X
    elif command == 8 and a8 == '-':
        a8 = X
    elif command == 9 and a9 == '-':
        a9 = X
    elif command == 1 and a1 != '-' or command == 2 and a2 != '-' or command == 3 and a3 != '-' or command == 4 and a4 != '-' or command == 5 and a5 != '-' or command == 6 and a6 != '-' or command == 8 and a8 != '-' or command == 7 and a7 != '-' or command == 9 and a9 != '-':
        while not validare_reincercare:
            command = int(input("Nu poti sa pui acolo"))
            verifica_x()
            validare_reincercare = True
    elif command > 9:
        validare_reincercare = False
        while not validare_reincercare:
            command = int(input("Selecteaza un numar de la 1 la 9:"))
            verifica_x()
            validare_reincercare = True
    return a1, a2, a3, a4, a5, a6, a7, a8, a9


# Tura BOTULUI
def tura_npc():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, command
    global npc_alege
    npc_alege = False
    alegeri_npc = (3, 5 ,7 ,9, 1, 2, 4, 6, 8)
    while not npc_alege:
        command = None
        # alege prima cifra din alegeri_npc care e valabila in loc sa faca random
        for picks in alegeri_npc:
            if picks == 3 and a3 == '-':
                command = 3
                break
            elif picks == 5 and a5 == '-':
                command = 5
                break
            elif picks == 7 and a7 == '-':
                command = 7
                break
            elif picks == 9 and a9 == '-':
                command = 9
                break
            elif picks == 1 and a1 == '-':
                command = 1
                break
            elif picks == 2 and a2 == '-':
                command = 2
                break
            elif picks == 4 and a4 == '-':
                command = 4
                break
            elif picks == 6 and a6 == '-':
                command = 6
                break
            elif picks == 8 and a8 == '-':
                command = 8
                break
        #         incepe sa verifice fiecare alegere si sa puna x in locurile definite mai sus
        if command == 3 and a3 == '-':
            a3 = X
            npc_alege = True
        elif command == 5 and a5 == '-':
            a5 = X
            npc_alege = True
        elif command == 7 and a7 == '-':
            a7 = X
            npc_alege = True
        elif command == 9 and a9 == '-':
            a9 = X
            npc_alege = True
        elif command == 1 and a1 == '-':
            a1 = X
            npc_alege = True
        elif command == 2 and a2 == '-':
            a2 = X
            npc_alege = True
        elif command == 4 and a4 == '-':
            a4 = X
            npc_alege = True
        elif command == 6 and a6 == '-':
            a6 = X
            npc_alege = True
        elif command == 8 and a8 == '-':
            a8 = X
            npc_alege = True
    return a1, a1, a3, a4, a5, a6, a7, a8, a9, print('Eu ALEG', command)

# un mic loop
while True:
    a1 = '-'
    a2 = '-'
    a3 = '-'
    a4 = '-'
    a5 = '-'
    a6 = '-'
    a7 = '-'
    a8 = '-'
    a9 = '-'
    nume_jucator = 'Player Neo'
    nume_jucator1 = 'NPC'
    x_castiga = False
    o_castiga = False
    npc_alege = False
    castiga = False
    remiza = False

# input cu niste conditii si mesaj de le NPC
    input_1 = input('>X si 0> (scrie incepe sau retry) ').lower()
    if input_1 == 'incepe' or input_1 == 'retry':
        ai = input('Vrei sa joci impotriva MEA :D ?: ')
        joc_inceput = True
        print('Eu sunt un NPC si o sa incerc sa te rup.')
        nume_jucator = input('Cum te Cheama? ')
        print("Hai sa vedem care pe care.")
        print(' ', 1, '|', 2, '|', 3, '\n ---------- \n', '', 4, '|', 5, '|', 6, '\n ----------\n', '', 7,
                  '|', 8, '|', 9, '\n')

        while ai == 'da' or ai == 'yes' or ai == 'sigur' or ai == 'go' or ai == 'bot':
            print('Yo eu sunt NPC.')
            nume_jucator1 = 'NPC'
            print("Hai sa incepem", nume_jucator.upper(), '\n\n')
            print(' ', 1, '|', 2, '|', 3, '\n ---------- \n', '', 4, '|', 5, '|', 6, '\n ----------\n', '', 7,
                  '|', 8, '|', 9, '\n')
# isi face tura aici el primul cu X
            print("NPC alege Acum")
            tura_npc()
            print('\n ', a1, '|', a2, '|', a3, '\n ---------- \n', '', a4, '|', a5, '|', a6, '\n ----------\n', '',
                  a7, '|', a8, '|', a9, '\n')
            conditii_castig()
            if castiga or remiza:
                break
# dupa aia pui tu 0 dupa el
            command_2 = int(input('>> Unde vrei sa pui 0? (doar cifre intre 1-9): '))
            verifica_o()
            print('\n ', a1, '|', a2, '|', a3, '\n ---------- \n', '', a4, '|', a5, '|', a6, '\n ----------\n', '',
                  a7, '|', a8, '|', a9, '\n')
            conditii_castig()
            if castiga or remiza:
                break
    else:
        print("Hopa-asa ceva nu a mers bine")