class Employee:
	num_of_emps = 0
	raise_amount = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		# self.email = first + '.' + last + '@company.com'
		self.pay = pay
	
	@property
	def email(self):
		return f'{self.first, self.last}@email.com'
	
	def fullname(self):
		return f'{self.first, self.last}'
	
	# def apply_raise(self):
	#     self.pay = int(self.pay * self.raise_amount)
	#
	# @classmethod
	# def set_raise_amount(cls, amount):
	#     cls.raise_amount = amount
	#
	# @classmethod
	# def from_string(cls, emp_str):
	#     first, last, pay = emp_str.split('-')
	#     return cls(first, last, pay)
	#
	# @staticmethod
	# def is_work_day(day):
	#     if day.weekday() == 5 or day.weekday == 6:
	#         return False
	#     return True
	#
	# class Developer(Employee):
	#     raise_amount = 1.10
	#
	#     def __init__(self, first, last, pay, prog_lang):
	#         super().__init__(first, last, pay)
	#         self.prog_lang = prog_lang
	#
	# class Manager(Employee):
	#     def __init__(self, first, last, pay, employees=None):
	#         super().__init__(first, last, pay)
	#         if employees is None:
	#             self.employees = []
	#         else:
	#             self.employees = employees
	#
	#     def add_emp(self, emp):
	#         if emp not in self.employees:
	#             self.employees.append(emp)
	#
	#     def remv_emp(self, emp):
	#         if emp in self.employees:
	#             self.employees.remove(emp)
	#
	#     def print_emp(self):
	#         for emp in self.employees:
	#             print('>>>', emp.fullname)


emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)
#
# enp_str_1 = 'John-Doe-70000'
# enp_str_2 = 'Steven-Smith-70000'
# enp_str_3 = 'Johne-Doe-90000'
#
# new_emp_1 = Employee.from_string((enp_str_1))
#
# import datetime
# my_date = datetime.date(2016, 11, 7)
#
print(emp_1.email)
