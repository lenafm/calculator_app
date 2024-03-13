import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)