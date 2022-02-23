import datetime
cnp = input('enter CNP: ')


def cnpp():
    if len(cnp) == 13 and cnp.isdigit():
        return cnp


def sss():
    s = '123456789'
    if cnpp()[0] in s:
        return True


def data():
    try:
        date = cnpp()[1:7]
        if datetime.datetime.strptime(date, "%y%m%d"):
            return True
    except ValueError:
        return False


def judet():
    jud = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
           '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '51', '52']
    if cnpp()[7:9] in jud:
        return True


def nnn():
    nnn = cnpp()[9:12]
    if nnn != 000:
        return True


def cif_control():
    intcnp = int(cnpp()[-1])
    val = '279146358279'
    cnpc = 0
    for i, v in enumerate(val):
        cnpc += int(v) * int(cnpp()[i])
    rest = cnpc % 11
    if rest == 10:
        rest = 1
    else:
        rest = rest
    if intcnp == rest:
        return True


def validare():
    if cnpp() and sss() and data() and judet() and cif_control() and nnn():
        return f'CNP valid: {cnpp()}'
    else:
        return 'CNP invalid, mai incearca'


print(validare())
