#I did sort of use Ai here just to figure out how to set this up, but I ended up fixing errors from the Ai.
from circle import Circle

def test_circle_area():
    # Create a Circle instance with a radius of 5
    circle = Circle(radius=5)
    expected_area = 3.14159 * 5 ** 2
    assert round(circle.circle_area(),3) == round(expected_area, 3)

def test_circumference():
    # Create a Circle instance with a radius of 3
    circle = Circle(radius=3)
    expected_circumference = 2 * 3.14159 * 3
    assert round(circle.circumference(),3) == round(expected_circumference,3)

if __name__ == '__main__':
    # Run the test cases
    test_circle_area()
    test_circumference()
    print("All tests passed!")
