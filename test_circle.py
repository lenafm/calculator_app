import pytest
import numpy as np

from circle import Circle#

def test_area_works():
    testCircle = Circle(radius = 1)
    assert testCircle.area() == np.pi

def test_perimeter_works():
    testCircle = Circle(radius = 4)
    assert testCircle.perimeter() == 8 * np.pi