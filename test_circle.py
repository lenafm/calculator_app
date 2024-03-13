from circle import Circle

def test_area():
    # Test the area method of the Circle class with radius 3
    radius = 3
    circle = Circle(radius)
    expected_area = 28.274333882308138  # Expected area for a circle with radius 3
    assert circle.area() == expected_area

def test_perimeter():
    # Test the perimeter method of the Circle class with radius 3
    radius = 3
    circle = Circle(radius)
    expected_perimeter = 18.84955592153876  # Expected perimeter for a circle with radius 3
    assert circle.perimeter() == expected_perimeter
