#create circle class
import numpy as np
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return  np.pi * self.radius ** 2
    def perimeter(self):
        return 2 * np.pi * self.radius