import datetime
import re
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
    jud = r'(0[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-6]|5[1-2])'
    if re.match(jud, cnpp()[7:9]):
        return True


def nnn():
    if cnpp()[9:12] != 000:
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
