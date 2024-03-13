from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pow(self.radius,2) * pi

    def perimeter(self):
        return 2 * pi * self.radius
