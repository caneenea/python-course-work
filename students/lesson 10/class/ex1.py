"""
Build a class tha manages an account of a client in a bank
The class will have :
name, lastname, balance, transcation history
---------------------------------------------------------UNFINISHED-----------------------------------------------------------------------
"""
from datetime import datetime


class Transaction:
    def __init__(self, amount):
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f'{self.date} {self.amount}'

class Account:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.__balance : float = 0
        self.__history : [Transaction] = []

    def __str__(self):
        return f'{self.name} {self.lastname}'

    def balance(self):
        return self.__balance

    def history(self):
        for date in self.__history:
            print(Transaction)


    def deposit(self, amount):
        if amount < 0:
           print('Amount should be grater then 0!')
        else:
         self.__balance += amount
         self.__history.append(Transaction(amount))

    def withdraw(self, amount):
        if amount < 0:
           print('Amount should be grater then 0!')
        elif amount > self.__balance:
            print('Amount should be less then balance!')
        else:
            self.__balance -= amount
            self.__history.append(Transaction(-amount))

client1 = Account('Enea', 'Cane')
print(client1.balance())
client1.deposit(100_000)
print(client1.balance())
client1.withdraw(10_000)
print(client1.balance())
client1.history()









