import random

class book:
    def __init__(self, name, writer):
        self.name = name
        self.duration = "available"
        self.writer = writer
        self.ISBN = self.ISBN_Calculator()
    def ISBN_Calculator(self):
        return str(random.randint(1000000000000,9999999999999))
    def show_information(self):
        pass

    