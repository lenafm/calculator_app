import pytest
from circle import circle_ops

def test_circle_perimeter():
    perimeter = circle_ops(radius=5, operation='perimeter')
    assert perimeter == 2 * 3.14 * 5

def test_circle_area():
    area = circle_ops(radius=5, operation='area')
    assert area == 3.14 * (5 ** 2)
