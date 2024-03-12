import numpy

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return numpy.pi * self.radius ** 2

    def perimeter(self):
        return  2 * self.radius * numpy.pi


