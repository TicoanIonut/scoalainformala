class Catalog:

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.absente = 0
        self.materii = {}

    def __str__(self):
        return f'{self.nume} {self.prenume} \n\tmaterii: {self.materii}\n\tavsente: {self.absente}'

    def increment(self):
        self.absente += 1

    def delete_abs(self, numar_absente):
        if self.absente > numar_absente:
            self.absente -= numar_absente


class Extensie1(Catalog):

    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)

    def add_subject(self, materie, note):
        self.materii.update({materie: note})

    def print_all(self):
        return f'{self.materii.keys()}'

    def final_grade(self):
        notefinale = {}
        for i, j in self.materii.items():
            if all(isinstance(x, int) for x in j):
                media = sum(j)/len(j)
                notefinale.update({i: media})
        return notefinale


student = Catalog('Roata', 'Ion')
print(student)
student.increment()
student.increment()
student.increment()
print(student)
student.delete_abs(2)
print(student)
student2 = Catalog('Cerc', 'George')
student2.increment()
student2.increment()
student2.increment()
student2.increment()
student2.delete_abs(2)
print(student2)
obj = Extensie1('Ana', 'Marie')
obj.add_subject('Python', [5, 7, 9])
obj.add_subject('Java', [3, 5, 9])
print(obj.final_grade())
