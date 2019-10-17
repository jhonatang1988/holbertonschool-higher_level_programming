#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            print("{:s}".format(line), end="")
