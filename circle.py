# create helper functions for simple circular geometry calculations

from math import pi

class Circle:
    def __init__ (self, radius):
        self.radius = radius

    def circle_calculation(radius:float) -> float:
        """""
        Calculates perimeter/area of circle with given radius.
        
        Parameters:
            radius (float): radius of given circle

        Returns:
            float: The perimeter/area of the circle.
        """""
        
        if operation == 'perimeter':
            result = float(2 * pi *radius) 
            
        elif operation == 'area':
            result == float(pi * radius ** 2)
       
        return result
