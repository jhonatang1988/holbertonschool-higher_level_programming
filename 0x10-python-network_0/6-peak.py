#!/usr/bin/python3
"""
finds a peak in a list of integers
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    l = list_of_integers
    last = len(l) - 1
    for i in range(0, last):
        if l[i] > l[i + 1]:
            return l[i]
    return l[last]
