import datetime


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
        jud = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
               '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
               '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '51', '52']
        if self.CNP[7:9] in jud:
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
