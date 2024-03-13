# Data Structures & Algorithms Spring 2024
# Problem Set 2
# Lonny Chen, 216697
# circle.py

import math

class Circle:
    rounding_int_default = 2

    def __init__(self, radius):
        '''Constructs Circle with instance attributes.'''
        self.radius = radius

    def area(self, rounding_int=rounding_int_default):
        '''Returns area of this Circle with input rounding.'''
        result = math.pi * (self.radius ** 2)
        if rounding_int == 0:
            rounded_result = round(result)
        else:
            rounded_result = round(result, rounding_int)
        return rounded_result

    def perimeter(self, rounding_int=rounding_int_default):
        '''Returns perimeter of this Circle with input rounding.'''
        result = 2 * math.pi * self.radius
        if rounding_int == 0:
            rounded_result = round(result)
        else:
            rounded_result = round(result, rounding_int)
        return rounded_result
