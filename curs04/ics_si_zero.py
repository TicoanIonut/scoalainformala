#Alegerea incepatorului
#Alegerea unei pozitii
#scrierea algoritmului dupa care se lucreaza
import random

castiga = 0
pierde = 0
X = 'X'
O = 'O'

def conditii_castig():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9
    global O_castiga, X_castiga, remiza
    global nume_jucator
    global castiga
    if a1 == 'X' and a2 == 'X' and a3 == 'X':
        X_castiga = True
    elif a4 == 'X' and a5 == 'X' and a6 == 'X':
        X_castiga = True
    elif a7 == 'X' and a8 == 'X' and a9 == 'X':
        X_castiga = True
    elif a1 == 'X' and a4 == 'X' and a7 == 'X':
        X_castiga = True
    elif a2 == 'X' and a5 == 'X' and a8 == 'X':
        X_castiga = True
    elif a3 == 'X' and a6 == 'X' and a9 == 'X':
        X_castiga = True
    elif a1 == 'X' and a5 == 'X' and a9 == 'X':
        X_castiga = True
    elif a3 == 'X' and a5 == 'X' and a7 == 'X':
        X_castiga = True
    elif a1 == 'O' and a2 == 'O' and a3 == 'O':
        O_castiga = True
    elif a4 == 'O' and a5 == 'O' and a6 == 'O':
        O_castiga = True
    elif a7 == 'O' and a8 == 'O' and a9 == 'O':
        O_castiga = True
    elif a1 == 'O' and a4 == 'O' and a7 == 'O':
        O_castiga = True
    elif a2 == 'O' and a5 == 'O' and a8 == 'O':
        O_castiga = True
    elif a3 == 'O' and a6 == 'O' and a9 == 'O':
        O_castiga = True
    elif a1 == 'O' and a5 == 'O' and a9 == 'O':
        O_castiga = True
    elif a3 == 'O' and a5 == 'O' and a7 == 'O':
        O_castiga = True
    if O_castiga:
        castiga = True
    if X_castiga:
        castiga = True
        return print('A castigat', nume_jucator.upper(), '\n--NPC-ul a pierdut :( --\n'), castiga
    if a1 != '-' and a2 != '-' and a3 != '-' and a4 != '-' and a5 != '-' and a6 != '-' and a7 != '-' and a8 != '-' and a9 != '-':
        remiza = True
        return print('Egalitate'), remiza

def verifica_0():
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
            verifica_0()
            validare_reincercare = True
    elif command_2 > 9:
        validare_reincercare = False
        while not validare_reincercare:
            command_2 = int(input("Selecteaza un numar de la 1 la 9 numai:"))
            verifica_0()
            validare_reincercare = True

    return a1, a2, a3, a4, a5, a6, a7, a8, a9
#    print("asd", command)



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

def tura_calculator():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, command
    global npc_alege
    npc_alege = False
    while not npc_alege:
        command = random.randrange(1, 10)
        if command == 5 and a5 == ' ':
            a1 = 0
            npc_alege = True
        elif command == 1 and a1 == ' ':
            a5 = 0
            npc_alege = True
        elif command == 3 and a3 == ' ':
            a3 = 0
            npc_alege = True
        elif command == 7 and a7 == ' ':
            a7 = 0
            npc_alege = True
        elif command == 9 and a9 == ' ':
            a9 = 0
            npc_alege = True
        elif command == 2 and a2 == ' ':
            a2 = 0
            npc_alege = True
        elif command == 4 and a4 == ' ':
            a4 = 0
            npc_alege = True
        elif command == 6 and a6 == ' ':
            a6 = 0
            npc_alege = True
        elif command == 8 and a8 == ' ':
            a8 = 0
            npc_alege = True
    return a1, a2, a3, a4, a5, a6, a7, a8, a9, print("asd", command)

while True:
    a1 = '_'
    a2 = '_'
    a3 = '_'
    a4 = '_'
    a5 = '_'
    a6 = '_'
    a7 = '_'
    a8 = '_'
    a9 = '_'

#Board = {a1: ' ', a2: ' ', a3: ' ',
#            a4: ' ', a5: ' ', a6: ' ',
#            a7: ' ', a8: ' ', a9: ' '}
#def printBoard(board):
#    print(board['1'] + '  |'+board['2']+'  |'+board['3'])
#    print('---|---|---')
#    print(board['4'] + '  |'+board['5']+'  |' + board['6'])
#    print('---|---|---')
#    print(board['7'] + '  |'+board['8']+'  |' + board['9'])
#printBoard(Board)

#pozitii_jucator = {'x':[], '0':[]}

jucator = ['Human', 'Robot']
#print(random.choice(jucator))

#castig = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

if random.choice(jucator) == 'Human':
    input("Jucatorul alege prima mutare")
else:
    print("Robotul alege prima mutare")
    tura_calculator()