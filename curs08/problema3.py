# class CatalogAuto:
#     def __init__(self, marca , tip):
#         self.marca = marca
#         self.tip = tip
#
#     def schimb_culoare(self, culoare):
#         self.culoare = culoare
#
#     def __str__(self):
#         return f"Culoarea este :{self.culoare}"
#
# class ScauneIncalzite(CatalogAuto):
#     def __init__(self, scaune_incalzite, marca, tip):
#         super().__init__(marca, tip)
#         self.scaune_incalzite = scaune_incalzite
#     def __str__(self):
#         return f"Marca este :{self.marca},\n Tipul este:{self.tip},\n Scaune incalzite :{self.scaune_incalzite}"
#
# class BlocuriOpticeLDED(CatalogAuto):
#     def __init__(self, blocuri_optice_led, marca, tip):
#         super().__init__(marca, tip)
#         self.blocuri_optice_led = blocuri_optice_led
#
#
#     def __str__(self):
#          return f"Marca este :{self.marca},\n Tipul este:{self.tip},\n Blocuri optice:{self.blocuri_optice_led}"
#
#
# obj = ScauneIncalzite(marca="ARO", tip=461, scaune_incalzite= "NU")
# print(obj)
# obj.schimb_culoare("rosu")
# print(obj.culoare)

class Calcul:
    def __init__(self, a=1, b=2, c=3, d=4):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def verificare(self):
        self.e = f'mesaj gresit'
        if str(self.a).isnumeric() and str(self.b).isnumeric() and str(self.c).isnumeric() and str(self.d).isnumeric():
            self.e = (self.a * (self.b + 3) / self.c) * self.d
        return self.e

    def __str__(self):
        return f'{self.verificare()}'
obiect = Calcul()
print(obiect)
obiect2 = Calcul(5, 6, 7, 8)
print(obiect2)
ob3 = Calcul('x', 'y', 'z', 't')
print(ob3)
obj4 = Calcul(9, 2)
print(obj4)
