#!/usr/bin/python3
"""
class to return a sorted list
"""


class MyList(list):
    """
    Args:
    * new_list = a shadow copy of the list
    """
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print(new_list)
