import numpy as np
from circle import Circle 

def test_perimeter():
    circle = Circle(1)
    expected_result = 2 * np.pi * 1
    assert circle.perimeter() == expected_result

def test_area():
    circle = Circle(1)
    expected_result = np.pi * 1 ** 2
    assert circle.area() == expected_result