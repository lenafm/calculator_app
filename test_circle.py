import unittest
from circle import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)

    def test_perimeter(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.perimeter(), 31.41592653589793, places=5)

if __name__ == '__main__':
        unittest.main()