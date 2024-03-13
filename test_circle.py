from circle import Circle


def test_area():
    radius = 5
    manual_area = round(3.14159265359 * (radius ** 2), 2)
    circle = Circle(radius)
    assert round(circle.area(), 2) == manual_area, "Area test failed"


def test_perimeter():
    radius = 5
    manual_perimeter = round(2 * 3.14159265359 * radius, 2)
    circle = Circle(radius)
    assert round(circle.perimeter(), 2) == manual_perimeter, "Perimeter test failed"


if __name__ == "__main__":
    test_area()
    test_perimeter()
    print("All tests successfully passed.")
