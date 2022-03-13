class Fractii:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __add__(self):
        return self.numarator + self.numitor

    def __sub__(self):
        return self.numarator - self.numitor

    def invers(self):
        return self.numitor / self.numarator

    def __str__(self):
        return f"{self.__add__()}\n" + f"{self.__sub__()}\n" + f"{self.numarator/self.numitor}\n" + f"{self.invers()}"


n1 = int(input('Introdu numarator '))
n2 = int(input('Introdu numitor '))
print(Fractii(n1, n2))
