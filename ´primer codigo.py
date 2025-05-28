class Shape():
    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width= width
        self.height= height
    def compute_area(self):
        return self.width * self.height
    def compute_perimeter(self):
        return 2 *(self.width + self.height)
class  Square(Shape):
    def __init__(self, side):
        self.side= side
    def compute_area(self):
        return self.side ** 2
    def compute_perimeter(self):
        return 4 * self.side
rect= Rectangle(4, 5)
print(f"Área del rectángulo: {rect.compute_area()}")
print(f"Perímetro del rectángulo: {rect.compute_perimeter()}")
Squ= Square(4)
print(f"Área del cuadrado: {rect.compute_area()}")
print(f"perímetro del cuadrado: {rect.compute_perimeter()}")
