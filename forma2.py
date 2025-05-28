import math

class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x: int):
        self._x = x

    def set_y(self, y: int):
        self._y = y

    def compute_distance(self, other):
        return math.sqrt((self._x - other.get_x()) ** 2 + (self._y - other.get_y()) ** 2)

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def get_start_point(self):
        return self._start_point

    def get_end_point(self):
        return self._end_point

    def get_length(self):
        return self._length

    def set_start_point(self, point: Point):
        self._start_point = point
        self._length = self.compute_length()

    def set_end_point(self, point: Point):
        self._end_point = point
        self._length = self.compute_length()

    def compute_length(self):
        return self._start_point.compute_distance(self._end_point) 

class Shape:
    def __init__(self, vertices: list[Point]):
        self._vertices = vertices
        self._edges = self.compute_edges()
        self._inner_angles = []
        self._is_regular = False
    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def get_inner_angles(self):
        return self._inner_angles

    def get_is_regular(self):
        return self._is_regular

    def set_vertices(self, vertices: list[Point]):
        self._vertices = vertices
        self._edges = self.compute_edges()

    def set_is_regular(self, value: bool):
        self._is_regular = value 

    def compute_edges(self):
        edges = []
        for i in range(len(self._vertices)):
            start = self._vertices[i]
            end = self._vertices[(i + 1) % len(self._vertices)]
            edges.append(Line(start, end))
        return edges
    
    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_inner_angles(self):
        pass  

    def compute_area(self):
        raise NotImplementedError("Este método debe ser aplicado por las subclases.") 

class Triangle(Shape):
    def __init__(self, vertices: list[Point]):
        if len(vertices) != 3:
            raise ValueError("Un triangulo tiene 3 vertices.")
        super().__init__(vertices)

    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self._edges]
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area
class Equilateral(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(True)

class Isosceles(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(False)

class Scalene(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(False)

class RightTriangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(False)

class Rectangle(Shape):
    def __init__(self, vertices: list[Point]):
        if len(vertices) != 4:
            raise ValueError("Un rectangulo debe tener 4 vertices.")
        super().__init__(vertices)
        self.set_is_regular(False)

    def compute_area(self):
        base = self._edges[0].get_length()
        height = self._edges[1].get_length()
        return base * height
    
class Square(Rectangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(True)
