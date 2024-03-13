# create helper functions for calculating radius and perimeter of the circle (rounded to two decimal points)
class Circle:
    """
    A class to represent a circle and perform calculations to it.
    Attributes:
        radius(float): The radius of the circle
    """

    def __init__(self, radius: float):
        """
        Constructs the necessary attributes for the circle class.
        Parameters:
            radius(float): The radius of the circle.
        """
        if radius < 0:
            raise ValueError("positive radius expected")
        self.radius = radius

    def area(self) -> float:
        """
        Calculates the area of the circle.
        Returns:
            float: The area of the circle.
        """
        assert self.radius >= 0, "positive radius expected"
        pi = 3.14159265359
        return round(pi * (self.radius ** 2), 2)

    def perimeter(self) -> float:
        """
        Calculates the perimeter of the circle.
        Returns:
            float: The perimeter of the circle.
        """
        assert self.radius >= 0, "positive radius expected"
        pi = 3.14159265359
        return round(2 * pi * self.radius, 2)
