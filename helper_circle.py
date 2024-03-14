# create helper_circle functions for circle calculations
import math
class circle_perform:
    def __init__(self, radius: float):
        self.radius=radius
    def perimeter(self) -> float:
        return  2*math.pi*self.radius
    def area(self) -> float:
        return math.pi*(self.radius**2)