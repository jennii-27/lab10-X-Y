"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    result = a+b
    return result
def subtract(a,b):
    result = a-b
    return result
def multiply(a,b):
    result = a*b
    return result
def divide(a,b):
    if a == 0:
        raise ZeroDivisionError('a cannot be 0!')
    result = b/a
    return result

def logarithm(a,b):
    if a == 0 or a == 1 or b == 0:
        raise ValueError
    result = math.log(a,b)
    return result
def exponent(a,b):
    result = a**b
    return result


