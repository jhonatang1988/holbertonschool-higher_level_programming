#!/usr/bin/python3
"""
function to check if object is instance of a class
"""


def is_same_class(obj, a_class):
    """
    Args:
    * obj: object to check
    * a_class: class to check
    """
    if type(obj) == a_class:
        return True
    return False
