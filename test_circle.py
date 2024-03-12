import unittest
from circle import calculate_area, calculate_circumference


class TestCircleMethods(unittest.TestCase):

    def test_area(self):
        # Testing the area calculation for known values
        self.assertAlmostEqual(calculate_area(0), 0)
        self.assertAlmostEqual(calculate_area(1), 3.141592653589793)
        self.assertAlmostEqual(calculate_area(2.5), 19.634954084936208)

    def test_circumference(self):
        # Testing the circumference calculation for known values
        self.assertAlmostEqual(calculate_circumference(0), 0)
        self.assertAlmostEqual(calculate_circumference(1), 6.283185307179586)
        self.assertAlmostEqual(calculate_circumference(2.5), 15.707963267948966)


if __name__ == '__main__':
    unittest.main()
