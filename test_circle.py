
from circle import Circle
import math

def test_circle():
    # Test case for perimeter
    radius = 5
    circle = Circle(radius)

    expected_perimeter = 2 * math.pi * radius
    assert circle.perimeter() == expected_perimeter, f"Expected perimeter: {expected_perimeter}, but got: {circle.perimeter()}"

    # Test case for area
    expected_area = math.pi * (radius ** 2)
    assert circle.area() == expected_area, f"Expected area: {expected_area}, but got: {circle.area()}"


    print("All tests passed!")


if __name__ == "__main__":
    test_circle()