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


b1 = Book("Suç ve Ceza", "Dostoyevski")

b1.show_information()

b1.borrow()

b1.show_information()

b1.get_refund()

b1.show_information()