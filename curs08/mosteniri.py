# 1. Vehicul
# 1.1. vehicule de apa
# 1.2. Vehicule de aer
# 1.3. Vehicule de spatiu
# 1.4. Vehicule terestru
# 1.4.1. Vehicul de teren
# 1.4.2. Vehicul de curs
# 1. este superclasa 1.1 ->1.14
# 1.1 -> 1.4. este subclasa pentru 1.

# 2 Animale
# 2.1. Mamifere
# 2.1.1. Animale salbatice
# 2.1.2. Animale domestice
# 2.2. Reptile
# 2. pentru 2.1 si 2.2 este superclasa
# 2.1 si 2.2 pentru 2. sunt subclase
# 2.1.1. si 2.1.2. pentru 2.1. sunt subclase
# 2.1.1. si 2.1.2. pentru 2 sunt subclase

# Max este un caine mare care doarme toata ziua.
# obiectul -> Max (substantiv)
# clasa -> caine (substantiv)
# proprietatea -> mare (adjectiv)
# activitatea -> doarme (verb) -> metoda

# Un Logan verde merge incet
# obiect -> Logan
# clasea -> masina
# proprietate -> verde
# activitate -> merge incet

# Rudolph este o pisica mare care mananca multe boabe
# obiect -> Rudolph
# clasa -> pisica
# proprietate -> mare
# activitate -> mananca

# Lenovo-ul gri se poate cumpara la un pret mai mic de pe un magazin online
# obiect -> Lenovo
# clasa -> Laptop
# proprietate -> gri
# activitate -> se poate cumpara

# Sa se realizeze jocul x&0 intre 2 jucatori in care:
# primul jucator este mereu calculatorul
# exista reguli de joc pentru mutari
# obiectele -> calculator/om
# clasa -> jocul
# proprietate -> primul jucator este mereu calculatorul
# activitatea -> mutari/calcul de scor al jocului

# class MyFirstClass:
#     pass
# my_object = MyFirstClass()
#
# stack = []
#
#
# def push(val):
#     stack.append(val)
#     return stack
#
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
#
# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())
#
#
# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def __str__(self):
#         return f"{self.__stack_list}"
#
#
# obiect_stiva = Stack()
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
# print(obiect_stiva)
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())


# class ClasaExemplu:
#
#     def __init__(self, val=1):
#         self.first = val
#         self.second = 0
#
#     def set_second(self, val=2):
#         self.second = val
#
#     def __str__(self):
#         return f"{self.first} {self.second}"
#
#
# obiect_1 = ClasaExemplu()
# obiect_2 = ClasaExemplu(2)
# obiect_3 = ClasaExemplu(3)

# # print(obiect_1)
# # print(obiect_2)
# # print(obiect_3.set_second(3))
# print(obiect_3.second)

# class Caine:
#     nr_picioare = 4   # atribu
#
#     def __init__(self, name, vaccin, age=2):        # constructor creaza date
#         self.__nume = name
#         self.__varsta = age
#         self.__vaccinuri = vaccin
#         self.stare = 'tanar'
#         self.cumpara = 'mancare'
#         if self.__varsta == 4:
#             self.stare = 'batran'
#         else:
#             self.cumpara = 'jucarie'
#         # Caine.nr_picioare = 3
#
#     def __str__(self):
#         return f"{self.__nume} - {self.__varsta}"
#
#     def change_name(self, name):
#         self.__nume = name
#         return 'Ceva'
#
#
# obiect_1 = Caine('Rex', 10, 4)
# print(type(obiect_1).__name__)
# print(obiect_1.__dict__)
# print(obiect_1.cumpara)
# print(Caine.__dict__)
# print(hasattr(Caine, 'nr_picioare'))
# var2 =obiect_1.__dict__
# print(obiect_1._Caine__nume)
# print(obiect_1.nr_picioare, 'nr picioare')
# print(obiect_1.varsta, 'varsta')
# print(obiect_1.nume, 'nume')
# print(obiect_1.vaccinuri, 'vaccin')

# vehicul
# vehiculdeteren
# vehiculdetractare


class Vehicul:
    pass


class VehiculTeren(Vehicul):
    pass


class VehiculTractare(VehiculTeren):
    pass

# Vehicul este parinte pentru VehiculTeren si VehiculTractare(indirect)
# VehiculTeren este parinte pentru VehiculTractare
# parintii sunt superclase pentru copii (superclass)

# VehiculTractare este copil pentru VehiculTeren si Vehicul(indirect)
# VehiculTeren este copil pentru Vehicul
# copii se numesc subclase

# print('Vehicul VehiculTeren VehiculTractare')
# for cls1 in [Vehicul, VehiculTeren, VehiculTractare]:
#     for cls2 in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(issubclass(cls1, cls2), end='\t')     # issubclass asfiseaza relatiile dintre 2 clase
#    print()


vehicul1 = Vehicul()
vehicul_teren = VehiculTeren()
vehicul_tractare = VehiculTractare()
# print(isinstance(vehicul1, VehiculTeren))

# print('Vehicul VehiculTeren VehiculTractare')
# for obj in [vehicul1, vehicul_teren, vehicul_tractare]:
#     for cls in [vehicul1, vehicul_teren, vehicul_tractare]:
#         print(isinstance(obj, cls), end='\t')     # isinstance asfiseaza relatiile dintre 2 obiecte
#     print()


class Exemplu:

    def __init__(self, val):
        self.value = val

    def __str__(self):
        return f'{self.value}'


obiect_1 = Exemplu(0)
print(obiect_1.value, '223')
obiect_2 = Exemplu(2)
print(obiect_2.value, 225)
obiect_3 = obiect_1
obiect_1.value = 7
print(obiect_3, obiect_1.value, '227')
obiect_3.value += 1
a = obiect_1.value
b = obiect_2.value
c = obiect_3.value

# print(obiect_1 is obiect_2)
# print(obiect_2 is obiect_3)
# print(obiect_3 is obiect_1)
print(obiect_1.value, obiect_2.value, obiect_3.value)

# str1 = 'Maria are mere '
# str2 = str1
# str1 = 'www'
# # str2 = 'Maria are mere mari'
# # str1 += 'mari'
#
# print(str1 == str2, str1 is str2, str1, str2)
