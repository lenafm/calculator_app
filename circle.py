# The Circle class for calculations

import numpy as np

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area_internal = np.pi * (radius ** 2)
        self.perimeter_internal = np.pi * 2 * radius
        #We already calculate the values for area and perimeter and area as attributes
    
    def area(self):
        return(self.area_internal)
    #Returns the area
    
    def perimeter(self):
        return(self.perimeter_internal)
    #Returns the perimeter