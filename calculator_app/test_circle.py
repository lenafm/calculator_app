import unittest
from circle import circle_calculation

class TestCircleCalculations(unittest.TestCase):
    def test_area(self):
        # Testing area calculation
        result = circle_calculation(value1=5, operation='Area')
        self.assertAlmostEqual(result, 78.53981633974483, places=5)

    def test_perimeter(self):
        # Testing perimeter calculation
        result = circle_calculation(value1=5, operation='Perimeter')
        self.assertAlmostEqual(result, 31.41592653589793, places=5)

if __name__ == '_main_':
    unittest.main()
