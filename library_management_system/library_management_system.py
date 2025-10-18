import random

class Book:
    def __init__(self, name, writer):
        self.name = name
        self.duration = "available"
        self.writer = writer
        self.ISBN = self.ISBN_Calculator()
    def ISBN_Calculator(self):
        return str(random.randint(1000000000000,9999999999999))
    def show_information(self):
        print(f"Book Name: {self.name} /// Writer Name: {self.writer} /// Duration: {self.duration} /// ISBN: {self.ISBN}")
    def borrow(self):
        if self.duration == "available":
            self.duration = "borrowed"
        else:
            print("This book has already been borrowed.")
    def get_refund(self):
        self.duration = "available"

class Member:
    def __init__(self, name):
        self.name = name
        self.ID = self.ID_Calculator()
        self.borrowed_list = []
    def ID_Calculator(self):
        return str(random.randint(100000000,999999999))
    def show_information(self):
        print(f"Member Name: {self.name} /// ID: {self.ID} /// Borrowed List: {self.borrowed_list}")

class Library:
    pass