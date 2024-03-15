
from circle import Circle
from math import isclose

# area tests
def test_circle_calculation_area_int():
    circle = Circle(5)
    actual_area_5 = circle.circle_calculation('area')
    expected_area_5 = 78.53981633974483
    assert isclose(actual_area_5, expected_area_5, rel_tol=1e-9), f"Expected {expected_area_5}, but got {actual_area_5}"
    
def test_circle_calculation_area_float():
    circle = Circle(4.9)
    actual_area_4_9 = circle.circle_calculation('area')
    expected_area_4_9 = 75.429639612691
    assert isclose(actual_area_4_9, expected_area_4_9, rel_tol=1e-9), f"Expected {expected_area_4_9}, but got {actual_area_4_9}"

def test_circle_calculation_area_0():   
    circle = Circle(0)
    assert circle.circle_calculation("area") == 0
    
def test_circle_calculation_area_neg():
    circle = Circle(-1)
    assert circle.circle_calculation("area") == "Invalid input for radius" 

def test_circle_calculation_area_tiny():
    circle = Circle(0.0001)
    actual_area_tiny = circle.circle_calculation('area')
    expected_area_tiny = 3.141592653589793e-08
    assert isclose(actual_area_tiny, expected_area_tiny, rel_tol=1e-9), f"Expected {expected_area_tiny}, but got {actual_area_tiny}"

def test_circle_calculation_area_string():
    circle = Circle("HelloWorld")
    assert circle.circle_calculation("area") == "Cannot perform operation with this input"
    
# perimeter tests    
   
def test_circle_calculation_perimeter_int():
    circle = Circle(5)
    actual_perimeter_5 = circle.circle_calculation('perimeter')
    expected_perimeter_5 = 31.41592653589793
    assert isclose(actual_perimeter_5, expected_perimeter_5, rel_tol=1e-9), f"Expected {expected_area_5}, but got {actual_perimeter_5}"
    
def test_circle_calculation_perimeter_float():
    circle = Circle(4.9)
    actual_perimeter_4_9 = circle.circle_calculation('perimeter')
    expected_perimeter_4_9 = 30.78760800518
    assert isclose(actual_perimeter_4_9, expected_perimeter_4_9, rel_tol=1e-9), f"Expected {expected_perimeter_4_9}, but got {actual_perimeter_4_9}"
    
def test_circle_calculation_perimeter_0():
    circle = Circle(0)
    assert circle.circle_calculation("perimeter") == 0
    
def test_circle_calculation_perimeter_neg():
    circle = Circle(-1)
    assert circle.circle_calculation("perimeter") == "Invalid input for radius"
    
def test_circle_calculation_perimeter_tiny():
    circle = Circle(0.0001)
    actual_perimeter_tiny = circle.circle_calculation("perimeter")
    expected_perimeter_tiny = 0.00062831853071796
    assert isclose(actual_perimeter_tiny, expected_perimeter_tiny, rel_tol=1e-9), f"Expected {expected_perimeter_tiny}, but got {actual_perimeter_tiny}"

def test_circle_calculation_perimeter_string():
    circle = Circle("HelloWorld")
    assert circle.circle_calculation("area") == "Cannot perform operation with this input"    

def run_tests():
    test_circle_calculation_area_int()
    test_circle_calculation_area_float()
    test_circle_calculation_area_0()
    test_circle_calculation_area_neg()
    test_circle_calculation_area_tiny()
    test_circle_calculation_area_string()
    test_circle_calculation_perimeter_int()
    test_circle_calculation_perimeter_float()
    test_circle_calculation_perimeter_0()
    test_circle_calculation_perimeter_neg()
    test_circle_calculation_perimeter_tiny()
    test_circle_calculation_perimeter_string()
    print("All tests passed!") # if any assertions fail, AssertionError will be raised
    
if __name__ == "__main__":
    run_tests()