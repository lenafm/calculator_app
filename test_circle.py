
#test Circle class and get_perimeter and get_area methods

import unittest

from circle import Circle

class TestCircle(unittest.TestCase):

    def test_get_perimeter(self):
        circle1 = Circle(1)
        self.assertAlmostEqual(circle1.get_perimeter(), 6.2832)

        circle2 = Circle(2)
        self.assertAlmostEqual(circle2.get_perimeter(), 12.5664)

        with self.assertRaises(ValueError): #check if correct error is shown when radius is 0
            Circle(0)

        with self.assertRaises(ValueError): #check if correct error is shown when radius is negative float
            Circle(-1)

        with self.assertRaises(ValueError): #check if correct error is shown when radius is a string
            Circle("abc")

    def test_get_area(self):
        circle1 = Circle(1)
        self.assertAlmostEqual(circle1.get_area(), 3.1416)

        circle2 = Circle(2)
        self.assertAlmostEqual(circle2.get_area(), 12.5664)

        with self.assertRaises(ValueError): #check if correct error is shown when radius is 0
            Circle(0)

        with self.assertRaises(ValueError): #check if correct error is shown when radius is negative float
            Circle(-1)

        with self.assertRaises(ValueError): #check if correct error is shown when radius is a string
            Circle("abc")


if __name__ == '__main__':
    unittest.main()

