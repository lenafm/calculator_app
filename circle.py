import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return math.pi * float(self.radius) ** 2

    def circumference(self):
        return 2 * math.pi * float(self.radius)

    def circle_calculate(self, operation):
        if operation.lower() == "area":
            return self.circle_area()
        elif operation.lower() == "circumference":
            return self.circumference()
        else:
            return "Invalid operation. Please choose 'area' or 'circumference'."

