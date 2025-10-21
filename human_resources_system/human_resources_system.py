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
        print(f"Name: {self.name} /// Salary: {self.salary} /// Department: {self.department} /// Count_of_Proje: {self.count_projects}")

class Worker(Personal):
    def __init__(self, name, salary, department, programming_language):
        super().__init__(name, salary, department)
        self.programming_language = programming_language
    def show_information(self):
        print(f"Name: {self.name} /// Salary: {self.salary} /// Department: {self.department} /// Programming Language: {self.programming_language}")

yonetici1 = Administrators("Ali", 80000, "Yönetim", 5) 
gelistirici1 = Worker("Kerem", 60000, "Teknoloji", "Python")

yonetici1.show_information()
gelistirici1.show_information()