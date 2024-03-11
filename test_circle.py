from circle import Circle

def test_calculate(radius: float, operation: str) -> float:
    circle_instance = Circle(radius)

    if operation == 'perimeter':
        result = circle_instance.calculate_perimeter()
    else:
        result = circle_instance.calculate_area()

    return result