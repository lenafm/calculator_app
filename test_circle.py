from circle import Circle
import math

radius = Circle(5)


def test_circle():
    assert radius.perimeter() == 2 * math.pi * 5, 'The perimeter method is wrong'
    assert radius.area() == math.pi * (5 ** 2), 'The area method is wrong'
