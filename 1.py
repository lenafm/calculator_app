from circle import Circle
import math
r = 2
ins = Circle(r)
print(ins.circle_perimeter())
print(round((math.pi * 2 * r), 2))
print(round((math.pi * r**2), 2))
print(ins.circle_area())