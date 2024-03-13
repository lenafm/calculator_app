from circle import Circle, circle_calc
import pytest
import numpy as np
from math import pi

# Testing area calculation
radius = 3
def area_test():
    circle = Circle(radius)
    expected = np.pi * radius ** 2
    assert Circle(radius).area() == expected
    
def perimeter_test():
    circle = Circle(radius)
    expected = 2 * np.pi * radius
    assert Circle(radius).perimeter() == expected