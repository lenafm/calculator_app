# create area and parameter functions for calculations

import math

class Circle: #define a circle class
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)): #this will check if the radius input is a string or not
            raise ValueError("Invalid input. Radius must be a numeric value greater than 0.")
        if radius <= 0:
            raise ValueError("Invalid input. Radius must be a numeric value greater than 0.")
        self.radius = radius

    def get_perimeter(self) -> float: #function for perimeter of a circle
        return round(2 * math.pi * self.radius,4)

    def get_area(self) -> float: #function for area of a circle
        return round(math.pi * self.radius ** 2, 4)
