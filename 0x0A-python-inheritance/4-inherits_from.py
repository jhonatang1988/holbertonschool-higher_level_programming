#!/usr/bin/python3
"""
class to check if is subclass
"""


def inherits_from(obj, a_class):
    """
    Args:
    *obj: object
    *a_class: class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
