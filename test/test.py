class Cake:
   __cake_list = []
   def __init__(self, name: str, price: int, quantity: int):
       self.name = name
       self.price = price
       self.quantity = quantity
       self.__cake_list.append(self)
   @staticmethod
   def print_a_cake(cake):
       print(f'Cake named {cake.name}, quantity of {cake.quantity}g, at the price of ${cake.price};')
   @staticmethod
   def print_a_list_of_cakes( cake_list: []):
       for cake in cake_list:
           Cake.print_a_cake(cake)
   def show_cake_list_by_price(self):
       sorted_cake_list = sorted(self.__cake_list, key= lambda item: item.price, reverse=True)
       Cake.print_a_list_of_cakes(sorted_cake_list)
   def show_cake_list_by_quantity(self):
       sorted_cake_list = sorted(self.__cake_list, key=lambda item: item.quantity, reverse=True)
       Cake.print_a_list_of_cakes(sorted_cake_list)
class Tort(Cake):
   __etajat = False
   __glazura = "ciocolata"
   def change_etajat(self, etajat: bool):
       self.__etajat = etajat
   def change_glazura(self, glazura: str):
       self.__glazura = glazura
   def show_options(self):
       print(f'Tortul {"" if self.__etajat else "nu "}este etajat iar glazura este de {self.__glazura}')
class Fursec(Cake):
   pass
tort_1 = Tort('Alcazar', 150, 1250)
tort_2 = Tort('Choco', 125, 1500)
tort_3 = Tort('Fruits', 75, 1050)
fursec_1 = Fursec('Mini', 1, 15)
fursec_2 = Fursec('Medium', 2, 25)
fursec_3 = Fursec('Campion', 5, 75)
tort_3.change_glazura('iaurt')
tort_3.change_etajat(True)
print('Cakes by quantity')
Cake.show_cake_list_by_quantity(Cake)
print('Cakes by price')
Cake.show_cake_list_by_price(Cake)
print('Cake special options')
tort_3.show_options()