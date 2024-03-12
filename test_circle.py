from circle import Circle
import math
r = 2
ins = Circle(r)
print(ins.circle_perimeter())

# Testing Perimeter function
assert ins.circle_perimeter() == round((math.pi * 2 * r), 2)

# Testing Area function
assert ins.circle_area() == round((math.pi * r**2), 2)



