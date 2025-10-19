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
    def __init__(self):
        self.all_books = []
        self.all_members = []
    def book_register(self, book_object):
        self.all_books.append(book_object)
    def Member_register(self, member_object):
        self.all_members.append(member_object)
    def book_research(self, isbn):
        for book in self.all_books:
            if book.ISBN ==  isbn:
                return book
        return None
    def member_research(self, id):
        for member in self.all_members:
            if member.ID ==  id:
                return member
        return None

    def book_borrow(self, isbn, id):
        book = self.book_research(isbn)
        member = self.member_research(id)
        if (member is None) or (book is None):
            print("Member or Book has not found")
        else:
            if book.duration == "available":
                book.borrow()
                member.borrowed_list.append(book.name)
                print(f"Success. {book.name} has been borrowed by {member.name}")
            else:
                print(f"{book.name} has already been borrowed")
    
    def book_get_refund(self, isbn, id):
        book = self.book_research(isbn)
        member = self.member_research(id)
        if (member is None) or (book is None):
            print("Member or Book has not found")
        else:
            if book.duration != "available":
                book.get_refund()
                member.borrowed_list.remove(book.name)
                print(f"Success. {book.name} has been refund by {member.name}")
            else:
                print(f"{book.name} has already been refund")