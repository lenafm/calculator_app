from circle import Circle
from math import pi
import random

'''
These tests are circular, but we're testing a toy example.
I could have also hardcoded some precalculated perimeters and areas and tested it that way.
I am not testing invalid inputs (e.g. radius = "five") here because I handle that via input validation in Flask.
I would normally test the Flask app itself, but that is out of scope for this problem set.

I run these tests via pytest test_circle.py
'''



def test_circle_perimeter():
    radius = random.random() * 100
    circle = Circle(radius)
    assert circle.perimeter() == pi * 2 * radius


def test_circle_area():
    radius = random.random() * 100
    circle = Circle(radius)
    assert circle.area() == pi * radius**2