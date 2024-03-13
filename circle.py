from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def area(self):
        return 3.14 * self.radius * self.radius 

def circle_calc(radius, operation):
    c = Circle(float(radius))
    if operation == 'perimeter':
        return c.perimeter()
    elif operation == 'area':
        return c.area()
    else:
        return "Invalid operation"