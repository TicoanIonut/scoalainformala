class Calculator:

    def __init__(self, op1, oper, op2):
        self.operator1 = op1
        self.oper = oper
        self.operator2 = op2

    def __add__(self):
        return self.operator1 + self.operator2

    def __sub__(self):
        return self.operator1 - self.operator2

    def __mul__(self):
        return self.operator1 * self.operator2

    def __floordiv__(self):
        return self.operator1 / self.operator2

    def __truediv__(self):
        return self.operator1 // self.operator2

    def __mod__(self):
        return self.operator1 // self.operator2

    def __str__(self):
        if self.oper == '+':
            return f"{self.__add__()}"
        if self.oper == '-':
            return f"{self.__sub__()}"
        if self.oper == '*':
            return f"{self.__mul__()}"
        if self.oper == '/':
            return f"{self.__floordiv__()}"
        if self.oper == '//':
            return f"{self.__truediv__()}"
        if self.oper == '%':
            return f"{self.__mod__()}"


nr1 = int(input("Introduceti primul numar: "))
simbol_operatie = input("Introduceti tipul operatiei: ")
nr2 = int(input("Introduceti al doilea numar: "))
print(Calculator(nr1, simbol_operatie, nr2))
