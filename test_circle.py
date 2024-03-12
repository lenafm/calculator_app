from circle import Circle

def test_circle(radius : float, operation : str) -> float:
    circle_instance = Circle(radius)
    if operation == "area":
        result = circle_instance.calculate_area()
    else:
        result = circle_instance.calculate_perimeter()
    return result
