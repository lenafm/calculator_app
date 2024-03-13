from circle import Circle
from math import pi

# Test case for the area method
def test_circle_area():
    radius = 3
    test_circle = Circle(radius)
    expected_area = pi * radius ** 2
    assert test_circle.area() == expected_area

# Test case for the perimeter method
def test_circle_perimeter():
    radius = 3
    test_circle = Circle(radius)
    expected_perimeter = 2 * pi * radius
    assert test_circle.perimeter() == expected_perimeter

if __name__ == "__main__":
    test_circle_area()
    test_circle_perimeter()
    print("All tests passed!")