import random

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.id = self.id_calculator()
        self.__balance = balance
    def id_calculator(self):
        return str(random.randint(100000000,999999999))
    def withdraw_money(self, amount):
        if amount > self.__balance:
            print("Your balance is not enough for this action")
        else:
            self.__balance = self.__balance - amount
            print(f"Successfull. Your new balance is {self.__balance}")
    def deposit_money(self, amount):
        self.__balance = self.__balance + amount
        print(f"Successfull. Your new balance is {self.__balance}")
    def show_information(self):
        print(f"Account name is: {self.name} /// ID: {self.id} /// balance: {self.__balance}")


a1 = Account("Kerem Can Belli", 10000)

a1.show_information()

a1.withdraw_money(100000)

a1.show_information()

a1.withdraw_money(1)

a1.show_information()

a1.deposit_money(10)

a1.show_information()