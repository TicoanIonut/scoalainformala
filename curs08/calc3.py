class Calculator:
    def __init__(self, op1, oper, op2):
        self.operator1 = op1
        self.oper = oper
        self.operator2 = op2

    def __add__(self):
        return int(self.operator1) + int(self.operator2)

    def __sub__(self):
        return int(self.operator1) - int(self.operator2)

    def __mul__(self):
        return int(self.operator1) * int(self.operator2)

    def __floordiv__(self):
        return int(self.operator1) / int(self.operator2)

    def __str__(self):
        if self.oper == '+':
            return f"{self.operator1} + {self.operator2} = {self.__add__()}"
        if self.oper == '-':
            return f"{self.operator1} - {self.operator2} = {self.__sub__()}"
        if self.oper == '*':
            return f"{self.operator1} * {self.operator2} = {self.__mul__()}"
        if self.oper == '/':
            try:
                return f"{self.operator1} / {self.operator2} = {self.__floordiv__()}"
            except ZeroDivisionError:
                return 'Can not divide to zero'


nr1 = input("Introduceti primul numar: ")
while nr1.isdigit() is False:
    nr1 = input("Introduceti al doilea numar: ")
simbol_operatie = input("Introduceti tipul operatiei: ")
while simbol_operatie not in ['*', '/', '+', '-']:
    simbol_operatie = input('Introduceti tipul operatiei: ')
nr2 = input("Introduceti al doilea numar: ")
while nr2.isdigit() is False:
    nr2 = input("Introduceti al doilea numar: ")
print(Calculator(nr1, simbol_operatie, nr2))
