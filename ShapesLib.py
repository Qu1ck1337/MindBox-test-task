import math


#Абстрактный класс Shape, от которого будут унаследоваться Circle, Triangle
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
        self.area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))