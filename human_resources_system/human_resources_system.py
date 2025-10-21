import string

class Personal:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    def show_information(self):
        raise NotImplementedError("This method should be implemented in child classes according to their own formula.")
    
class Administrators(Personal):
    def __init__(self, name, salary, department, count_projects):
        super().__init__(name, salary, department)
        self.count_projects = count_projects
    def show_information(self):
        print("\n--- RESULT ---")
        print(f"Name: {self.name} /// Salary: {self.salary} /// Department: {self.department} /// The Count of Proje: {self.count_projects}")

class Worker(Personal):
    def __init__(self, name, salary, department, programming_language):
        super().__init__(name, salary, department)
        self.programming_language = programming_language
    def show_information(self):
        print("\n--- RESULT ---")
        print(f"Name: {self.name} /// Salary: {self.salary} /// Department: {self.department} /// Programming Language: {self.programming_language}")

def check_string(prompt):
    while True:
        string_input = input(prompt)
        if not string_input.strip():
            print("\n--- RESULT ---")
            print("Please do not leave blank.")
            continue

        if string_input.isdigit():
            print("\n--- RESULT ---")
            print("The value cannot consist numbers only.")
            continue

        return string_input
    
def check_integer(prompt):
    while True:
        try:
            integer_input = int(input(prompt))
            if integer_input <= 0:
                print("\n--- RESULT ---")
                print("Please input a positive number.")
                continue
            else:
                return integer_input
        except ValueError:
            print("\n--- RESULT ---")
            print("Please input an integer.")

print("\n--- OOP HUMAN RESOURCES SYSTEM ---")
while True:
    try:
        print("\n--- MAIN MENU ---")
        mainmenu_input = input("Press 1 to register Administrator\n" \
        "Press 2 to register a worker\n" \
        "Press 3 to quit: ")
        mainmenu = int(mainmenu_input)
        if mainmenu not in [1,2,3]:
            print("\n--- RESULT ---")
            print("Please input a number that you see on the screen.")
            continue
        elif mainmenu == 1:
            name = check_string("Please input the name: ")
            salary = check_integer("Please input the salary: ")
            department = check_string("Please input the department: ")
            count_projects = check_integer("Please input the count of projects: ")
            print("Registeration is successfully.")
            A1 = Administrators(name, salary, department, count_projects)
            A1.show_information()
        elif mainmenu == 2:
            name = check_string("Please input the name: ")
            salary = check_integer("Please input the salary: ")
            department = check_string("Please input the department: ")
            programming_language = check_string("Please input a programming language that you know: ")
            print("Registeration is successfully.")
            W1 = Worker(name, salary, department, programming_language)
            W1.show_information()
        else:
            break
    except ValueError:
        print("\n--- RESULT ---")
        print("Please input an integer.")

SystemExit