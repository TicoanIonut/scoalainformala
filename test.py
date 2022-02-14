import datetime
def cnpc():
    validare = '279146358279'
    cnpc = 0
    for i, v in enumerate(validare):
        cnpc += int(v) * int(cnp[i])

def datele():
    cnpc()
    an = '123456789'
    jud = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'
                , '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'
                , '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39'
                , '40', '41', '42', '43', '44', '45', '46', '51', '52']
    # cnpc = ((2 * cnp[0]) + (7 * cnp[1]) + (9 * cnp[2]) + (1 * cnp[3]) + (4 * cnp[4]) + (6 * cnp[5]) +
    #         (3 * cnp[6]) + (5 * cnp[7]) + (8 * cnp[8]) + (2 * cnp[9]) + (7 * cnp[10]) + (9 * cnp[11]))
    rest = sum(map(int, cnpc)) % 11
    date = cnp[1:7]
    intcnp = int(cnp[-1])

cnp = input('enterCNP:')

def cnpval():
    datele()
    cnpc()
    if datetime.datetime.strptime(date,"%y%m%d"):
        if len(cnp) == 13:
            if cnp[0] in an:
                if cnp[7:9] in jud:
                    if intcnp == rest:
                        return True
    return False


def call_cnp():
    try:
        if cnpval() == True:
             print(f'CNP Valid: {cnp}')
    except:
        print('CNP invalid, mai incearca')


