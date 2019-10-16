#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, encoding="utf-8", mode='w') as a_file:
        return a_file.write(text)
