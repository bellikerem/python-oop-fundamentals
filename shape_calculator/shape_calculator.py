import math

class Shape:
    def __init__ (self, name):
        self.name = name
    def area_calculator(self):
        raise NotImplementedError("This method should be implemented in child classes according to their own formula.")
    def perimeter_calculator(self):
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