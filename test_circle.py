
import unittest
from circle import Circle


class TestCircle(unittest.TestCase):

    def test_calculate_perimeter(self):
        circle = Circle(5)
        # Adjusted expected value to match the exact output
        self.assertAlmostEqual(circle.calculate_perimeter(), 31.41592653589793, places=5)

    def test_calculate_area(self):
        circle = Circle(5)
        # Adjusted expected value to match the exact output
        self.assertAlmostEqual(circle.calculate_area(), 78.53981633974483, places=5)


if __name__ == '__main__':
    unittest.main()
