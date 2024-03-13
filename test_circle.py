import unittest
from circle import Circle

class TestCircleMethods(unittest.TestCase):

    def test_calculate_perimeter(self):
        circle = Circle(1)  # For a circle with radius 1
        self.assertAlmostEqual(circle.calculate_perimeter(), 2 * 3.14159, places=5)

    def test_calculate_area(self):
        circle = Circle(1)  # For a circle with radius 1
        self.assertAlmostEqual(circle.calculate_area(), 3.14159, places=5)

    def test_calculate_area_small_radius(self):
        circle = Circle(0.5)  # Testing with a smaller radius
        self.assertAlmostEqual(circle.calculate_area(), 3.14159 * 0.5 ** 2, places=5)

    def test_calculate_area_large_radius(self):
        circle = Circle(10)  # Testing with a larger radius
        self.assertAlmostEqual(circle.calculate_area(), 3.14159 * 10 ** 2, places=5)

if __name__ == '__main__':
    unittest.main()