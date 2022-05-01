# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_students(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
#
#
# s1 = Student('Tim', 19, 95)
# s2 = Student('Bill', 19, 75)
# s3 = Student('Jill', 19, 65)
#
# course = Course('Science', 2)
# course.add_students(s1)
# course.add_students(s2)
# print(course.average_grade())
class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def show(self):
		print(f"I am {self.name} and I am {self.age} years old.")
	
	def speak(self):
		print("I don't know what to say")


class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age)
		self.color = color
	
	def speak(self):
		print('Meow')
	
	def show(self):
		print(f"I am {self.name}, I am {self.age} years old and I am {self.color} Cat.")


class Dog(Pet):
	def speak(self):
		print('Wof')


class Fish(Pet):
	pass


p = Pet('Tim', 19)
p.speak()
c = Cat('Bill', 34, 'green')
c.show()
c.speak()
d = Dog('Jim', 22)
d.show()
d.speak()
f = Fish("Bubles", 2)
f.show()
f.speak()
