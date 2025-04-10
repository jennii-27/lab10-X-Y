# https://github.com/jennii-27/lab10-X-Y.git

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# Partner 1: Xindi Wang
# Partner 2: Yamirka Varela-Hernandez

# First example
import math
def square_root(a):
    if a <0:
        raise ValueError
    else:
        return math.sqrt(a)
def hypotenuse(a, b):
    result = (a**2+b**2)**(1/2)
    return result

def add(a, b): 
    result = a+b
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

def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def log(a, b):
    if a == 0 or a ==1 or b == 0:
        raise ValueError("Cannot calculate log of zero")
        # use math library + raise ValueError
    return math.log(a, b)
def exp(a, b):
    return a**b

