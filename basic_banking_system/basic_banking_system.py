import random
import string

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.id = self.id_calculator()
        self.__balance = balance
    def id_calculator(self):
        return str(random.randint(100000000,999999999))
    def withdraw_money(self, amount):
        if amount > self.__balance:
            print("\n--- RESULT ---")
            print("Your balance is not enough for this action")
        else:
            self.__balance = self.__balance - amount
            print("\n--- RESULT ---")
            print(f"Successfull. Your new balance is {self.__balance}")
    def deposit_money(self, amount):
        self.__balance = self.__balance + amount
        print("\n--- RESULT ---")
        print(f"Successfull. Your new balance is {self.__balance}")
    def show_information(self):
        print("\n--- RESULT ---")
        print(f"Account name is: {self.name} /// ID: {self.id} /// balance: {self.__balance}")

def check_string(prompt):
    while True:
        string_input = input(prompt)
        if not string_input.strip():
            print("\n--- RESULT ---")
            print("Please do not leave blank.")
            continue
        
        if string_input.isdigit():
            print("\n--- RESULT ---")
            print("The name cannot consist of numbers only. Please enter a name.")
            continue

        return string_input.strip()

def check_integer(number):
    while True:
        try:
            integer_input = int(input(number))
            if integer_input > 0:
                return integer_input
            elif integer_input < 0:
                print("\n--- RESULT ---")
                print("Please input a positive number")
                continue
            else:
                print("\n--- RESULT ---")
                print("Please do not input 0")
                continue
        except ValueError:
            print("\n--- RESULT ---")
            print("Please input an integer")


while True:
    print("\n--- WELCOME TO THE OOP BANK ---")
    print("Please create an account...")
    name = check_string("Please input an account name: ")
    balance = check_integer("Please input a balance (if you dont input a value. it will be automaticly 0): ")
    a1 = Account(name, balance)
    print("Account has been created.")
    a1.show_information()
    break

while True:
    try:
        print("\n--- MAIN MENU ---")
        mainmenu_input = input("Press 1 to withdraw money\n" \
        "Press 2 to deposit money\n" \
        "Press 3 to show information\n" \
        "Press 4 to quit: ")
        mainmenu = int(mainmenu_input)
        if mainmenu not in [1,2,3,4]:
            print("\n--- RESULT ---")
            print("Please input a number that you see on the screen")
        elif mainmenu == 1:
            amount = check_integer("Please input an amount: ")
            a1.withdraw_money(amount)
        elif mainmenu == 2:
            amount = check_integer("Please input an amount: ")
            a1.deposit_money(amount)
        elif mainmenu == 3:
            a1.show_information()
        else:
            break
    except ValueError:
        print("\n--- RESULT ---")
        print("Please input an integer")
SystemExit