# Data Structures & Algorithms Spring 2024
# Problem Set 2
# Lonny Chen, 216697
# helper.py

# create helper functions for calculations

def perform_calculation(value1: float, value2: float, operation: str, rounding_int: int) -> float:
    """
    Perform a mathematical operation on two values.

    Parameters:
        value1 (float): The first value.
        value2 (float): The second value.
        operation (str): The operation to perform. Can be 'add', 'subtract', 'divide', or 'multiply'.
        rounding_int (int): Number of decimal places to round result to.

    Returns:
        float or int: The result of the operation.

    Raises:
        ZeroDivisionError: If attempting to divide by zero.
    """
    if operation == 'add':
        result = value1 + value2
    elif operation == 'subtract':
        result = value1 - value2
    elif operation == 'divide':
        result = value1 / value2
    else:
        result = value1 * value2

    if rounding_int == 0:
        rounded_result = round(result)
    else:
        rounded_result = round(result, rounding_int)

    return rounded_result


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
