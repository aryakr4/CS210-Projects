import doctest
import math

def circle_area(diameter):
    ''' Calculates and returns the
    area of a circle given the
    diameter.

    >>> circle_area(12)
    113.09

    (int) -> float

    '''

    r = diameter / 2
    area = math.pi * r**2

    return area




def pizza_calculator(diameter, cost): 
    ''' 
    (int, num) -> float 

    Calculates and returns the cost per square inch 
    of pizza for a pizza of given diameter and cost. 
    Examples: 

    >>> pizza_calculator(16, 18) 
    0.117
    >>> pizza_calculator(14, 20.25)  
    0.132
    ''' 

    r = diameter / 2 
    area = math.pi * r**2 

    cost_per_inch = cost / area 
    cost_per_inch = round(cost_per_inch, 3) 
    return cost_per_inch

print (doctest.testmod())
