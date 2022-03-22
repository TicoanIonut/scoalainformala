class Catalog_prajituri:
    lista_cat = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj



    def sortare(self):
        return self.lista_cat

    def __str__(self):
        return f'nume: {self.nume}\npret: {self.pret}\ngramaj: {self.gramaj}'


class Tort(Catalog_prajituri):
    def __init__(self, nume, pret, gramaj):
        super().__init__(nume, pret, gramaj)
        self.etajat = False
        self.glazura = 'ciocolata'

    def setare(self):
        self.etajat = False
        self.glazura = 'ciocolata'


class Fursec(Catalog_prajituri):
    def __init__(self, nume, pret, gramaj):
        super().__init__(nume, pret, gramaj)


cat_p1 = Catalog_prajituri('Brownie', 15, 100)
cat_p2 = Catalog_prajituri('Preajutura cu branza', 18, 80)
cat_p3 = Catalog_prajituri('Prajutura cu mere', 17, 70)
Catalog_prajituri.lista_cat.append(cat_p1)
Catalog_prajituri.lista_cat.append(cat_p2)
Catalog_prajituri.lista_cat.append(cat_p3)
print(Catalog_prajituri.sortare)
tort1 = Tort('Banana tort', 55, 250)
tort2 = Tort('Choco tort', 42, 350)
tort3 = Tort('Cheese tort', 77, 300)
tort2.etajat = True
tort1.glazura = 'frisca'
print(tort1.glazura)
print(tort2.etajat)
print(tort3)
fursec1 = Fursec('Furesc gem', 5, 22)
fursec2 = Fursec('Fursec cioco', 8, 33)
fursec3 = Fursec('Furesc vanilie', 7, 26)
print(fursec1)
print(fursec2)
print(fursec3)
