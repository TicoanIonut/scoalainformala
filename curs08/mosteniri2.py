# class Star:
#     def __init__(self, nume, galaxie):
#         self.name = nume
#         self.galaxy = galaxie
#
#     def __str__(self):
#         return f"{self.name} este in {self.galaxy}"
#
#
# soare = Star('Soarele', "Calea Lacteei")
# print(soare)


class SuperClass:
    supVar = 1
    variabila_clasa = 6

    def __init__(self, nume):
        self.name = nume
        # self.var1 = 101

    def __str__(self):
        return f"Numele meu esre {self.name}"


class Clasa3:
    variabila_clasa = 5

    def __init__(self, nume):
        self.name = nume
        self.var2 = 201
        self.var1 = 101

    def prima_metoda(self):
        pass


class SubClass(Clasa3, SuperClass):
    subVar = 2
    supVar = 3

    def __init__(self, nume):
        # self.var1 = 202
        # print(self.var1)
        super(). __init__(nume)
        self.var3 = 301
        self.var1 = 203

    def __str__(self):
        return f'Nume'


obiect = SubClass('ILIESCU! si sunt Vampir HAHAHA!')
# print(obiect.subVar)
# print(obiect.supVar)
# print(obiect.variabila_clasa)
# print(obiect.var3, obiect.var2, obiect.var1)
print(obiect.var1)
