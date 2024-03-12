import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return round((math.pi * self.radius**2), 2)

    def circle_perimeter(self):
        return round((math.pi * self.radius * 2), 2)

circle_instance = Circle(1)
check = circle_instance.circle_area()
check2 = circle_instance.circle_perimeter()

print(check)
print(check2)