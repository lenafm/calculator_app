from circle import Circle

def test_calc_perimeter():
    circle = Circle(5)
    assert circle.calc_perimeter() == 2 * 3.1416 * 5

    circle = Circle(2)
    assert circle.calc_perimeter() == 2 * 3.1416 * 2
def test_calc_area():
    circle = Circle(2)
    assert circle.calc_area() == 3.1416* 2 ** 2

    circle = Circle(4)
    assert circle.calc_area() == 3.1416* 4 ** 2