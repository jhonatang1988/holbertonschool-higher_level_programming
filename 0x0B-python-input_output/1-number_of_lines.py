#!/usr/bin/python3


def number_of_lines(filename=""):
    counter = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            counter += 1
    return (counter)
