
from circle import Circle
import math

def test_calculate_perimeter():
    # testing calculate_perimeter
    circle = Circle(radius=5)
    expected_perimeter = 2 * math.pi * 5
    assert circle.calculate_perimeter() == round(expected_perimeter, 2)

def test_calculate_area():
    # testing calculate_area
    circle = Circle(radius=5)
    expected_area = math.pi * 5**2
    assert circle.calculate_area() == round(expected_area, 2)