import datetime
import re


class Validator:
    def __init__(self, cnp):
        self.CNP = cnp

    def lungime(self):
        if len(self.CNP) != 13:
            return False
        return True

    def format(self):
        if self.CNP.isdigit():
            return True
        return False

    def sex(self):
        s = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if self.sex in s:
            return False
        return True

    def date(self):
        try:
            date = self.CNP[1:7]
            if datetime.datetime.strptime(date, "%y%m%d"):
                return True
        except ValueError:
            return False

    def judet(self):
        jud = r'(0[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-6]|5[1-2])'
        if re.match(jud, self.CNP[7:9]):
            return True
        return False

    def nnn(self):
        nnn = self.CNP[9:12]
        if nnn != 000:
            return True
        return False

    def cifcontrol(self):
        intcnp = int(self.CNP[-1])
        val = '279146358279'
        cnpc = 0
        for i, v in enumerate(val):
            cnpc += int(v) * int(self.CNP[i])
        rest = cnpc % 11
        if rest == 10:
            rest = 1
        else:
            rest = rest
        if intcnp == rest:
            return True
        return False

    def __str__(self):
        if self.lungime() and self.sex() and self.date() and self.judet() and \
                self.cifcontrol() and self.nnn() and self.format() is True:
            return f'CNP: {self.CNP} este valid.'
        return f'CNP: {self.CNP} nu este valid.'


obiect_1 = Validator(input('Introdu CNP: '))
print(obiect_1)
