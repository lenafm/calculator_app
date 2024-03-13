## create functions for circle calculations

# import package
from math import pi

# define class for circle calculations
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        result = pi * self.radius**2
        return f"This circle's area is: {round(result, 4)}"
    
    def perimeter(self):
        result = 2 * pi * self.radius
        return f"This circle's perimeter is: {round(result, 4)}"