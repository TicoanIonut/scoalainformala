# from operator import itemgetter

class CatalogPrajituri:
    lista_cat = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        self.lista_cat.append(self.nume)
        self.lista_cat.append(self.pret)
        self.lista_cat.append(self.gramaj)

    # @staticmethod
    # def sortare():
    #     sort_nume = sorted(CatalogPrajituri.lista_cat, key=itemgetter(0))
    #     sort_pret = sorted(CatalogPrajituri.lista_cat, key=itemgetter(1))
    #     sort_gram = sorted(CatalogPrajituri.lista_cat, key=itemgetter(2))
    #     return sort_nume, sort_pret, sort_gram

    def __str__(self):
        return f'nume: {self.nume}\npret: {self.pret}\ngramaj: {self.gramaj}'


class Tort(CatalogPrajituri):
    def __init__(self, nume, pret, gramaj, etajat=False, glazura='ciocolata'):
        super().__init__(nume, pret, gramaj)
        self.etajat = etajat
        self.glazura = glazura

    def __str__(self):
        return f'etajare {self.etajat} glazura: {self.glazura}'


class Fursec(CatalogPrajituri):
    def __init__(self, nume, pret, gramaj):
        super().__init__(nume, pret, gramaj)


cat_p1 = CatalogPrajituri('Brownie', 15, 100)
cat_p2 = CatalogPrajituri('Preajutura cu branza', 18, 80)
cat_p3 = CatalogPrajituri('Prajutura cu mere', 17, 70)
print(CatalogPrajituri.lista_cat)
tort1 = Tort('Banana tort', 55, 250)
tort2 = Tort('Choco tort', 42, 350)
tort3 = Tort('Cheese tort', 77, 300, True, 'migdale')
tort2.etajat = True
tort1.glazura = 'frisca'
print(tort1.glazura)
print(tort2.etajat)
print(tort3)
fursec1 = Fursec('Furesc gem', 5, 22)
fursec2 = Fursec('Fursec cioco', 8, 33)
fursec3 = Fursec('Furesc vanilie', 7, 26)
print(CatalogPrajituri.lista_cat)
# print(fursec1)
# print(fursec2)
# print(fursec3)
# print(CatalogPrajituri.sortare())
