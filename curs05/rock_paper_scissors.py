from random import choice

nume_jucator = input('Cum te cheama?')

print('Optiunile tale sunt\npiatra\nfoarfece\nhartie')

while True:

    alegere_jucator = input('Alege o optiune:')
    alegeri_totale = ['piatra', 'foarfece', 'hartie']
    alege_calculator = choice(alegeri_totale)

    print(f'Tu ai ales {alegere_jucator}, si NPCul a ales {alege_calculator}')

    if alegere_jucator == alege_calculator:
        print('Ati ales amandoi acelas lucru. Incearca din nou.')
    elif alegere_jucator == 'piatra' and alege_calculator == 'foarfece':
        print('Piatra bate foarfeca.Ai castigat')
    elif alegere_jucator == 'foarfece' and alege_calculator == 'hartie':
        print('Piatra bate foarfeca.Ai castigat')
    elif alegere_jucator == 'hartie' and alege_calculator == 'piatra':
        print('Hartie bate piatra.Ai castigat')
    elif alegere_jucator == 'foarfece' and alege_calculator == 'piatra':
        print('Piatra bate foarfeca.Ai pierdut')
    elif alegere_jucator == 'hartie' and alege_calculator == 'foarfece':
        print('Piatra bate foarfeca.Ai pierdut')
    elif alegere_jucator == 'piatra' and alege_calculator == 'hartie':
        print('Hartie bate piatra.Ai pierdut')
    restart_joc = input('vrei sa joci din nou? da sau nu:')
    if restart_joc != 'da':
        break