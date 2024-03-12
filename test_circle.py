
#Testing both methods in circle.py
import pytest
from math import pi
from circle import Circle

# Tests for perimeter calculation with positive float input
def test_perimeter():

    #creating instance for radius = 2
    circle_instance = Circle(radius = 2)
    expected_perim_result = f'This circle has a perimeter of {round(2 * pi * 2, 2)} cm.'
    actual_perim_result = circle_instance.perform_cir_calc('perimeter')
    assert actual_perim_result == expected_perim_result, "Perimeter calculation test failed!"


# Tests for area calculation
def test_area():

    #creating instance for radius = 2
    circle_instance = Circle(radius = 2)
    expected_area_result = f'This circle has an area of {round(pi * 2 ** 2, 2)} cm.'
    actual_area_result = circle_instance.perform_cir_calc('area')
    assert actual_area_result == expected_area_result, "Area calculation test failed!"