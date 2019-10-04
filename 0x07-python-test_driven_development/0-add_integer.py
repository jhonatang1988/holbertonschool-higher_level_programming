#!/usr/bin/python3
def add_integer(a, b=98):
    result = 0
    if type(a) == type(1.0):
        a = int(a)
    if type(b) == type(1.0):
        b = int(b)
    if not type(a) == type(1):
        raise TypeError("a must be an integer")
    if not type(b) == type(2):
        raise TypeError("b must be an integer")
    return a + b
