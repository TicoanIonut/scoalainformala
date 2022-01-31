#alegerea incepatorului
#alegera unei pozitii
#scrierea algorimului
# board ={a1:'',a2:'',a3:'',
#         a4'',a5:'',a6:'',
#         a7:'',a8:'',a9:'',}

def draw_board(board):
    board[0]=-1
    #draw first row
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")
    print("-"*11)
    #draw second row
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("   |   |   ")
    print("-"*11)
    #draw third row
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("   |   |   ")
    print("-"*11)
    return board


import random
jucator = ['Human', 'Robot']

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

def tura_calculator():
    global a1,a2,a3,a4,a5,a6,a7,a8,a9,command
    global npc_alege
    npc_alege = False
    while not npc_alege:
        command = random.randrange(1, 10)
    if command == 5 and a5 == ' ':
        a1 = 0
        npc_alege = True
    elif command == 1 and a1 == ' ':
        a1 = 0
        npc_alege = True
    elif command == 3 and a3 == ' ':
        a1 = 0
        npc_alege = True
    elif command == 7 and a7 == ' ':
        a1 = 0
        npc_alege = True
    elif command == 9 and a9 == ' ':
        a1 = 0
        npc_alege = True
    elif command == 2 and a2 == ' ':
        a1 = 0
        npc_alege = True
    elif command == 4 and a4 == ' ':
        a1 = 0
        npc_alege = True
    elif command == 6 and a6 == ' ':
        a1 = 0
        npc_alege = True
    elif command == 8 and a8 == ' ':
        a1 = 0
        npc_alege = True
    return a1,a2,a3,a4,a5,a6,a7,a8,a9,print('calculatorul', command)

while True:
    a1='_'
    a2='_'
    a3='_'
    a4='_'
    a5='_'
    a6='_'
    a7='_'
    a8='_'
    a9='_'




if random.choice(jucator) == jucator[0]:
    input("Jucatorul alege prima mutare")

if random.choice(jucator) == jucator[1]:
    print("Robotul alege prima mutare")







