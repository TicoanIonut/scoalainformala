from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Keyboard('jscKeyboard', 1000, 3)
item1.apply_discount()
print(item1.price)
# item1 = Phone('jscPhone', 1000, 3)
# item1.apply_increment(0.2)
# item1.send_email()
# print(item1.price)
# item1 = Item('MyItem', 750)
# item1.name = 'OtherItem'
# print(item1.name)
# item1.apply_increment(0.2)
# item1.apply_discount()
# print(item1.price)
# item1 = Item('MyItem', 750, 6)
# item1.send_email()


# phone1 = Phone('jscPhonev10', 500, 5, 1)
# print(Item.all)
# print(Phone.all)
# print(phone1.calculate_total_price())
# phone2 = Phone('jscPhonev20', 700, 5, 1)

# print(Item.is_integer(7.5))
# print(Item.is_integer(7))

# Item.instantiate_from_csv()

# item1 = Item('Phone', 100, 1)
# item2 = Item('Laptop', 1000, 3)
# item3 = Item('Cable', 10, 5)
# item4 = Item('Mouse', 50, 5)
# item5 = Item('Keyboard', 75, 5)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)
