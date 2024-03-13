## create helper functions for circle calculations

# import circle class from circle.py
from circle import Circle
from math import pi

# test area function
def test_area():
    circle = calc_circles(radius = 1)
    expected_res = f"This circle's area is: {round(pi * 1 ** 2, 4)}"
    actual_res = circle.area("area")
    assert actual_res == expected_res


# test area function
def test_perimeter():
    circle = calc_circles(radius = 1)
    expected_res = f"This circle's perimeter is: {round(result, 4)}"
    actual_res = circle.perimeter("perimeter")
    assert actual_res == expected_res
