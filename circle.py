# create helper functions for simple circular geometry calculations

from math import pi

class Circle:
    def __init__ (self, radius):
        self.radius = radius

    def circle_calculation(self, operation:str) -> float:
        """""
        Calculates perimeter/area of circle with given radius.
        
        Parameters:
            radius (float): radius of given circle

        Returns:
            float: The perimeter/area of the circle.
        """""
        
        if operation == 'perimeter':
            result = float(2 * pi * self.radius) 
            
        elif operation == 'area':
            result = float(pi * self.radius ** 2)
       
        else:
            raise ValueError("Invalid operation. Please specify 'perimeter' or 'area'.")
               
        return result
