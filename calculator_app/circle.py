# create function to calculate the perimeter of a circle by inputting the radius
import math 
import unittest
    

# create helper functions for calculations


def circle_calculation(value1: float, operation: str) -> float:
    """
    Perform a mathematical operation on two values.

    Parameters:
        value1 (float): radius 
        
        operation (str): The operation to perform. Can be 'area', 'perimeter"

    Returns:
        float: The result of the operation.

    Raises:
        ZeroDivisionError: If attempting to divide by zero.
    """
    if operation == 'Area':
        result = math.pi * value1 ** 2 # πr^2
    else:
        result = 2 * math.pi * value1 # 2πr

    return result


def convert_to_float(value: str) -> float:
    """
    Convert string to floating point number.

    Parameters:
        value (str): The value to convert.

    Returns:
        float: The converted float value of input value.

    Raises:
        ValueError: If value cannot be converted to a float.
    """

    float_value = float(value)

    return float_value



