
from circle import Circle

def test_circle_calculation_area():
    circle = Circle()
    assert circle.circle_calculation(5, "area") == 78.53981633974483
    assert circle.circle_calculation(5.0, "area") == 78.53981633974483
    #assert circle.circle_calculation(-1 "area") == NEED TO MAKE IT ROBUST TO NEG NUMBERS
    assert circle.circle_calculation(0 "area") == 0
    assert circle.circle_calculation("HelloWorld" "area") == "Cannot perform operation with this input"
    
def test_circle_calculation_perimeter():
    circle = Circle()
    assert circle.circle_calculation(5, "perimeter") == 31.41592653589793
    assert circle.circle_calculation(5.0, "perimeter") == 31.41592653589793
    #assert circle.circle_calculation(-1 "area") == NEED TO MAKE IT ROBUST TO NEG NUMBERS
    assert circle.circle_calculation(0 "area") == 0
    assert circle.circle_calculation("HelloWorld" "area") == "Cannot perform operation with this input"    
    
if __name__ == '__main__':
    unittest.main()