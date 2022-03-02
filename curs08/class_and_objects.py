# class MyFirstClass:
#     pass
#
#
# my_first_object = MyFirstClass()


# class Caine:
#     nr_picioare = 4   # atribu
#
#     def __init__(self, name, age=2):        # constructor creaza date
#         self.nume = name
#         self.varsta = age
#
#     def __str__(self):
#         return f"{self.nume} - {self.varsta}"
#
#     def change_name(self, name):
#         self.nume = name
#         return 'Ceva'
#
#
# # print(Caine.nr_picioare)
#
# cainele_meu = Caine('Rex')
# # print(cainele_meu.nume)
# # print(cainele_meu.change_name('Ben'))
# # print(cainele_meu)
# # print(cainele_meu.varsta)

class Calculator:
    def __init__(self, op1, op2, operation):
        self.operator1 = op1
        self.operator2 = op2
        self.operatie = operation

    def adunare(self):
        return self.operator1 + self.operator2

    def scadere(self):
        return self.operator1 - self.operator2

    def __str__(self):
        if self.operatie == '+':
            return f"{self.adunare()}"
        elif self.operatie == '-':
            return f"{self.scadere()}"


obiect1 = Calculator(1, 2, '+')
obiect2 = Calculator(1, 2, '-')
print(obiect1, obiect2)


def suma(a, b):
    return a + b


var1 = suma(1, 2)
var2 = suma(3, 2)
