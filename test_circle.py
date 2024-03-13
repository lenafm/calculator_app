from circle import Circle
import math
def test_perimeter_calculation():
    # Create an instance of the Circle class with radius 1
    circle = Circle(1)

    # Call the perimeter_calculation method
    perimeter = circle.perimeter_calculation()

    # Assert the result rounded to 8 decimal places
    assert round(perimeter, 8) == round(2 * math.pi, 8)
def test_area_calculation():
    # Create an instance of the Circle class with radius 1
    circle = Circle(1)

    # Call the area_calculation method
    area = circle.area_calculation()

    # Assert the result rounded to 8 decimal places
    assert round(area, 8) == round(math.pi, 8)