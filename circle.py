import math


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = radius

    def perimeter(self):
        # Calculate the perimeter of a circle
        return 2 * math.pi * self.radius

    def area(self):
        # Calculate the area of a circle
        return math.pi * (self.radius ** 2)
