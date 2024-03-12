## create helper functions for circle calculations

# import circle class from circle.py
from circle import circle_class

def circle_calc(radius: float, operation: str) -> float:
    """
    Perform a mathematical operation on two values.

    Parameters:
        radius (float): The radius.
        operation (str): The operation to perform. Can be 'area' or 'perimeter'.

    Returns:
        float: The result of the operation.
    """

    # create object of circle class with given radius
    my_circle = circle_class(radius)

    # check operation and call the appropriate method
    if operation == 'area':
        result = my_circle.area()
    else:
        result = my_circle.perimeter()
    
    # return result
    return result
