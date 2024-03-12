from circle import Circle


def test_circle(radius: float, operation: str) -> float:
    # Create an instance of the Circle class
    circle_instance = Circle(radius)

    if operation == 'area':
        result = circle_instance.area()
    else:
        result = circle_instance.perimeter()

    return result

def convert_to_float(value: str) -> float:

    float_value = float(value)

    return float_value


