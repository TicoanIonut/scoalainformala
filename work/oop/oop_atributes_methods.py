# class Person:
#     number_of_people = 0
#
#     def __init__(self, names):
#         self.names = names
#         Person.add_person()
#
#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
#
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
#
#
# p1 = Person('Tim')
# p2 = Person('Jim')
# print(Person.number_of_people_())

# class Math:
#
#     @staticmethod
#     def add5(x):
#         return x + 5
#
#     @staticmethod
#     def pr():
#         print('run')
#
#
# print(Math.add5(5))
# Math.pr()
class User:
	def log(self):
		print(self)


class Teacher(User):
	def log(self):
		print("I'm a teacher ")


class Customer(User):
	
	def log(self):
		print(self)
	
	def __init__(self, name, membership_type):
		self.name = name
		self.membership_type = membership_type
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name):
		self._name = name
	
	# @name.deleter
	# def name(self):
	#     del self._name
	
	def update_membership(self, new_membership):
		print('Calculating costs')
		self.membership_type = new_membership
	
	def __str__(self):
		return self.name + '' + self.membership_type
	
	@staticmethod
	def print_all_customers(self):
		for customer in users:
			print(customer)
	
	def __eq__(self, other):
		if self.name == other.name and self.membership_type == other.membership_type:
			return True
		return False


users = [Customer('Caleb ', 'Gold'), Customer('John ', 'Bronze'), Teacher()]
for user in users:
	user.log()
