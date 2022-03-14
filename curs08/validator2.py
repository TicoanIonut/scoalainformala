class Validator:
    def __init__(self, cnp):
        self.CNP = cnp

    def lungime(self):
        if len(self.CNP) != 13:
            return False
        return True

    def __str__(self):
        if self.lungime() is True:
            return f'CNP: {self.CNP} este valid.'
        return f'CNP: {self.CNP} nu este valid.'


obiect_1 = Validator(input('Introdu CNP: '))
print(obiect_1)
