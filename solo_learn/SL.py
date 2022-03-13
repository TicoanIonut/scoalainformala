class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def __repr__(self):
        return "Account Balance: {}".format(self._balance)

    def deposit(self, amount):
        self._balance += amount


acc = BankAccount(0)
acc.deposit(int(input()))
print(acc)


class Number:
    def __init__(self, num):
        self.value = num

    @property
    def iseven(self):
        if self.value % 2 == 0:
            return True
        return False


x = Number(int(input()))
print(x.iseven)


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, other):
        return Juice(self.name + '&' + other.name, self.capacity + other.capacity)

    def __str__(self):
        return self.name + ' ('+str(self.capacity)+'L)'


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)
