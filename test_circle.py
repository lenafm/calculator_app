
from circle import Circle
from math import isclose

def test_circle_calculation_area():
    circle = Circle(5)
    assert circle.circle_calculation("area") == 78.53981633974483
    circle = Circle(5.0)
    assert circle.circle_calculation("area") == 78.53981633974483
    circle = Circle(0)
    assert circle.circle_calculation("area") == 0
    circle = Circle(-1)
    assert circle.circle_calculation("area") == "Invalid input for radius" 
    circle = Circle(0.0001)
    assert circle.circle_calculation("area") == 3.141592653589793e-08
    circle = Circle("HelloWorld")
    assert circle.circle_calculation("area") == "Cannot perform operation with this input"
    
def test_circle_calculation_perimeter():
    circle = Circle(5)
    assert circle.circle_calculation("perimeter") == 31.41592653589793
    circle = Circle(5.0)
    assert circle.circle_calculation("perimeter") == 31.41592653589793
    circle = Circle(0)
    assert circle.circle_calculation("perimeter") == 0
    circle = Circle(-1)
    assert circle.circle_calculation("perimeter") == "Invalid input for radius"
    circle = Circle(0.0001)
    actual_perimeter = circle.circle_calculation("perimeter")
    expected_perimeter = 0.00062831853071796
    assert isclose(actual_perimeter, expected_perimeter, rel_tol=1e-9), f"Expected {expected_perimeter}, but got {actual_perimeter}"
    circle = Circle("HelloWorld")
    assert circle.circle_calculation("area") == "Cannot perform operation with this input"    

def run_tests():
    test_circle_calculation_area()
    test_circle_calculation_perimeter()
    print("All tests passed!") # if any assertions fail, AssertionError will be raised
    
if __name__ == "__main__":
    run_tests()