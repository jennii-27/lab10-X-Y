"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass


import math
def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0
        raise ZeroDivisionError("Division by zero")
    return a / b

def log(a, b):
    if a == 0 or a ==1 or b == 0:
        raise ValueError("Cannot calculate log of zero")
        # use math library + raise ValueError
    return math.log(a, b)
def exp(a, b):
    return a**b


