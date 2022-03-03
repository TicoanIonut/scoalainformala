def suma(a: int, b: int) -> str:
    return f"{a} + {b} = {a+b}"


def diferenta(a: int, b: int) -> str:
    return f"{a} - {b} = {a-b}"


def inmultire(a: int, b: int) -> str:
    return f"{a} * {b} = {a*b}"


def impartire(a: int, b: int) -> (str, float):
    if b == 0:
        while b == 0:
            b = input('aloca o noua valoare pentru b:')
    if a % b == 0:
        c = int(a/b)
    else:
        c = float(a/b)
    return f"{a} / {b} = {c}"


def operator() -> str:
    op = input('alege operatorul: ')
    if op not in ['*', '/', '+', '-']:
        while op not in ['*', '/', '+', '-']:
            op = input('alege operatorul: ')
    return op


def conversie(mesaj_input: str):
    nr = input(f"{mesaj_input}")
    while nr.isdigit() is False:
        nr = input(f'{mesaj_input}')
    return int(nr)


def calculator():
    nr1 = conversie('primul numar: ')
    op = operator()
    nr2 = conversie('al doilea numar: ')
    if op == '+':
        rezultat = suma(nr1, nr2)
    elif op == '-':
        rezultat = diferenta(nr1, nr2)
    elif op == '*':
        rezultat = inmultire(nr1, nr2)
    elif op == '/':
        rezultat = impartire(nr1, nr2)
    return rezultat

    # return f"{nr1}{op}{nr2}=", eval(f"{nr1}{op}{nr2}")


print(calculator())
