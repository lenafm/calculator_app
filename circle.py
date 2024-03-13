## Calculation for area and permiter
import math
class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    def perimeter_calculation(self) -> float: ## Perimeter Method
        return 2 * math.pi * self.radius
    def area_calculation(self) -> float:   ## Area Method
        return math.pi * self.radius ** 2