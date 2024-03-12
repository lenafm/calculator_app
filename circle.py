from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return pi * 2 * self.radius
    def area(self):
        return pi * self.radius**2