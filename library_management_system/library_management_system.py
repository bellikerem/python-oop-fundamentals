import random
import string


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
    def show_all_members(self):
        print("\n--- ALL MEMBERS ---")
        for i in self.all_members:
            Member.show_information(i)
    def show_all_books(self):
        print("\n--- ALL BOOKS ---")
        for i in self.all_books:
            Book.show_information(i)


def check_string(prompt):
    while True:
        string_input = input(prompt)
        if not string_input.strip():
            print("Please do not leave blank.")
            continue
        
        if string_input.isdigit(): 
            print("The name cannot consist of numbers only. Please enter a name.")
            continue

        return string_input.strip()


my_library = Library()

book1 = Book("The Call of Wild", "Jack London")
book2 = Book("The Miser", "Moliere")
member1 = Member("Steve")
member2 = Member("Richards")

my_library.book_register(book1)
my_library.book_register(book2)
my_library.Member_register(member1)
my_library.Member_register(member2)


print("\n--- WELCOME TO OOP ACADEMY LİBRARY ---")
while True:
    try:
        print("\n--- MAIN MENU ---")
        mainmenu_input = input("Press 1 to register as a member\n" \
        "Press 2 to register as a book\n" \
        "Press 3 to borrow a book\n" \
        "Press 4 to refund a book\n" \
        "Press 5 to quit: ")
        mainmenu = int(mainmenu_input)
        if mainmenu not in [1,2,3,4,5]:
            print("\n--- RESULT ---")
            print("Please press input a number that you see")
            continue
        else:
            if mainmenu == 1:
                name_input = check_string("Please input member's name: ")
                member = Member(name_input)
                my_library.Member_register(member)
                print("\n--- RESULT ---")
                print("Registration completed")
                member.show_information()
            elif mainmenu == 2:
                name_input = check_string("Please input book's name: ")
                writer_input = check_string("Please input book's writer: ")
                book = Book(name_input, writer_input)
                my_library.book_register(book)
                print("\n--- RESULT ---")
                print("Registration completed")
                book.show_information()
            elif mainmenu == 3:
                my_library.show_all_members()
                id_input = str(input("Please input member's id: "))
                my_library.show_all_books()
                isbn_input = str(input("Please input book's isbn number: "))
                print("\n--- RESULT ---")
                my_library.book_borrow(isbn_input, id_input)
            elif mainmenu == 4:
                my_library.show_all_members()
                id_input = str(input("Please input member's id: "))
                my_library.show_all_books()
                isbn_input = str(input("Please input book's isbn number: "))
                print("\n--- RESULT ---")
                my_library.book_get_refund(isbn_input, id_input)
            else:
                break
    except ValueError:
        print("Please input a integer")
SystemExit