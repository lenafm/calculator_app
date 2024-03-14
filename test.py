from helper_circle import circle_perform
import math

def perimeter_test():
    #Create an instance radius=1
    helper_circle = circle_perform(1)

    perimeter = helper_circle.perimeter()
    assert round(perimeter, 8) == round(2 * math.pi, 8)

def area_test():
    #Create an instance radius=1
    helper_circle = circle_perform(1)

    area = helper_circle.area
    assert round(area, 8) == round(math.pi, 8)




