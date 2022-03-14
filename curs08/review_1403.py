class ClasaMea:
    gamma = 0   # atribut / variabila de clasa

    def __init__(self):     # constructor
        self.alpha = 1  # variabila de instanta
        self.__delta_ = 3   # variabila de instanta PRIVATA

obj = ClasaMea()    #instantiere a clasei ClasaMea
obj.beta = 2    # variabila de instatnta si poate exista doar in interiorul obj
print(obj.__dict__)
print(obj.alpha)
print(obj.gamma)
print(ClasaMea.gamma)
print(obj._ClasaMea__delta_)     # accesare private

