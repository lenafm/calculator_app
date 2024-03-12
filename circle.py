
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)

    def calculate_area(self):
        area = math.pi * self.radius**2
        return round(area, 2)