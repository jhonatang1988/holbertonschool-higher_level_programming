#!/usr/bin/python3
"""
function to check if is instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
    *obj: object to check
    *a_class: class to compare to
    """
    if isinstance(obj, a_class):
        return True
    return False
