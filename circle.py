from math import pi

#Defining Circle class
class Circle: 
    def __init__(self, radius: float):
        self.radius = radius

    #Calculating perimeter of circle     
    def perimeter(self):
        return 2 * pi * self.radius

    #Calculating area of circle
    def area(self): 
        return pi * self.radius ** 2

    #Defining calculation function based on selected operation
    def perform_cir_calc(self, operation: str) -> float: 
        if operation == 'perimeter':
            return f'This circle has a perimeter of {round(self.perimeter(), 2)} cm.'
        elif operation == 'area':
            return f'This circle has an area of {round(self.area(), 2)} cm.'
   
#Converting radius input into float
def convert_radius_to_float(radius: str) -> float:
    return float(radius)
