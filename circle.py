# The Circle class for calculations

import numpy as np

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = np.pi * (radius ** 2)
        self.perimeter = np.pi * 2 * radius
    
    def area(self):
        return(self.area)
    
    def perimeter(self):
        return(self.perimeter)