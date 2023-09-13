import math


# Abstract class Shape, from which Circle, Triangle will inherit
class Shape:
    def __init__(self):
        self.area = 0

    def get_area(self) -> float:
        return self.area


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.area = math.pi * radius ** 2


class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        super().__init__()
        p = (side1 + side2 + side3) / 2
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))

    def is_right_triangle(self) -> bool:
        if (self.side1 ** 2 + self.side2 ** 2 == self.side3 ** 2) or \
            (self.side2 ** 2 + self.side3 ** 2 == self.side1 ** 2) or \
            (self.side1 ** 2 + self.side3 ** 2 == self.side2 ** 2):
            return True
        return False
