class Fractii:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __add__(self):
        return int(self.numarator) + int(self.numitor)

    def __sub__(self):
        return int(self.numarator) - int(self.numitor)

    def __floordiv__(self):
        try:
            return int(self.numarator) / int(self.numitor)
        except ZeroDivisionError:
            return 'Can not divide to ZERO'

    def invers(self):
        try:
            return int(self.numitor) / int(self.numarator)
        except ZeroDivisionError:
            return 'Can not divide to ZERO'

    def __str__(self):
        return f"Adunare {self.__add__()}\n" + f"Scadere {self.__sub__()}\n" + \
                f"Fractia {self.__floordiv__()}\n" + f"Inverse {self.invers()}"


n1 = input('Introdu numarator ')
while n1.isdigit() is False:
    n1 = input('Introdu numarator ')
n2 = input('Introdu numitor ')
while n2.isdigit() is False:
    n2 = input('Introdu numarator ')
print(Fractii(n1, n2))
