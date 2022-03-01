class Calculator:

    def __init__(self, op1, op2, operation):
        self.operator1 = op1
        self.operator2 = op2
        self.operatie = operation

    def adunare(self):
        return self.operator1 + self.operator2

    def scadere(self):
        return self.operator1 - self.operator2

    def inmultire(self):
        return self.operator1 * self.operator2

    def impartire(self):
        return self.operator1 / self.operator2

    def __str__(self):
        if self.operatie == '+':
            return f"{self.adunare()}"
        if self.operatie == '-':
            return f"{self.scadere()}"
        if self.operatie == '*':
            return f"{self.inmultire()}"
        if self.operatie == '/':
            return f"{self.impartire()}"


nr1 = int(input("Introduceti primul operator: "))
nr2 = int(input("Introduceti al doilea operator: "))
simbol_operatie = input("Introduceti tipul operatiei: ")

obiect1 = Calculator(nr1, nr2, simbol_operatie)
print(obiect1)
