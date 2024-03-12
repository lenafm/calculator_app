# test_circle.py

import math
import pytest
from circle import Circle

def test_calculate_perimeter():
    # Test the calculate_perimeter method
    circle = Circle(radius=5)
    expected_perimeter = 2 * math.pi * 5
    assert circle.calculate_perimeter() == round(expected_perimeter, 2)

def test_calculate_area():
    # Test the calculate_area method
    circle = Circle(radius=5)
    expected_area = math.pi * 5**2
    assert circle.calculate_area() == round(expected_area, 2)