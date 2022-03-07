# exercise 1
#
# num_calls = 0
#
# def exercitiu(x):
#     global num_calls
#     num_calls = 3
#     num_calls += 1
#     return  x * x
#
# print(exercitiu(4))
# correct response: b. 16 (a. 9; b.16; c.4; d. error)
#
# exercise 2
# x = 1
#
#
# def f():
#     return x
#
# print(x)
# print(f())
# correct response: c. 1 1 (a. error; b. 1; c. 1 1; d. 0 1)
#
# exercise 3
# x = [1, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))
#
# correct response: b.5 (a. TypeError; b. 5; c. 0; d. 2)
#
# exercise 4
#
# x = (1, 2, 3)
#
# x[1] = 4
#
# correct response: d. TypeError (a. x= (1, 2, 4); b. x= (1, 2, 3); c. x = [1, 2, 3]; d. TypeError
# TypeError: 'tuple' object does not support item assignment
#
#
# exercise 5
# a = [1, 2, 3]
# b = [4, 5]
#
# print(a+b*3)
#
# correct response: d (a. [1, 2, 3, 4, 5] ; b. [1, 2, 3]; c. error; d. [1, 2, 3, 4, 5, 4, 5, 4, 5])
#
# exercise 6
# x = [1, 2, 3, 4]
# print(x[-1:])
#
# correct response: b [4] (a. [1, 2, 3]; b. [4]; c. [1, 2, 3, 4]; d. [3, 2, 1])
#
# exercise 7
#
# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)

# correct response: c (a.[0,1,3]; b.[1, 3, 2]; c. [0, 1, 2], d. error)
#
# exercise 8
# def exercitiu(i):
#     for i in range:
#         return i
#
# x = exercitiu(3)
# print(x)
#
# correct response: a. error (a. error b. 0 1 2 c.3 d. 0)
#
# exercise 9
# a = range(10)
# y = [x*x for x in a if x%2 == 0]
# print(y)
#
# correct response: c. [0, 4, 16, 36, 64] (a. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; b. [2, 4, 6, 8]; c. [0, 4, 16, 36, 64];
# d. [0, 2, 16, 36, 64])
#
# exercise 10
# def make_account():
#     return {'balance': 0}
#
# def deposit(account, amount):
#     account['balance'] += amount
#     return account['balance']
#
# a = make_account()
# print(deposit(a, 10))
#
# correct response: a. error; b. 0; c. 10; d. None
#
# exercise 11
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
# a = BankAccount()
# b = BankAccount()
# print(a.deposit(100))
#
# correct response: d.100 (a. 0; b. None; c. error, d. 100)
#
# exercise 12
# "foo" + 2
# correct response: a. cannot concatenate "str" and "int" objects
# a. cannot concatenate "str" and "int" objects
# b. name "foo" is not defined
# c. foo2
# d. integer division or modulo by zero
#
# exercise 13
# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")
#
# correct response: c. a c d (a. a b c d; b. a b c; c. a c d; d. error)
#
# exercise 14
# for k in {"x": 1, "y": 2}:
#     print(k)
# correct response: b. x y (a.{"x": 1, "y": 2}; b. x y; c. 1 2; d. error)
#
# exercise 15
# print(list("python"))
#
# correct response: d. ['p', 'y', 't', 'h', 'o', 'n']
# a. ['python']
# b. 'p', 'y', 't', 'h', 'o', 'n'
# c. error
# d. ['p', 'y', 't', 'h', 'o', 'n']
#
# exercise 16
# def func(*args):
#     return 3 + len(args)
#
# print(func(4, 4, 4))
#
# correct response: c. 6  (a. 4; b. error; c. 6; d. 15;)
#
# exercise 17
# count = (3, 2, 5, 4)
# while len(count) < 5:
#     count0 = count[0]+1
#     print("Hello Geek")
#
# correct response: b. loop infinit in care se afiseaza Hello Geek
# a. Hello Geek
# b. loop infinit in care se afiseaza Hello Geek
# c. None
# d. error

# exercise 18
#
# def exercitiu(var):
#     for letter in 'geeksforgeeks':
#         if letter == 'e' or letter == 's':
#             continue
#         print('Current Letter :', letter)
#         var = 10
#         return var
#
# print(exercitiu(20))
#
# correct response: c. Current Letter:g10
# a. 10; b. None; c. Current Letter:g10; d. Current Letter:g20;
#
# exercise 19
# Care este diferenta intre liste si tupluri:
#
# correct response: a. Listele sunt mutabile, tuplurile sunt imutabile
# a. Listele sunt mutabile, tuplurile sunt imutabile
# b. Listele sunt imutabile, tuplurile sunt mutabile
# c. Listele nu sunt indexabile, tuplurile sunt indexabile
# d. niciuna din variantele de mai sus
#
# exercise 20
# def f(a,list=[]):
#     for i in range(a):
#         list.append(i*i)
#         print(list)
# f(3)
# f(2,[1,2,3])
# f(2)
#
# correct response: a.[0,1,4][1,2,3,0,1][0,1,4,0,1]
# a.[0,1,4][1,2,3,0,1][0,1,4,0,1]
# b.[0,1,4][1,2,3,0,1][0,1]
# c.error
# d.[0,1,4]
