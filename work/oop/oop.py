# class Rectangle:
#     def __init__(self, width, height):
#         self.w = width
#         self.h = height
#     def vol(self):
#         return self.w * self.h
# w = int(input())
# h = int(input())
# obj = Rectangle(w, h)
# print(obj.vol())

# class Vehicle:
#     def horn(self):
#         print('beep')
# class Car(Vehicle):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# obj = Car('bmw', 'red')
# obj.horn()

class BankAccount:
	def __init__(self, balance):
		self.balance = balance
	
	def __add__(self, other):
		return BankAccount(self.balance + other.balance)


a = BankAccount(111)
b = BankAccount(11)
res = a + b
print(res.balance)


class Player:
	def __init__(self, name, lives):
		self.name = name
		self._lives = lives
	
	def hit(self):
		self._lives -= 1
	
	@property
	def isalive(self):
		if self._lives > 0:
			return True


p = Player('yolo', int(input('Cyberpunk\t')))
i = 1
while True:
	p.hit()
	print('Hi # ' + str(i))
	i += 1
	if not p.isalive:
		print('Game Over')
		break
