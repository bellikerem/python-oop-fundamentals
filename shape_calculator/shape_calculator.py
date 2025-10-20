import math

class Shape:
    def __init__ (self, name):
        self.name = name
    def area_calculator(self):
        print("\n--- RESULT ---")
        raise NotImplementedError("This method should be implemented in child classes according to their own formula.")
    def perimeter_calculator(self):
        print("\n--- RESULT ---")
        raise NotImplementedError("This method should be implemented in child classes according to their own formula.")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area_calculator(self):
        return math.pi * (self.radius ** 2)
    def perimeter_calculator(self):
        return 2 * math.pi * self.radius
    
class Square(Shape):
    def __init__(self, edge):
        super().__init__("Square")
        self.edge = edge

    def area_calculator(self):
        return self.edge ** 2
    def perimeter_calculator(self):
        return self.edge * 4

class Rectangle(Shape):
    def __init__(self, long_edge, short_edge):
        super().__init__("Rectangle")
        self.long_edge = long_edge
        self.short_edge = short_edge

    def area_calculator(self):
        return self.long_edge * self.short_edge
    def perimeter_calculator(self):
        return (self.long_edge * 2) + (self.short_edge * 2)

class Triangle(Shape):
    def __init__(self, height, base_edge):
        super().__init__("Triangle")
        self.height = height
        self.base_edge = base_edge
    def area_calculator(self):
        return (self.height * self.base_edge) / 2
    def perimeter_calculator(self):
        print("\n--- RESULT ---")
        raise NotImplementedError("The perimeter cannot be calculated because the edges are unknown.")
    

def check_integer(number):
    while True:
        try:
            integer_input = int(input(number))
            if integer_input > 0:
                return integer_input
            else:
                print("\n--- RESULT ---")
                print("Please input a positive value.")
                continue
        except ValueError:
            print("\n--- RESULT ---")
            print("Please input an integer")


print("\n--- SHAPE CALCULATOR ---")
while True:
    try:
        print("\n--- DECİSİON ---")
        decision_input = input("Press 1 to calculate area\n" \
        "Press 2 to calculate perimeter: ")
        decision = int(decision_input)
        if decision not in [1,2]:
            print("\n--- RESULT ---")
            print("Please input 1 or 2.")
        elif decision == 1:
            decision1 = "Area"
            break
        else:
            decision1 = "Perimeter"
            break
    except ValueError:
        print("\n--- RESULT ---")
        print("Please input an integer")

while True:
    try:
        print("\n--- MAIN MENU ---")
        mainmenu_input = input("Press 1 if your shape is circle\n" \
        "Press 2 if your shape is Square\n" \
        "Press 3 if your shape is rectangle\n" \
        "Press 4 if your shape is triangle\n" \
        "Press 5 to quit: ")
        mainmenu = int(mainmenu_input)
        if mainmenu not in [1,2,3,4,5]:
            print("\n--- RESULT ---")
            print("Please input a number that you see on the screen")
        elif mainmenu == 1:
            if decision1 == "Area":
                radius = check_integer("Please input a radius value: ")
                circle = Circle(radius)
                print("\n--- RESULT ---")
                print(circle.area_calculator())
            else:
                radius = check_integer("Please input a radius value: ")
                circle = Circle(radius)
                print("\n--- RESULT ---")
                print(circle.perimeter_calculator())
        elif mainmenu == 2:
            if decision1 == "Area":
                edge = check_integer("Please input a edge value: ")
                square = Square(edge)
                print("\n--- RESULT ---")
                print(square.area_calculator())
            else:
                edge = check_integer("Please input a edge value: ")
                square = Square(edge)
                print("\n--- RESULT ---")
                print(square.perimeter_calculator())
        elif mainmenu == 3:
            if decision1 == "Area":
                long_edge = check_integer("Please input a long edge value: ")
                short_edge = check_integer("Please input a short edge value: ")
                rectangle = Rectangle(long_edge, short_edge)
                print("\n--- RESULT ---")
                print(rectangle.area_calculator())
            else:
                long_edge = check_integer("Please input a long edge value: ")
                short_edge = check_integer("Please input a short edge value: ")
                rectangle = Rectangle(long_edge, short_edge)
                print("\n--- RESULT ---")
                print(rectangle.perimeter_calculator())
        elif mainmenu == 4:
            if decision1 == "Area":
                height = check_integer("Please input a height value: ")
                base_edge = check_integer("Please input a base edge value: ")
                triangle = Triangle(height, base_edge)
                print("\n--- RESULT ---")
                print(triangle.area_calculator())
            else:
                height = check_integer("Please input a height value: ")
                base_edge = check_integer("Please input a base edge value: ")
                triangle = Triangle(height, base_edge)
                print("\n--- RESULT ---")
                print(triangle.perimeter_calculator())
        else:
            break
    except ValueError:
        print("Please input an integer")
SystemExit