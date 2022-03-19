class Telefon:
    counter = 0

    def __init__(self, numar):
        self.numar = numar
        Telefon.counter += 1

    def apelare(self, numar):
        mesaj = f'Apelati{numar} utilizand propriul numar de telfon'
        return mesaj


class TelefonFix(Telefon):
    last_sn = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonFix.last_sn += 1
        self.SN = f'Telefon fix -{TelefonFix.last_sn}'


class TelefonMobil(Telefon):
    last_sn = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonMobil.last_sn += 1
        self.SN = f'Telfon mobil - {TelefonMobil.last_sn}'


print(f'Numarul total de dispozitive este {Telefon.counter}')
fix1 = TelefonFix('021 77 66 55')
fix2 = TelefonFix('031 66 33 88')
mobil = TelefonMobil('0741 45 67 89')
print(f'Numarul total de dispozitive fixe {TelefonFix.last_sn}')
print(f'Numarul total de dispozitive mobile {TelefonMobil.last_sn}')
print(f'Numarul total de dispozitive este {Telefon.counter}')
