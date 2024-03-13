def circle_ops(radius: float, operation: str) -> float:  # Define the 'circle_ops' class
    print(radius)
    if operation == 'perimeter':
        result = 2.0 * 3.14 * radius  # Define the perimeter method
    else:
        result = 3.14 * (radius**2.0) # Define the area method

    return result