# Data Structures & Algorithms Spring 2024
# Problem Set 2
# Lonny Chen, 216697
# test_circle.py
#   Usage: pytest test_circle.py or Run in PyCharm IDE

from circle import Circle
import math
import random

def check_circle_area(radius, rounding):
    '''A Circle with input radius returns the expected area with input rounding.'''
    circle = Circle(radius)
    expected = round(math.pi * (radius ** 2), rounding)
    result = circle.area(rounding)
    print(f'Testing area of circle with radius {radius}, rounding {rounding}')
    print(f'Expected: {expected}')
    print(f'Result:   {result}')
    assert expected == result

def check_circle_perimeter(radius, rounding):
    '''A Circle with input radius returns the expected perimeter with input rounding.'''
    circle = Circle(radius)
    expected = round(2 * math.pi * radius, rounding)
    result = circle.perimeter(rounding)
    print(f'Testing perimeter of circle with radius {radius}, rounding {rounding}')
    print(f'Expected: {expected}')
    print(f'Result:   {result}')
    assert expected == result

def generate_random_seed(min, max):
    '''Generate a random seed between input min and max.'''
    seed = random.randint(min, max)
    print(f'\nRandom seed is: {seed}') #note for reproducability
    random.seed(seed)

def test_directed_circle_area(radius_list = [0, 1, 2, math.pi, 10, 100, 1e6]):
    '''Test Circle::area() with interesting radius values.'''
    generate_random_seed(1, 100)
    for r in radius_list:
        rounding = random.randint(0, 10)
        check_circle_area(r, rounding)

def test_directed_circle_perimeter(radius_list = [0, 1, 2, math.pi, 10, 100, 1e6]):
    '''Test Circle::perimeter() with interesting radius values.'''
    generate_random_seed(1, 100)
    for r in radius_list:
        rounding = random.randint(0, 10)
        check_circle_perimeter(r, rounding)

def test_random_circle_area(iterations=10):
    ''' Test Circle::area() with random radius and rounding for input number of iterations.'''
    generate_random_seed(1, 100)
    for i in range(0, iterations):
        print(f'\nIteration #{i}')
        radius = random.uniform(0,1000)
        rounding = random.randint(0, 10)
        check_circle_area(radius, rounding)

def test_random_circle_perimeter(iterations=10):
    ''' Test Circle::perimeter() with random radius and rounding for input number of iterations.'''
    generate_random_seed(1, 100)
    for i in range(0, iterations):
        print(f'\nIteration #{i}')
        radius = random.uniform(0,1000)
        rounding = random.randint(0, 10)
        check_circle_perimeter(radius, rounding)
